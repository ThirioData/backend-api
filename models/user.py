import sqlite3
from flask_restful import Resource, reqparse

class UserModel:
    def __init__(self, _id, username, password, email, firstname, lastname, age, sex, location, non_veg, user_guid):
        self.id = _id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.age = age
        self.sex = sex
        self.location = location
        self.non_veg = non_veg
        self.user_guid = user_guid

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row is not None:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row is not None:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

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

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (data['username'], data['password'], data['email'], data['firstname'], data['lastname'], data['age'], data['sex'], data['location'], data['non_veg'], data['user_guid']))

        connection.commit()
        connection.close()
        return {
            "message": "successfully signed up"
        }, 201