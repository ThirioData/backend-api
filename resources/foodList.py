import sqlite3
from flask_restful import Resource


class FoodList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM foods"
        results = cursor.execute(query)
        foods = []
        for row in results:
            foods.append({
                'food_id': row[0],
                'food_name': row[1],
                'food_calorie': row[2],
                'food_type': row[3],
                'food_cuisine': row[4],
                'food_image': row[5],
                'food_category': row[6],
                'food_description': row[7],
                'spice1': row[8],
                'spice2': row[9],
                'spice3': row[10],
                'spice4': row[11]
            })
        connection.close()
        return {
            "foods": foods
        }