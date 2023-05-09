#!/usr/bin/python3
"""
Gets the top 10 hot posts for a subreddit
"""
import requests

def top_ten(subreddit):
    """
    Gets the top 10 hot posts for a subreddit
    """
    if not isinstance(subreddit, str):
        print("None")
        return
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/femziprof)"}
    response = requests.get(base_url, headers=headers)
    if response.status_code != 200:
        print("None")
        return
    hot_posts = response.json().get("data", {}).get("children", [])
    for post in hot_posts[:10]:
        title = post.get("data", {}).get("title", "")
        print(title)
