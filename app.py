from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/system")
def system():
    return os.system("ls")


@app.route("/system2")
def system2():
    return os.system(request.args["command"])


@app.route("/system3")
def system3():
    os.system(request.args["1"])
    os.system(request.args["2"])
    os.system(request.args["3"])
    os.system(request.args["4"])
    os.system(request.args["5"])

@app.route("/secret")
def secret():
    app.config["SECRET_KEY"] = 'xxxxxxxxxxxxxxxxxx'
