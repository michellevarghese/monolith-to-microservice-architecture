from flask import Flask
from flask_restful import Api, Resource
import requests
import os

app = Flask(__name__)
api = Api(app)

# Create a class which inherits Resource class from flask_restful
class Add(Resource):
    def get(self, number1, number2):
        return number1 + number2
# Handle all types of data with constructor overloading

api.add_resource(Add,'/<int:number1>/<int:number2>')

# Test the app
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5051,
        host="0.0.0.0"
    )

