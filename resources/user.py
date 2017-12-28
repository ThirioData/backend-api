from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
               type=str,
               required=True,
               help="Username cannot be empty"
               )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Password cannot be empty"
                        )