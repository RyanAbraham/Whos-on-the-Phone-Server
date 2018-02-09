import indicoio
import json
import os

if os.environ.get('IS_HEROKU', None):
    indicoio.config.api_key = os.environ.get('INDICO_KEY', "")
else:
    import modules.config as conf
    indicoio.config.api_key = conf.indico_key

def get_keywords(text):
   keywords = indicoio.keywords(text)
   return json.dumps({"keywords": keywords})
