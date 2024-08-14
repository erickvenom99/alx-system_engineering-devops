#!/usr/bin/python3
"""Task 3"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """function that queries the Reddit API, parses the title of
        all hot articles, and prints a sorted count of given keywords
    """
    res_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if res_info.status_code != 200:
        return None

    data_info = res_info.json()

    hot_list = [child.get("data").get("title")
                for child in data_info
                .get("data")
                .get("children")]
    if not hot_list:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot_list:
        title_words = title.lower().split()
        for word in word_list:
            word_count[word] += title_words.count(word.lower())

    if not data_info.get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[1],
                               reverse=True)
        for k, v in sorted_counts:
            if v != 0:
                print(f'{k}: {v}')
    else:
        return count_words(subreddit, word_list, word_count,
                           data_info.get("data").get("after"))
