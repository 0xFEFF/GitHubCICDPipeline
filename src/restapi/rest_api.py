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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)