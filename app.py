from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.food import Food
from resources.foodList import FoodList

app = Flask(__name__)
app.secret_key = "Dodo@N9"
api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
# add foods endpoint here
api.add_resource(Food, '/food/<string:food_name>')
api.add_resource(FoodList, '/foods')

if __name__ == '__main__':
    app.run(debug=True, port=5000)