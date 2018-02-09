from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
# import the modal for accessing it's method
from models.user import UserModel
from resources.twiliohelper import TwilioHelper

class GenerateOtp(Resource):
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
        data = GenerateOtp.parser.parse_args()
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


class Verify(Resource):
    # get the useremail and related data
    parser = reqparse.RequestParser()
    parser.add_argument("mobileno", type=str, required=True, help="Your mobile number")
    parser.add_argument("token", type=int, required=True, help="your token")

    def post(self):
        data = Verify.parser.parse_args()
        mobileno, token = data['mobileno'], data['token']
        oldUser = TwilioHelper()
        oldUser.verify(mobileno, token)