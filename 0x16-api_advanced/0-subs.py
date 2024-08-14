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
    res = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers={'User-Agent': 'custom'},
                       allow_redirects=False)
    response = res.json().get('data').get('subscribers')
    if response:
        return response
    else:
        return 0
