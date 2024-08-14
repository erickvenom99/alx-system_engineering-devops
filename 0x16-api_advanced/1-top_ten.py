#!/usr/bin/python3
"""
Queries Reddit and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10
       hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            print("None")
            return

        data = res.json()['data']['children']

        if len(data) == 0:
            print("None")
            return

        for titles in data:
            print(titles['data']['title'])
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except (KeyError, IndexError):
        print("None")
