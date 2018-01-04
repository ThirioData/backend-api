from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.food import FoodModel

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

    @jwt_required()
    def get(self, food_name):
        food = FoodModel.find_by_food_name(food_name)
        if food:
            # return food.json()
            return food.json()
        return {
            "message": "No food item found"
        }, 404

    @jwt_required()
    def post(self, food_name):
        food = FoodModel.find_by_food_name(food_name)
        if food:
            return {
                "message": "food food_name with '{}' already exists".format(food_name)
            }, 400, {'Access-Control-Allow-Origin': '*'}
        data = Food.parser.parse_args()
        food = FoodModel(data['food_name'], data['food_calorie'], data['food_type'], data['food_cuisine'], data['food_image'], data['food_category'], data['food_description'], data['spice1'], data['spice2'], data['spice3'], data['spice4'])
        try:
            food.save_to_db()
        except:
            return {
                "message": "Error occured durig insertion"
            }, 500
        return food.json(), 201

    # @jwt_required()
    def put(self, food_name):
        data = Food.parser.parse_args()
        food = FoodModel.find_by_food_name(food_name)

        if food is None:
            food = FoodModel(data['food_name'], data['food_calorie'], data['food_type'], data['food_cuisine'], data['food_image'], data['food_category'], data['food_description'], data['spice1'], data['spice2'], data['spice3'], data['spice4'])
        else:
            food.food_name = data['food_name']
            food.food_calorie = data['food_calorie']
            food.food_type = data['food_type']
            food.food_cuisine = data['food_cuisine']
            food.food_image = data['food_image']
            food.food_category = data['food_category']
            food.food_description = data['food_description']
            food.spice1 = data['spice1']
            food.spice2 = data['spice2']
            food.spice3 = data['spice3']
            food.spice4 = data['spice4']
        food.save_to_db()
        return food.json(), {'Access-Control-Allow-Origin': '*'}

    @jwt_required()
    def delete(self, food_name):
        food = FoodModel.find_by_food_name(food_name)
        if food:
            food.delete_from_db()
        return {
            "message": "Successfully deleted {}".format(food_name)
        }
