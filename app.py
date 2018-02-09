from flask import Flask
from flask_cors import CORS
import modules.reddit as red
import modules.indico as ico
import json
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    with open("dict.md") as f:
        lines = f.readlines()
        return random.choice(lines) + random.choice(lines) + random.choice(lines)

@app.route("/reddit/<subreddit>/<search>", methods=['GET'])
def reddit_sub(search, subreddit):
    return red.fetch_post(search, subreddit)

@app.route("/reddit/<search>")
def reddit(search):
    return red.fetch_post(search)

@app.route("/indico/keywords/<text>")
def keywords(text):
    return ico.get_keywords(text)

@app.route("/indico/tag/<text>")
def tag(text):
    return ico.get_tag(text)

@app.errorhandler(404)
def route_not_found(err):
    return json.dumps({ 'message': 'Unknown route', 'code': '404' }), 404

if __name__ == "__main__":
    app.run()
