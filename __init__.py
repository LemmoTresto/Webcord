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
        if str(type(self.webhook_url)).replace("<class '", "").replace(">'", "") == 'array' or str(type(self.webhook_url)).replace("<class '", "").replace(">'", "") == 'list':
            for url in self.webhook_url:
                response = sess.post(url, data=payload)
                print(response.status_code)
        else:
            response = sess.post(self.webhook_url, data=payload)
            print(response.status_code)

    def send_embed(self, embed, username, avatar_url=None):
                # Check for input of avatar url in function itself
        if avatar_url == None:
            #Check if user wants default avatar url
            if self.avatar_url == None:
                #Doesn't have default avatar_url defined.
                payload = {
                    "embeds": [{embed}],
                    "username":username
                }
            else:
                #Want's to use default avatar from webhook instance.
                payload = {
                    "embeds": [{embed}],
                    "username":username,
                    "avatar_url":self.avatar_url
                }
        #Doesn't want to use default avatar url nor any input avatar url.
        elif avatar_url == '' or avatar_url == ' ':
           payload = {
               "embeds": [{embed}],
               "username":username
           }
        else:
            #Avatar_url was inputted in this function.
            payload = {
                "embeds": [{embed.to_dict()}],
                "username":username,
                "avatar_url":avatar_url
            }
        sess = requests.session()
        if str(type(self.webhook_url)).replace("<class '", "").replace(">'", "") == 'array' or str(type(self.webhook_url)).replace("<class '", "").replace(">'", "") == 'list':
            for url in self.webhook_url:
                response = sess.post(url, data=payload)
                print(response.status_code)
        else:
           response = sess.post(self.webhook_url, data=payload)
           print(response.status_code)

