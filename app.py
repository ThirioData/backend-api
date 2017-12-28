from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from models.user import UserRegister

app = Flask(__name__)
app.secret_key = "Dodo@N9"
api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
# add foods endpoint here
api.add_resource(FoodList, '/')

app.run(debug=True, port=5000)