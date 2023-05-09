#!/usr/bin/python3
"""
Queries number of subscribers for a particular subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries number of subscribers for a particular subreddit
    """
    if not isinstance(subreddit, str):
        return 0
    base_url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/femziprof)"}
    response = requests.get(base_url, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
