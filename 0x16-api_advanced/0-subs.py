#!/usr/bin/python3
"""A function that returns the total number of
subscribers for a reddit account."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a
    given subreddit."""
    if not subreddit and type(subreddit) != str:
        return 0

    route = 'https://www.reddit.com'
    r = requests.get('{}/r/{}/about.json'.format(route, subreddit),
                     headers={'User-Agent': 'tediyang'},
                     allow_redirects=False).json()

    subs = r.get("data", {}).get("subscribers", 0)
    return subs
