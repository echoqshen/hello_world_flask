from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Booboo !'

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

if __name__ == '__main__':
    app.run()
