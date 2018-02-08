import indicoio
import json
import os

indicoio.config.api_key = os.environ.get('INDICO_KEY', "")

def get_keywords(text):
   keywords = indicoio.keywords(text)
   return json.dumps({"keywords": keywords})

