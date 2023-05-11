#!/usr/bin/python3
"""Recursive function that queries, parses the title of all hot articles, and prints a sorted count of given keywords"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
  """Initialize the counts dictionary if not given"""
  if counts is None:
    counts = {}
    for word in word_list:
      counts[word.lower()] = 0
  
  """Base case: no more posts to process"""
  if after == "":
    return counts
  
  """Build the URL and make the request"""
  url = f"https://www.reddit.com/r/{subreddit}/hot.json"
  if after is not None:
    url += f"?after={after}"
  headers = {"User-Agent": "recursive-function"}
  response = requests.get(url, headers=headers, allow_redirects=False)
  
  """ Check if the response is valid"""
  if response.status_code != 200:
    return counts
  
  """Get the data and the next page"""
  data = response.json().get("data", {})
  after = data.get("after", "")
  posts = data.get("children", [])
  
  """Process each post title and update the counts"""
  for post in posts:
    title = post.get("data", {}).get("title", "").lower()
    for word in word_list:
      word = word.lower()
      """Split the title by non-alphanumeric characters and count the word"""
      if word in title.split():
        counts[word] += title.split().count(word)
  
  """Recursively call the function with the next page"""
  return count_words(subreddit, word_list, after, counts)

"""Example usage"""
subreddit = "programming"
word_list = ["python", "java", "javascript", "go"]
counts = count_words(subreddit, word_list)

""" Sort and print the results"""
sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
for word, count in sorted_counts:
  if count > 0:
    print(f"{word}: {count}")
