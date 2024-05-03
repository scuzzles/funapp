from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "hello from vercel app"

@app.route("/about")
def about():
    return "hello about"

app.run(host="0.0.0.0", port=8080)