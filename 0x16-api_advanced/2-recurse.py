#!/usr/bin/python3
"""
Returns a list of all the hot titles in a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of all the hot titles in a subreddit
    """
    if type(subreddit) is not str:
        return None
    s = subreddit
    base_url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(s)
    if after is not None:
        base_url += "&after={}".format(after)
    headers = {'user-agent': 'safari:holberton/0.1.0 (by /u/Nacho_Buddy)'}
    response = requests.get(base_url,
                            headers=headers,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    response = response.json()
    after = response.get("data").get("after")
    hot_posts = response.get("data").get("children")
    hot_list.extend(map(lambda p: p.get("data").get("title"), hot_posts))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
