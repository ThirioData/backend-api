from flask_restful import Resource
from models.food import FoodModel


class FoodList(Resource):
    def get(self):
        return {
            "foods": [food.json() for food in FoodModel.query.all()]
        }, 200
