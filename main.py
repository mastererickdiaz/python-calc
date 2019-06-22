#!/usr/bin/env python

import re, json

from bottle import route, run, template
from bottle import request, response, hook
from bottle import post, get, put, delete


from modules.calc import Calc



"""
import mysql.connector

cnx = mysql.connector.connect(host='db', database='api_db', user='root', password='myclave')
cursor = cnx.cursor()
"""

_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers


@route('/', method=['GET'])
def save_handler():
    return "Hello"


@route('/add', method=['POST', 'OPTIONS'])
def save_handler():
    if request.method == "OPTIONS":
      return json.dumps({'status': True})

    status = False
    result = None
    data = request.json
    print("data:", data)
    if data is not None:
        if data['number1'] is not None and \
            data['number2'] is not None:
            calc = Calc()
            result = calc.add(data['number1'], data['number2'])
            #sql_insert_query = "insert into `personaje` values(NULL, '%s', '%s', '%s')" % (data['first_name'], data["last_name"], data["twitter"])
            #result  = cursor.execute(sql_insert_query)
            #cnx.commit()
            status = True

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'status': status, 'result': result})

@route('/sub', method=['POST', 'OPTIONS'])
def save_handler():
    if request.method == "OPTIONS":
      return json.dumps({'status': True})

    status = False
    result = None
    data = request.json
    if data is not None:
        if data['number1'] is not None and \
            data['number2'] is not None:
            calc = Calc()
            result = calc.sub(data['number1'], data['number2'])
            status = True

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'status': status, 'result': result})

@route('/mul', method=['POST', 'OPTIONS'])
def save_handler():
    if request.method == "OPTIONS":
      return json.dumps({'status': True})

    status = False
    result = None
    data = request.json
    if data is not None:
        if data['number1'] is not None and \
            data['number2'] is not None:
            calc = Calc()
            result = calc.mul(data['number1'], data['number2'])
            status = True

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'status': status, 'result': result})

@route('/div', method=['POST', 'OPTIONS'])
def save_handler():
    if request.method == "OPTIONS":
      return json.dumps({'status': True})

    status = False
    result = None
    data = request.json
    if data is not None:
        if data['number1'] is not None and \
            data['number2'] is not None:
            calc = Calc()
            result = calc.div(data['number1'], data['number2'])
            status = True

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'status': status, 'result': result})


run(host='0.0.0.0', reloader=True, port=8080)
