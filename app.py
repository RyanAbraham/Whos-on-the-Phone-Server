from flask import Flask
from flask_cors import CORS
import modules.reddit as red
import modules.indico as ico
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    with open("dict.md") as f:
        lines = f.readlines()
        return random.choice(lines) + random.choice(lines) + random.choice(lines)

@app.route("/reddit/<subreddit>/<search>", methods=['GET'])
def reddit_sub(subreddit, search):
    return red.fetch_post(subreddit, search)

@app.route("/reddit/<search>")
def reddit(search):
    return red.fetch_post("all", search)

@app.route("/indico/keywords/<text>")
def keywords(text):
    return ico.get_keywords(text)

if __name__ == "__main__":
    app.run()
