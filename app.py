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
    app.config["SECRET_KEY"] = 'xxxxxxxxxxxxxxxxxx'
    app.config["SECRET_KEY"] = '1'
    app.config["SECRET_KEY"] = '2'
    app.config["SECRET_KEY"] = '3'
    app.config["SECRET_KEY"] = '4'
    app.config["SECRET_KEY"] = '5'
    app.config["SECRET_KEY"] = '6'
    app.config["SECRET_KEY"] = '7'
    app.config["SECRET_KEY"] = '8'
    app.config["SECRET_KEY"] = '9'
    app.config["SECRET_KEY"] = '10'
    app.config["SECRET_KEY"] = '11'
    app.config["SECRET_KEY"] = '12'
    app.config["SECRET_KEY"] = '13'
    app.config["SECRET_KEY"] = '14'
    app.config["SECRET_KEY"] = '15'
    app.config["SECRET_KEY"] = '16'
    app.config["SECRET_KEY"] = '17'
    app.config["SECRET_KEY"] = '18'
    app.config["SECRET_KEY"] = '19'
    app.config["SECRET_KEY"] = '20'
    app.config["SECRET_KEY"] = '21'
    app.config["SECRET_KEY"] = '22'
    app.config["SECRET_KEY"] = '23'
    app.config["SECRET_KEY"] = '24'
    app.config["SECRET_KEY"] = '25'
    app.config["SECRET_KEY"] = '26'
    app.config["SECRET_KEY"] = '27'
    app.config["SECRET_KEY"] = '28'
    app.config["SECRET_KEY"] = '29'
    app.config["SECRET_KEY"] = '30'
    app.config["SECRET_KEY"] = '31'
    app.config["SECRET_KEY"] = '32'
    app.config["SECRET_KEY"] = '33'
    app.config["SECRET_KEY"] = '34'
    app.config["SECRET_KEY"] = '35'
    app.config["SECRET_KEY"] = '36'
    app.config["SECRET_KEY"] = '37'
    app.config["SECRET_KEY"] = '38'
    app.config["SECRET_KEY"] = '39'
    app.config["SECRET_KEY"] = '40'
    app.config["SECRET_KEY"] = '41'
    app.config["SECRET_KEY"] = '42'
    app.config["SECRET_KEY"] = '43'
    app.config["SECRET_KEY"] = '44'
    app.config["SECRET_KEY"] = '45'
    app.config["SECRET_KEY"] = '46'
    app.config["SECRET_KEY"] = '47'
    app.config["SECRET_KEY"] = '48'
    app.config["SECRET_KEY"] = '49'
    app.config["SECRET_KEY"] = '50'
    app.config["SECRET_KEY"] = '51'
    app.config["SECRET_KEY"] = '52'
    app.config["SECRET_KEY"] = '53'
    app.config["SECRET_KEY"] = '54'
    app.config["SECRET_KEY"] = '55'
    app.config["SECRET_KEY"] = '56'
    app.config["SECRET_KEY"] = '57'
    app.config["SECRET_KEY"] = '58'
    app.config["SECRET_KEY"] = '59'
    app.config["SECRET_KEY"] = '60'
    app.config["SECRET_KEY"] = '61'
    app.config["SECRET_KEY"] = '62'
    app.config["SECRET_KEY"] = '63'
    app.config["SECRET_KEY"] = '64'
    app.config["SECRET_KEY"] = '65'
    app.config["SECRET_KEY"] = '66'
    app.config["SECRET_KEY"] = '67'
    app.config["SECRET_KEY"] = '68'
    app.config["SECRET_KEY"] = '69'
    app.config["SECRET_KEY"] = '70'
    app.config["SECRET_KEY"] = '71'
    app.config["SECRET_KEY"] = '72'
    app.config["SECRET_KEY"] = '73'
    app.config["SECRET_KEY"] = '74'
    app.config["SECRET_KEY"] = '75'
    app.config["SECRET_KEY"] = '76'
    app.config["SECRET_KEY"] = '77'
    app.config["SECRET_KEY"] = '78'
    app.config["SECRET_KEY"] = '79'
    app.config["SECRET_KEY"] = '80'
    app.config["SECRET_KEY"] = '81'
    app.config["SECRET_KEY"] = '82'
    app.config["SECRET_KEY"] = '83'
    app.config["SECRET_KEY"] = '84'
    app.config["SECRET_KEY"] = '85'
    app.config["SECRET_KEY"] = '86'
    app.config["SECRET_KEY"] = '87'
    app.config["SECRET_KEY"] = '88'
    app.config["SECRET_KEY"] = '89'
    app.config["SECRET_KEY"] = '90'
    app.config["SECRET_KEY"] = '91'
    app.config["SECRET_KEY"] = '92'
    app.config["SECRET_KEY"] = '93'
    app.config["SECRET_KEY"] = '94'
    app.config["SECRET_KEY"] = '95'
    app.config["SECRET_KEY"] = '96'
    app.config["SECRET_KEY"] = '97'
    app.config["SECRET_KEY"] = '98'
    app.config["SECRET_KEY"] = '99'
    app.config["SECRET_KEY"] = '100'
