# dishook.py
Webhooks library for python

Installation.

In CMD Line:
  pip install dishook.py
 
If you don't have pip installed:
 Search for the library on pypi and install it manually.
 

# Usage:

This usage is made for people who don't even really don't know Python. I made this easy so people who struggle with Webhooks can easily send messages to them now. More features will be added.

First you need to import the library:

from dishook.py import Webhook

Then you have to create the webhook instance.
WEBHOOKURL should be replaced with the webhook url you want to use.
avatar_url is if you want to use an avatar_url when you haven't set it in a function. (optional)
If you want to use multiple webhooks at once replace 'WEBHOOKURL' with an array/list.
You'd make an array/list
urlArray = ['url1', 'url2']
and put the array/list in your Webhook instance.
Or make an array/list in the instance like so:
webhook = Webhook(['url1', 'url2'])

webhook = Webhook('WEBHOOKURL', avatar_url=None)

Functions:
To use a function you need to use the instance you have created in the top of your code and then use the function.
If you don't understand this then please look at an example.


send_message(message, username, avatar_url=None)

Send a message as the webhook.
If avatar_url is None it will use the default avatar you gave in the webhook instance.
If you didn't define an url in the webhook instance no avatar_url is used unless you have defined avatar_url in the function.
If you don't want to input an avatar_url and don't want to use the default one you defined either.
set avatar_url to an empty string or just ONE space. The avatar_url will be removed from the payload.
Returns discord status code for more information on status codes look at the status code wiki.


change_url(urls/urls)

Change the current's webhook url. If you have multiple webhooks
change your array/list accordingly.
for instance you want to add a url
You would do this:

urlArray.append('webhookurl')
change_url(urlArray)

Removing one is the same concept except you don't use append but .remove() or .pop()
You can also use a new array/list with new urls. Or go from an array/list to just one webhook url.

change_default_avatar_url(url)

Change the default avatar url you defined in the webhook instance.


# Discord Status Codes




