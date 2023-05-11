#!/usr/bin/python3
'''Get ALL articles for a given subreddit'''
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        after (str): The parameter for the next page of the API results.
        counts (int): The parameter of results matched thus far.
    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)

    headers = {'User-Agent': 'softboi/0.0.1'}
    response = requests.get(url, headers=headers)
    data = response.json()

    articles = data['data']['children']
    for article in articles:
        title = article['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            if word in title.split():
                counts[word] = counts.get(word, 0) + 1

    next_page = data['data']['after']
    if next_page:
        return count_words(subreddit, word_list, after=next_page,
                           counts=counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
