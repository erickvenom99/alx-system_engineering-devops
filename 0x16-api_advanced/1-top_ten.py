#!/usr/bin/python3
"""
Quries Reddit and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the tifles of the first 10
       hot posts
    """
    url = "https://www.reddit.com/r/{s}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'custom'}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code == 200:
            data = res.json()
            titles = [post['data']['title'] for post in
                      data['data']['children']]
            for title in titles:
                print(title)
        else:
            print(None)
    except requests.RequestException:
        print(None)
