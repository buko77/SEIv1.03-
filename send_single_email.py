#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:40:02 2013

@author: claes
"""
import re
import smtplib, glob, string, datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders 

def send_email(debug,toaddr2,msgsubject,fromaddr,template,smtp_server,username,password):
    replyto = fromaddr
    htmlmsgtext = template
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
    msg.add_header('To', toaddr2)
    msg.add_header('Subject', msgsubject)
    msg.add_header('Reply-To', replyto)
    server = smtplib.SMTP(smtp_server)
    if debug == True:
            server.set_debuglevel(True)
    
    server.starttls()
    server.login(username,password)
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    print ">sent email"
    server.quit()
    print ">closed session"
        
    #except:
    #    print ">error sending email"
