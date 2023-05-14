#!/usr/bin/python3
"""
A function that shows the top ten posts
"""

import requests as req


def top_ten(subreddit):
    """
    Returns the top ten posts for a
    given subreddit
    """

    if not subreddit and type(subreddit) != str:
        return 0

    route = 'https://www.reddit.com'
    params = {'limit': 10}
    r = req.get('{}/r/{}/hot.json'.format(route, subreddit), params=params,
                headers={'User-Agent': 'tediyang'},
                allow_redirects=False)
    if r.status_code == 404:
        print("None")
        return
    results = r.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
