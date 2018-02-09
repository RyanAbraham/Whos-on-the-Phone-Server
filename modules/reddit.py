# Delivers a reddit post from a subreddit based on search critera
import praw
import random
import json
import os

if os.environ.get('IS_HEROKU', None):
    reddit_secret = os.environ.get('REDDIT_SECRET', '')
else:
    import modules.config as conf
    reddit_secret = conf.reddit_secret

# Connect to Reddit via PRAW
reddit = praw.Reddit(client_id='Us-byLFTjQmSJQ',
                     client_secret=reddit_secret,
                     user_agent='python:com.ryanabraham.whophone:v1.0')

# search_text should be passed in as a string
def fetch_post(subreddit, search_text):
    all_posts = reddit.subreddit(subreddit)
    for post in all_posts.search(search_text, limit=1):
        return json.dumps({
            'title': post.title,
            'text': post.selftext,
            'subreddit': post.subreddit_name_prefixed
            })
    print("WARNING: Could not find %s on Reddit" % (search_text))
    return json.dumps({
        'title': "",
        'text': "",
        'subreddit': ""
    })
