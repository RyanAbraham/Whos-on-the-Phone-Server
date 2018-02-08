import indicoio
import json
import os
import modules.config as config

indicoio.config.api_key = os.environ.get('INDICO_KEY', "")

def get_keywords(text):
   keywords = indicoio.keywords(text)
   return json.dumps({"keywords": keywords})

