#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers, if invalid subreddit is given the function
returns None
"""
import requests


def number_of_subscribers(subreddit):
    """ tasks reddit user name and return the subscribers number """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    Heads = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=Heads,  allow_redirects=False)

    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    else:
        return 0
