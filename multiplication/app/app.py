from flask import Flask
from flask_restful import Api, Resource
import requests
import os

app = Flask(__name__)
api = Api(app)

class Multiply(Resource):
    def get(self, number1, number2):
        return int(number1) * int(number2)


api.add_resource(Multiply, '/<int:number1>/<int:number2>')
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5080,
        host="0.0.0.0"
    )
