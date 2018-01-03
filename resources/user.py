from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="Username is required"
                        )
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="Password is also required"
                        )
    parser.add_argument("email",
                        type=str,
                        required=True,
                        help="Email is also required"
                        )
    parser.add_argument("firstname",
                        type=str
                        )
    parser.add_argument("lastname",
                        type=str
                        )
    parser.add_argument("age",
                        type=int
                        )
    parser.add_argument("sex",
                        type=str
                        )
    parser.add_argument("location",
                        type=str
                        )
    parser.add_argument("non_veg",
                        type=str
                        )
    parser.add_argument("user_guid",
                        type=str
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {
                "message": "A user already exists with this userxxxxxxxxxxxxxxxname"
            }, 400

        user = UserModel(**data)
        user.save_to_db()

        return {
            "message": "successfully signed up"
        }, 201, {'Access-Control-Allow-Origin': '*'}
