from flask import Flask
from flask_restful import Api, Resource
import requests
import os
import math
app = Flask(__name__)
api = Api(app)


class Gcd(Resource):
    def get(self, number1, number2):
        return math.gcd(int(number1), int(number2))
        

api.add_resource(Gcd, '/<int:number1>/<int:number2>')
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5082,
        host="0.0.0.0"
    )
