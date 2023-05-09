#!/usr/bin/python3
'''Get ALL articles for a given subreddit'''
import pprint
import requests


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Softboi/0.0.1'}
    response = requests.get(url, headers=headers, params={'limit': 100})
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after'] is not None:
            recurse(subreddit, hot_list=hot_list, after=data['data']['after'])
        else:
            return hot_list
    else:
        return None
