#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers, if invalid subreddit is given the function
returns None
"""
import requests


def number_of_subscribers(subreddit):
    try:
        respond = requests.get('https://www.reddit.com/r/{}/about.json'.format
                               (subreddit), headers={'User-Agent': 'custom'},
                               allow_redirects=False)
        return respond.json().get('data').get('subscribers')
    except:
        return 0
