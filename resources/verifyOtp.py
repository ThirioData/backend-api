from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
# import the modal for accessing it's method
from models.user import UserModel

class VerifyOtp(Resource):
    """ already signup user verifying for otp"""
    # get the useremail and related data
    parser = reqparse.RequestParser()
    parser.add_argument("company", type=str, required=True, help="Please select company name")
    parser.add_argument("name", type=str, required=True, help="Your name")
    parser.add_argument("username", type=str, required=True, help="Username")
    parser.add_argument("mobileno", type=int, required=True, help="Your mobile number")


    @jwt_required()
    def post(self):
        """ User must already registered """
        data = VerifyOtp.parser.parser_args()
        if not UserModel.find_by_username(data['username']):
            # send otp to the user phone no.
            pass
        else:
            return {
                "message": "You are not registered user"
            }, 400

