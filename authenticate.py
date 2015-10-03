#!/usr/bin/env python3
# Authenticate a twitter app!

import tweepy

consumer_key = input("consumer_key: ")
consumer_secret = input("consumer_secret: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_url = auth.get_authorization_url()

print("\n" + auth_url, "\n")

pin = input("PIN: ").strip()

auth.get_access_token(pin)

print()
print("consumer_key = \"" + consumer_key + "\"")
print("consumer_secret = \"" + consumer_secret + "\"")
print("access_token = \"" + auth.access_token + "\"")
print("access_token_secret = \"" + auth.access_token_secret + "\"")

