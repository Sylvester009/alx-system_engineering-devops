#!/usr/bin/python3
"""
0. How many subs?
"""

from requests import get

def number_of_subscribers(subreddit):
    # Check if the subreddit is valid
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
