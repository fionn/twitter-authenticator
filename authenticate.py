#!/usr/bin/env python3
"""Authenticate a twitter app!"""

import tweepy

def main() -> None:
    """Entry point"""
    consumer_key = input("consumer_key: ")
    consumer_secret = input("consumer_secret: ")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()

    print("\n" + auth_url, "\n")

    pin = input("PIN: ").strip()

    auth.get_access_token(pin)

    print()
    print(f"export API_KEY=\"{consumer_key}\"")
    print(f"export API_SECRET=\"{consumer_secret}\"")
    print(f"export ACCESS_TOKEN=\"{auth.access_token}\"")
    print(f"export ACCESS_TOKEN_SECRET=\"{auth.access_token_secret}\"")

if __name__ == "__main__":
    main()
