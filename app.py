import os
import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity
from resources.user import UserRegister
from models.user import UserModel
from resources.food import Food
from resources.foodList import FoodList

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Dodo@N9"
app.config['JWT_AUTH_URL_RULE'] = '/login'
# config JWT to expire within half an hour
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# config JWT auth key name to be 'email' instead of default 'username'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
api = Api(app)
# from app.jwt import authenticate, identity # Must import these after the database connection is made
jwt = JWT(app, authenticate, identity)

class HelloDodo(Resource):
    def get(self):
        return {
        "message": "Welcome to the api",
        "author": "OoOO"
    }

# @jwt.identity_handler
# def identify(payload):
#     return User.query.filter(User.id == payload['identity']).scalar()


class Recommend(Resource):
    @jwt_required()
    def get(self):
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return current_identity, 200

api.add_resource(HelloDodo, '/')
api.add_resource(UserRegister, '/register')
# add foods endpoint here
api.add_resource(Food, '/food/<string:food_name>')
api.add_resource(FoodList, '/foods')
api.add_resource(Recommend, '/dodo')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
