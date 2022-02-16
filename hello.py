from flask import Flask
from flask import jsonify
import pandas as pd
import random
import os
from random import randrange
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Booboo !'

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

@app.route("/user")
def users():
    my_user = os.environ['user']
    msg = "user: " + my_user
    return msg

@app.route("/pass")
def passes():
    my_pass = os.environ['pass']
    msg = "pass: " + my_pass
    return msg

@app.route("/vars")
def vars():
    my_vars = os.environ
    my_vars_dict = dict(my_vars)
    return jsonify(my_vars_dict)


@app.route("/random")
def random():
    
    ret_val = "your random number is: " + str(randrange(100))
    return ret_val

if __name__ == '__main__':
    app.run()
