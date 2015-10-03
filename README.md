## Authenticate your bots

Some time in 2015, Twitter changed the rules for creating apps to require you to have a phone number. This is a problem if the account you want to create an app under is for a bot and you don't have another phone number to burn.

One way around this is to make the app under your primary account. But then how do you authenticate the app for your bot account? By running this script.

Feed it your `consumer_key` and `consumer_secret` at the prompts and it'll give you a URL. Go there logged in as your bot account, authorise the app and get the PIN. Then input the PIN into the command line.

The output is formatted such that you can paste it into e.g. `creds.py`. Then just put
```python
from creds import consumer_key, consumer_secret, access_token, access_token_secret
```
into your code.

