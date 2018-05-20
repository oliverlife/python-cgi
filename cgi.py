#!/usr/bin/python
# -*- coding: UTF-8 -*-

# CGI Documents: http://www.ietf.org/rfc/rfc3875.txt
class Respone:
    def __init__(self):
        self.protocol = "HTTP/1.1"
        self.statusMap = {200: "OK"}
        self.status = 200
        self.contentType = "text/html"
        self.header = {}
        self.setCookies = {}
        self.content = ""

    def statusSection(self):
        return "Status:{status} {statusText}\n".format(status = self.status, statusText = self.statusMap[self.status])

    def contentTypeSection(self):
        return "Content-type:{contentType}\n".format(contentType = self.contentType)

    def headerSection(self):
        text = ""
        if hasattr(self, "header"):
            for key, value in self.header.items():
                text += "{0}:{1}\n".format(key, value)

        if hasattr(self, "setCookies"):
            for key, value in self.setCookies.items():
                text += "Set-Cookie:{0}={1};\n".format(key, value)

        return text

    def contentSection(self):
        text = ""
        if hasattr(self, "content"):
            text = self.content
        return text

    def __del__(self):
        print self.contentTypeSection() + self.statusSection() + self.headerSection() + "\n" + self.contentSection()

import cgi, cgitb
cgitb.enable()

import os

respone = Respone()
respone.setCookies["cookie-test"] = "test"
respone.setCookies["cookie-test2"] = "test2"
respone.header["xixi"] = "ts ejr"

str = ""
str += "<meta charset=\"utf-8\">"
str += "<b>环境变量 hahahuohuo</b><br>"
str += "<ul>"
for key in os.environ.keys():
    str += "<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key])
str += "</ul>"
respone.content = str

