# Delivers a reddit post from a subreddit based on search critera
import praw
import random
import json
import os

# Connect to Reddit via PRAW
reddit = praw.Reddit(client_id='Us-byLFTjQmSJQ',
                     client_secret=os.environ.get('REDDIT_SECRET', ""),
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
    print("ERROR: Could not find %s on Reddit" % (search_text))
