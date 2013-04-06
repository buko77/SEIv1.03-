#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:40:40 2013

@author: claes
"""

import time
import datetime
import re
import smtplib, glob, string, datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders   


def send_email_to_list(debug,line,fromaddr,template,smtp_server,msgsubject,username,password):     
    replyto = fromaddr
    htmlmsgtext = template
    try:
        msgtext = htmlmsgtext.replace('<b>','').replace('</b>','').replace('<br>',"\r").replace('</br>',"\r").replace('<br/>',"\r").replace('</a>','')
        msgtext = re.sub('<.*?>','',msgtext)
        msg = MIMEMultipart()
        msg.preamble = 'This is a multi-part message in MIME format.\n'
        msg.epilogue = ''

        body = MIMEMultipart('alternative')
        body.attach(MIMEText(msgtext))
        body.attach(MIMEText(htmlmsgtext, 'html'))
        msg.attach(body)

        msg.add_header('From', fromaddr)
        msg.add_header('To', line)
        msg.add_header('Subject', msgsubject)
        msg.add_header('Reply-To', replyto)
        server = smtplib.SMTP(smtp_server)
        if debug == True:
            server.set_debuglevel(True)
        
        server.starttls()
        server.login(username,password)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        print ">sent to: ",line
        server.quit()
        print ">closed session"
        print ">sleeping, dont want to flood smtp server"
        time.sleep(1)
        
    except Exception,e:
        print str(e)
        print ">error sending email ",line

