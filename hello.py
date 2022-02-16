from flask import Flask
import pandas as pd
import random
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

@app.route("/random")
def random():
    
    ret_val = "your random number is: " + str(randrange(100))
    return ret_val

if __name__ == '__main__':
    app.run()
