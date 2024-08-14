#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and
returns a list containing the titles of
all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Returns a list containing the titles of all hot articles
    for a given subreddit.
    """
    reddit = "https://www.reddit.com/"
    header = {'user-agent': 'my-app/0.0.1'}
    if after is None:
        return hot_list

    url = reddit + "r/{}/hot/.json".format(subreddit)
    params = {'limit': 100, 'after': after}

    res = requests.get(url, headers=header, params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        res_data = res.json()
        after = res_data['data']['after']
        hot_list.extend([child['data']['title']
                         for child in res_data['data']['children']])
        return recurse(subreddit, hot_list, after)
    except ValueError:
        return None
