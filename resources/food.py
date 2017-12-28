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

    @classmethod
    def insert(cls, food):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "INSERT INTO foods VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (
        food['food_name'], food['food_calorie'], food['food_type'], food['food_cuisine'], food['food_image'],
        food['food_category'], food['food_description'], food['spice1'], food['spice2'], food['spice3'],
        food['spice4']))
        connection.commit()
        connection.close()

    @classmethod
    def update(cls, food):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "UPDATE foods SET food_calorie=?, food_type=?, food_cuisine=?, food_image=?, food_category=?, food_description=?, spice1=?, spice2=?, spice3=?, spice4=? WHERE food_name=?"
        cursor.execute(query, (
            food['food_calorie'], food['food_type'], food['food_cuisine'], food['food_image'],
            food['food_category'], food['food_description'], food['spice1'], food['spice2'], food['spice3'],
            food['spice4', food['food_name']]))
        connection.commit()
        connection.close()

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
        food = {
            "food_name": data['food_name'],
            "food_calorie": data['food_calorie'],
            "food_type": data['food_type'],
            "food_cuisine": data['food_cuisine'],
            "food_image": data['food_image'],
            "food_category": data['food_category'],
            "food_description": data['food_description'],
            "spice1": data['spice1'],
            "spice2": data['spice2'],
            "spice3": data['spice3'],
            "spice4": data['spice4']
        }
        try:
            self.insert(food)
        except:
            return {
                "message": "Error occured durig insertion"
            }, 500
        return food, 201

    # @jwt_required()
    def put(self, food_name):
        data = Food.parser.parse_args()
        food = self.find_by_food_name(food_name)
        updated_food = {
            # "food_name": data['food_name'],
            "food_calorie": data['food_calorie'],
            "food_type": data['food_type'],
            "food_cuisine": data['food_cuisine'],
            "food_image": data['food_image'],
            "food_category": data['food_category'],
            "food_description": data['food_description'],
            "spice1": data['spice1'],
            "spice2": data['spice2'],
            "spice3": data['spice3'],
            "spice4": data['spice4']
        }
        if food is None:
            try:
                self.insert(updated_food)
            except:
                return {
                    "message": "Server insertion error on insert"
                }, 500
        else:
            try:
                self.update(updated_food)
            except:
                return {
                    "message": "error occured on update"
                }, 500
        return updated_food

    @jwt_required()
    def delete(self, food_name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "DELETE FROM foods WHERE food_name =?"
        result = cursor.execute(query, (food_name,))
        connection.commit()
        connection.close()
        return {
            "message": "Successfully deleted {}".format(food_name)
        }
