#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and
returns a list containing the titles of
all hot articles for a given subreddi
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".
    format(subreddit, after)
    headers = {'User-Agent': 'custom'}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code == 200:
            data = res.json()
            if "error" in data:
                return None
            hot_list.extend([post['data']['title'] for post in
                             data['data']['children']])
            if data['data']['after']:
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
