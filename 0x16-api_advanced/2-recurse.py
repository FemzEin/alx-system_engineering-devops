#!/usr/bin/python3
"""
Returns a list of all the hot titles in a subreddit
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of all the hot titles in a subreddit
    """
    if not isinstance(subreddit, str):
        return None
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        base_url += f"&after={after}"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/femziprof)"}
    response = requests.get(base_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    response = response.json()
    after = response.get("data", {}).get("after")
    hot_posts = response.get("data", {}).get("children", [])
    hot_list.extend([post.get("data", {}).get("title") for post in hot_posts])
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
