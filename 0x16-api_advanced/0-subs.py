#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import json
import requests


def get_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Softboi/0.0.1'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
