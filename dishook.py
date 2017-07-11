import requests

class Webhook:
    webhookurl = None

    def __init__(self, webhookurl):
        self.webhookurl = webhookurl

    def change_url(self, webhookurl):
        self.webhookurl = webhookurl

    def send_message(self, message, username, avatar_url=None):
        if avatar_url == None:
            payload = {
                "content":message,
                "username":username
            }
        else:
            payload = {
                "content":message,
                "username":username,
                "avatar_url":avatar_url
            }
        sess = requests.session()
        response = sess.post(self.webhookurl, data=payload)
        print(response.status_code)
