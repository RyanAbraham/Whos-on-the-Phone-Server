import indicoio
import json
import os
import operator

if os.environ.get('IS_HEROKU', None):
    indicoio.config.api_key = os.environ.get('INDICO_KEY', "")
else:
    import modules.config as conf
    indicoio.config.api_key = conf.indico_key

"""Return a list of keywords from the given text"""
def get_keywords(text):
   keywords = indicoio.keywords(text)
   return json.dumps({ "keywords": keywords })

"""Return a general tag closest related to the given text"""
def get_tag(text):
    tags = indicoio.text_tags(text)
    # Get the key with the highest correlation value
    best_tag = max(tags.items(), key=operator.itemgetter(1))[0]
    return json.dumps({ "tag": best_tag })
