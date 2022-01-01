## Authenticate your bots

Some time in 2015, Twitter changed the rules for creating apps to require you to have a phone number. This is a problem if the account you want to create an app under is for a bot and you don't have another phone number to burn.

One way around this is to make the app under your primary account. But then how do you authenticate the app for your bot account? By running this script.

Feed it your `consumer_key` and `consumer_secret` at the prompts and it'll give you a URL. Go there logged in as your bot account, authorise the app and get the PIN. Then input the PIN into the command line.

If Twitter instead redirects you, take the value of the `oauth_verifier` parameter in the redirect request and use it as the PIN.

The output is formatted such that you can paste it into a `.env` file and source it. Then access the credentials from the environment with something like
```python
auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"],
                      os.environ["ACCESS_TOKEN_SECRET"])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
```
for Tweepy.
