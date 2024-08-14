#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers, if invalid subreddit is given the function
returns None
"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "custom"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return None
    return res.json().get('data', {}).get('subscribers', 0)
