from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
        return int(requests.get('http://add-service:5051/'+str(n1)+'/'+str(n2)).text)

def minus(n1, n2):
    return int(requests.get('http://minus-service:5052/'+str(n1)+'/'+str(n2)).text)

def multiply(n1, n2):
    return int(requests.get('http://multiply-service:5080/'+str(n1)+'/'+str(n2)).text)

def divide(n1, n2):
    return int(requests.get('http://div-service:5081/'+str(n1)+'/'+str(n2)).text)
    
def gcd(n1, n2):
	return int(requests.get('http://gcd-service:5082/'+str(n1)+'/'+str(n2)).text)
	
def greater_than(n1, n2):
    return int(requests.get('http://greater-service:5065/'+str(n1)+'/'+str(n2)).text)

def lcm(n1, n2):
    return int(requests.get('http://lcm-service:5070/'+str(n1)+'/'+str(n2)).text)
    
@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        number_1 = int(request.form['first'])
        number_2 = int(request.form['second'])
        operation = request.form.get('operation')
    except:
        return render_template('index.html', result=None)
    result = 0
    if operation == 'add':
        result = add(number_1, number_2)
    elif operation == 'minus':
        result =  minus(number_1, number_2)
    elif operation == 'multiply':
        result = multiply(number_1, number_2)
    elif operation == 'divide':
        result = divide(number_1, number_2)
    elif operation == 'gcd':
        result = gcd(number_1, number_2)
    elif operation == 'greater_than':
        result = greater_than(number_1, number_2)
    elif operation == 'lcm':
        result = lcm(number_1, number_2)

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
