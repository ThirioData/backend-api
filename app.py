import os
from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.food import Food
from resources.foodList import FoodList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Dodo@N9"
api = Api(app)

jwt = JWT(app, authenticate, identity)

class HelloDodo(Resource):
    def get(self):
        return {
        "message": "Welcome to the api",
        "author": "OoOO"
    }

api.add_resource(HelloDodo, '/')
api.add_resource(UserRegister, '/register')
# add foods endpoint here
api.add_resource(Food, '/food/<string:food_name>')
api.add_resource(FoodList, '/foods')

port = int(os.environ.get("PORT", 5000))
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, port=port)
