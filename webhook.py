# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015-2016 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import json
import requests


class Webhook:
    webhook_url = None
    avatar_url = None

    def __init__(self, webhook_url, avatar_url=None):
        self.webhook_url = webhook_url
        self.avatar_url = avatar_url

    def change_url(self, webhook_url):
        self.webhook_url = webhook_url

    def change_avatar_url(self, avatar_url):
        self.avatar_url = avatar_url

    def send_message(self, message, username, avatar_url=None):
        # Check for input of avatar url in function itself
        if avatar_url == None:
            #Check if user wants default avatar url
            if self.avatar_url == None:
                #Doesn't have default avatar_url defined.
                payload = {
                    "content":message,
                    "username":username
                }
            else:
                #Want's to use default avatar from webhook instance.
                payload = {
                    "content":message,
                    "username":username,
                    "avatar_url":self.avatar_url
                }
        #Doesn't want to use default avatar url nor any input avatar url.
        elif avatar_url == '' or avatar_url == ' ':
           payload = {
               "content":message,
               "username":username
           }
        else:
            #Avatar_url was inputted in this function.
            payload = {
                "content":message,
                "username":username,
                "avatar_url":avatar_url
            }
        sess = requests.session()
        if str(type(self.webhook_url)).replace("<class '", "").replace(">'", "").replace("'>", "") == 'array' or str(type(self.webhook_url)).replace("<class '", "").replace(">'", "").replace("'>", "") == 'list':
            # do request for every webhook.
            for url in self.webhook_url:
                resp = sess.post(url, data=payload)
                print(resp.status_code)
        elif str(type(self.webhook_url)).replace("<class '", "").replace(">'", "").replace("'>", "") == 'str':
            resp = sess.post(self.webhook_url, data=payload)
            print(resp.status_code)
        else:
            print("Eror in webhook url(s)! Webhook url should be a string, list or array.")
            return None

    def send_embed(self, embed, username, avatar_url=None):
        embedDict = embed.to_dict()
        del embedDict['type']
                # Check for input of avatar url in function itself
        if avatar_url == None:
            #Check if user wants default avatar url
            if self.avatar_url == None:
                #Doesn't have default avatar_url defined.
                payload = {
                    "username":username,
                    "embeds": [embedDict]
                }
            else:
                #Want's to use default avatar from webhook instance.
                payload = {
                    "username":username,
                    "avatar_url":self.avatar_url,
                    "embed":[embedDict]
                }
        #Doesn't want to use default avatar url nor any input avatar url.
        elif avatar_url == '' or avatar_url == ' ':
           payload = {
               "username":username,
               "embed":[embedDict]
           }
        else:
            #Avatar_url was inputted in this function.
            payload = {
                "username":username,
                "avatar_url":avatar_url,
                "embed":[embedDict]
            }
        sess = requests.session()
        payload = json.dumps(payload)
        headers = {'content-type': 'application/json'}
        if str(type(self.webhook_url)).replace("<class '", "").replace(">'", "").replace("'>", "") == 'array' or str(type(self.webhook_url)).replace("<class '", "").replace(">'", "").replace("'>", "") == 'list':
            # do request for every webhook.
            for url in self.webhook_url:
                resp = sess.post(url, data=payload, headers=headers)
                print(resp.status_code)
        elif str(type(self.webhook_url)).replace("<class '", "").replace(">'", "").replace("'>", "") == 'str':
            resp = sess.post(self.webhook_url, data=payload, headers=headers)
            print(resp.status_code)
        else:
            print("Eror in webhook url(s)! Webhook url should be a string, list or array.")
            return None

#todo: create objects to return?? idk
