from flask import Flask

app = Flask(__name__)


@app.route("/")
def Home():
    return "Hello Flask from Vercel"


@app.route("/about")
def About():
    return "About page"


@app.route("/contact")
def About():
    return "Contact page"
