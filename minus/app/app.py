from flask import Flask
from flask_restful import Api, Resource
import requests
import os

app = Flask(__name__)
api = Api(app)

# Create a class which inherits Resource class from flask_restful
class Min(Resource):
    def get(self, number1, number2):
        return int(number1) - int(number2)

# Handle all types of data with constructor overloading

api.add_resource(Min,'/<int:number1>/<int:number2>')

# Test the app
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5052,
        host="0.0.0.0"
    )

