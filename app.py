from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/system")
def system():
    return os.system("ls")
