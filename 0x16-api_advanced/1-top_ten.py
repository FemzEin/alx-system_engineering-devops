#!/usr/bin/python3
"""
Gets the top 10 hot posts for a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Gets the top 10 hot posts for a subreddit
    """
    result = ""
    if type(subreddit) is not str:
        result = "None\n"
    else:
        base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'user-agent': 'safari:holberton/0.1.0 (by /u/Nacho_Buddy)'}
        response = requests.get(base_url,
                                headers=headers)
        if response.status_code != 200:
            result = "None\n"
        else:
            hot_posts = response.json().get("data").get("children")
            for i in range(10):
                title = hot_posts[i].get("data").get("title")
                result += "{}\n".format(title)
    print(result, end="")
