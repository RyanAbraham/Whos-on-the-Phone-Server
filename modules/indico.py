import indicoio
import json
import modules.config as config

indicoio.config.api_key = config.indico_api_key

def get_keywords(text):
   keywords = indicoio.keywords(text)
   return json.dumps({"keywords": keywords})

