#!/usr/bin/env python
# encoding: utf-8 

import json 
from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'Alice'})

@app.route('/me/')
def me():
    return jsonify({'name': 'Lucas'})

if __name__ == "__main__":
    app.run(host="172.17.0.2", port=5000)