#!/usr/bin/python
# -*- coding: UTF-8 -*-

# CGI Documents: http://www.ietf.org/rfc/rfc3875.txt
class Respone(object):
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

    def raw(self):
        return self.contentTypeSection() + self.statusSection() + self.headerSection() + "\n" + self.contentSection()

    def __del__(self):
        print(self.raw())

class JsonRespone(Respone):
    def super(self):
        return super(JsonRespone,self)

    def __init__(self):
        self.super().__init__()
        self.json = {}
        self.contentType = "text/json"

    def contentSection(self):
        self.content = json.dumps(self.json)
        return self.super().contentSection()

import cgi, cgitb
cgitb.enable()

import os
import json

respone = JsonRespone()
respone.setCookies["cookie-test"] = "test1013377"
respone.setCookies["cookie-test2"] = "test1023388"
respone.header["xixi"] = "ts ejr"
respone.json = {"a": "b", "c": {"a": "bee22"}}

