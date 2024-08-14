#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers, if invalid subreddit is given the function
retursn None

"""
import requests


def number_of_subscribers(subreddit):
    """Query reddit API
    """
    res = requests.get(
            f'https://www.reddit.com/r/{subreddit}/about.json',
            headers={'User-Agent': 'custom'},
            allow_redirects=False
        )
    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    else:
        return 0
