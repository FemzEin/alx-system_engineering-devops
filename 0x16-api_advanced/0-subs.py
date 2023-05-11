#!/usr/bin/python3
"""
Queries number of subscribers for a particular subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries number of subscribers for a particular subreddit
    """
    if type(subreddit) is not str:
        return 0
    base_url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {'user-agent': 'safari:holberton/0.1.0 (by /u/Nacho_Buddy)'}
    response = requests.get(base_url,
                            headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")
