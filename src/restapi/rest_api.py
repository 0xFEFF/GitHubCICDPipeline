#!/usr/bin/env python
# encoding: utf-8 

import json 
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'Alice'})

@app.route('/me/')
def me():
    return json.dumps({'name': 'Lucas'})

@app.route('/you/')
def me():
    return json.dumps({'name': 'Your Name'})

if __name__ == "__main__":
    app.run(host="172.17.0.2", port=5000)