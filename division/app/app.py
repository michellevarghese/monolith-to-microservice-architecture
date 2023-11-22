from flask import Flask
from flask_restful import Api, Resource
import requests
import os

app = Flask(__name__)
api = Api(app)

class Division(Resource):
    def get(self, number1, number2):
        x = int(number1) / int(number2)
        return int(x)


api.add_resource(Division, '/<int:number1>/<int:number2>')
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5081,
        host="0.0.0.0"
    )
