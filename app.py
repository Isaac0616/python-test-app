import json
import os

from json import dumps

import flask

from flask import request

app = flask.Flask(__name__)


@app.route("/user")
def user():
    user_dict = get_user(request.args.get("id"))
    os.system(request.args.get("command"))
    # ruleid:use-jsonify
    return json.dumps(user_dict)


@app.route("/user2")
def user2():
    user_dict = get_user(request.args.get("id"))
    # ruleid:use-jsonify
    return dumps(user_dict)


def get_user():
    return {}
