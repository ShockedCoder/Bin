#!/bin/python

import os
from bottle import route, run, template

@route('/hello')
def hello():
    return '<b>Hello gay jakub man!</b>'

run(host='192.168.10.87', port=8080, debug=True)
