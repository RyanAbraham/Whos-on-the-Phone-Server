# Delivers a reddit post from a subreddit based on search critera
import praw
import prawcore
import json
import os
import random

if os.environ.get('IS_HEROKU', None):
    reddit_secret = os.environ.get('REDDIT_SECRET', '')
else:
    import modules.config as conf
    reddit_secret = conf.reddit_secret

# Connect to Reddit via PRAW
reddit = praw.Reddit(client_id='Us-byLFTjQmSJQ',
                     client_secret=reddit_secret,
                     user_agent='python:com.ryanabraham.whophone:v1.0')

"""Return post information based on the search criteria
search_text -- Text to search for on Reddit - string
subreddit -- Subreddit to search - string (Optional)"""
def fetch_post(search_text, subreddit="all"):
    all_posts = reddit.subreddit(subreddit)
    search_results = []
    try:
        search_results = list(all_posts.search(search_text, limit=10))
    except prawcore.exceptions.Redirect:
        print("WARNING: Could not find subreddit %s" % (subreddit))
    except prawcore.exceptions.RequestException:
        print("ERROR: Could not establish connection to Reddit")
    if search_results:
        post = random.choice(search_results)
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
