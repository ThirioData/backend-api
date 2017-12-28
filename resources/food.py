import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Food(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("food_name",
                        type=str,
                        required=True,
                        help="Food food_name must be provided"
                        )
    parser.add_argument("food_calorie",
                        type=int,
                        required=True,
                        help="Food calorie must pe provided in integers"
                        )
    parser.add_argument("food_type",
                        type=str,
                        required=True,
                        help="food_type must be veg or non-veg"
                        )
    parser.add_argument("food_cuisine",
                        type=str,
                        required=True,
                        help="food_cuisine must be provided which region food belongs to."
                        )
    parser.add_argument("food_image",
                        type=str,
                        required=True,
                        help="A valid link to food"
                        )
    parser.add_argument("food_category",
                        type=str,
                        required=True,
                        help="food_category must be provided what type of food it is"
                        )
    parser.add_argument("food_description",
                        type=str,
                        required=True,
                        help="a valid description of food_description"
                        )
    parser.add_argument("spice1",
                        type=str,
                        required=True,
                        help="spice1 inside the food"
                        )
    parser.add_argument("spice2",
                        type=str,
                        required=True,
                        help="spice2 inside the food"
                        )
    parser.add_argument("spice3",
                        type=str,
                        required=True,
                        help="spice3 inside the food"
                        )
    parser.add_argument("spice4",
                        type=str,
                        required=True,
                        help="spice4 inside the food"
                        )

    @classmethod
    def find_by_food_name(cls, food_name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM foods WHERE food_name=?"
        result = cursor.execute(query, (food_name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {
                "Foods": row
            }

    @jwt_required()
    def get(self, food_name):
        food = self.find_by_food_name(food_name)
        if food:
            return food
        return {
            "message": "No food item found"
        }, 404

    @jwt_required()
    def post(self, food_name):
        food = self.find_by_food_name(food_name)
        if food:
            return {
                "message": "food food_name with '{}' already exists".format(food_name)
                # "dodo": "lives here '{}'".format(self)
            }, 400
        data = Food.parser.parse_args()

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "INSERT INTO foods VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        result = cursor.execute(query, (data['food_name'],data['food_calorie'], data['food_type'], data['food_cuisine'], data['food_image'], data['food_category'], data['food_description'], data['spice1'], data['spice2'], data['spice3'], data['spice4']))
        connection.commit()
        connection.close()
        return {
            "message": "Successfully added records"
        }, 201
