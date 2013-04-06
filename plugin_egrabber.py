#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:26:00 2013

@author: claes
"""

import sys
import re
import string
import urllib2
import httplib
import re
import threading
import random


class email_searcher(threading.Thread):
    def remove_to(text):
        finished = 0
        while not finished:
            finished = 1
            start = text.find("<")
            if start >= 0:
                stop = text[start:].find(">")
                if stop >= 0:
                    text = text[:start] + text[start+stop+1:]
                    finished = 0
        return text

    domain_name_to_search=raw_input("domain to search: ")
    pages_to_search = raw_input("pages to search: ")
    print ">scanning google for: ",domain_name_to_search
    print ">using random agent"
    d={}
    web_calcu = 0
    # based on -> http://www.catswhocode.com/blog/how-to-using-python-and-google-to-find-hundreds-of-e-mail-adresses
    google_warning = """
    google can blocking you if you running this plugin to often
    """
    print google_warning
    file_to_save_to = "email_list.data"
    file = open(file_to_save_to, "w")
    browser_agents = """Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01
Mozilla/5.0 (Windows NT 6.1; rv:2.0b7pre) Gecko/20100921 Firefox/4.0b7pre
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.106 Safari/535.2
Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0
Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.106 Safari/535.2
"""     
    print ">using random agent"
    lines = browser_agents.splitlines()
    random_agent = random.choice(lines) 
    print random_agent
    try:
        while web_calcu <pages_to_search:
            status = "http://groups.google.com/groups?q="+str(domain_name_to_search)+"&hl=en&lr=&ie=UTF-8&start=" + repr(web_calcu) + "&sa=N"
            request = urllib2.Request(status)
            request.add_header("User-Agent", random_agent)
            opener = urllib2.build_opener()
            text = opener.open(request).read()
            emails_addresses = (re.findall('([\w\.\-]+@'+domain_name_to_search+')',remove_to(text)))
            for email in emails_addresses:
                d[email]=1
                uniq_emails=d.keys()
            #web_calcu = web_calcu +10
    except KeyboardInterrupt:
        print "exit by user ..."
        exit()
    except Exception as e: 
        print(e)
        print "> [zero]"
        pass
   
    page_counter_web=0
    try:
        while page_counter_web >pages_to_search:
            status2 = "http://www.google.com/search?q=%40"+str(domain_name_to_search)+"&hl=en&lr=&ie=UTF-8&start=" + repr(page_counter_web) + "&sa=N"
            request_web = urllib2.Request(status2)
            request_web.add_header("User-Agent", random_agent)
            opener_web = urllib2.build_opener()
            text = opener_web.open(request_web).read()
            emails_addresses = (re.findall('([\w\.\-]+@'+domain_name_to_search+')',remove_to(text)))
            for email2 in emails_addresses:
                d[email2]=1
                uniq_emails=d.keys()
            #page_counter_web = page_counter_web +10

    except:
        print "> [zero]"
        pass
    
    for uniq_emails_web in d.keys():
        print uniq_emails_web+""
        file.write(uniq_emails_web+"\n")
        
print ">done scanning for emails"

