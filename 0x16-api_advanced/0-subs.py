#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers, if invalid subreddit is given the function
returns None
"""
import requests


def number_of_subscribers(subreddit):
    """Query reddit API"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'my-app/0.0.1'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        response = res.json().get('data', {}).get('subscribers', 0)
        return response
    else:
        return 0
