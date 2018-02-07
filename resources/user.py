from flask_restful import Resource, reqparse
from models.user import UserModel
import csv

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
                        type=int
                        )
    parser.add_argument("location",
                        type=int
                        )
    parser.add_argument("non_veg",
                        type=int
                        )
    parser.add_argument("calories",
                        type=int
                        )
    parser.add_argument("meal_size_rating",
                        type=int
                        ),
    parser.add_argument("previous_meal_size",
                        type=int
                        ),
    parser.add_argument("user_guid",
                        type=int
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        data['calories'] = 100
        data['meal_size_rating'] = 1
        data['previous_meal_size'] = 1
        if UserModel.find_by_username(data['username']):
            return {
                "message": "A user already exists with this userxxxxxxxxxxxxxxxname"
            }, 400

        user = UserModel(**data)
        # save to user_features
        filds = [data['age'], data['calories'], data['location'], data['non_veg'], data['sex'], data['meal_size_rating'], data['previous_meal_size'], data['user_guid']]
        with open(r'user_features', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
        user.save_to_db()

        return {
            "message": "successfully signed up"
        }, 201
