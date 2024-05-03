from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "hello from vercel app"

@app.route("/about")
def about():
    return "hello about"
