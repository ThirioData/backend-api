import os
import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
from authy.api import AuthyApiClient

from security import authenticate, identity
from resources.user import UserRegister
from models.user import UserModel
from resources.food import Food
from resources.foodList import FoodList
from resources.order import Order
from file_to_start import getrecommendation

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "postgresql://localhost/oooo")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# twilio config
app.config['TWILIO_ACCOUNT_SID'] = 'ACf47c31d9ae7326a853f37ecec24bfdef'
app.config['TWILIO_AUTH_TOKEN'] = 'dc68342dfa63281de3ab78131a9fa200'
app.config['TWILIO_NUMBER'] = '+16196482390'
app.secret_key = "Dodo@N9"
app.config['JWT_AUTH_URL_RULE'] = '/login'
twilioapi = AuthyApiClient(app.config['MH4y8ZkYq7HHcnx683vVRJ7qWeabIpan'])
# config JWT to expire within half an hour
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# config JWT auth key name to be 'email' instead of default 'username'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
api = Api(app)
# from app.jwt import authenticate, identity # Must import these after the database connection is made
jwt = JWT(app, authenticate, identity)

class TwilioApi:
    def __init__():
        return AuthyApiClient(app.config['MH4y8ZkYq7HHcnx683vVRJ7qWeabIpan'])

class HelloDodo(Resource):
    def get(self):
        return {
        "message": "Welcome to the api",
        "author": "OoOO"
    }







class VerifyOtp(Resource):
    """ already signup user verifying for otp"""
    # get the useremail and related data
    parser = reqparse.RequestParser()
    parser.add_argument("company", type=str, required=True, help="Please select company name")
    parser.add_argument("name", type=str, required=True, help="Your name")
    parser.add_argument("username", type=str, required=True, help="Username")
    parser.add_argument("mobileno", type=str, required=True, help="Your mobile number")


    # @jwt_required()
    def post(self):
        """ User must already registered """
        data = VerifyOtp.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            # send otp to the user phone no.
            toNumber = int(data['mobileno'])
            mobno = str(toNumber)
            oldUser = TwilioHelper()
            code = oldUser.send_confirmation_code(mobno)
            return {
                code: code
            }
        else:
            return {
                "message": "You are not registered user"
            }, 400


def generate_code():
    return str(random.randrange(100000, 999999))

def send_sms(to_number, body):
    account_sid = 'ACf47c31d9ae7326a853f37ecec24bfdef'
    auth_token = 'dc68342dfa63281de3ab78131a9fa200'
    # auth_api_key = 'MH4y8ZkYq7HHcnx683vVRJ7qWeabIpan'
    twilio_number = '+16196482390'
    client = Client(account_sid, auth_token)
    # api = TwilioApi()
    twilioapi.phones.verification_start(to_number, '+91', via='sms')
    phoneNo = "+91" + to_number
    message = client.messages.create(phoneNo, from_=twilio_number, body=body)


class TwilioHelper:
    # @classmethod
    def send_confirmation_code(self, to_number):
        verification_code = generate_code()
        send_sms(to_number, verification_code)
        # print("send_confirmation")
        return verification_code

    def verify(self, phone_number, token):
        # api = TwilioApi()
        verification = twilioapi.phones.verification_check(phone_number, "+91", token)
        if verification.ok():
            return {
                "message": "successfully verified the mobile no"
            }, 201

        # Error in verification    
        return {
            "message": "Error verifying the phone no"
        }







# @jwt.identity_handler
# def identify(payload):
#     return User.query.filter(User.id == payload['identity']).scalar()


class Recommend(Resource):
    @jwt_required()
    def get(self):
        # Access the identity of the current user with get_jwt_identity
        # current_user = get_jwt_identity()
        userId = int(getattr(current_identity, 'id', None))
        # currentUser = UserModel.find_by_id(userId)
        recommendation = getrecommendation(userId)
        return recommendation, 200

api.add_resource(HelloDodo, '/')
api.add_resource(UserRegister, '/register')
# add foods endpoint here
api.add_resource(Food, '/food/<string:food_name>')
api.add_resource(FoodList, '/foods')
api.add_resource(Recommend, '/dodo')
api.add_resource(VerifyOtp, '/verify')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
