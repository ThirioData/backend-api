import sqlite3

class FoodModel:
    def __init__(self, food_name, food_calorie, food_type, food_cuisine, food_image,food_category, food_description, spice1, spice2, spice3, spice4):
        self.food_name = food_name
        self.food_calorie = food_calorie
        self.food_type = food_type
        self.food_cuisine = food_cuisine
        self.food_image = food_image
        self.food_category = food_category
        self.food_description = food_description
        self.spice1 = spice1
        self.spice2 = spice2
        self.spice3 = spice3
        self.spice4 = spice4

    def json(self):
        return {
            "food_name": self.food_name,
            "food_calorie": self.food_calorie,
            "food_type": self.food_type,
            "food_cuisine": self.food_cuisine,
            "food_image": self.food_image,
            "food_category": self.food_category,
            "food_description": self.food_description,
            "spice1": self.spice1,
            "spice2": self.spice2,
            "spice3": self.spice3,
            "spice4": self.spice4
        }

    @classmethod
    def find_by_food_name(cls, food_name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM foods WHERE food_name=?"
        result = cursor.execute(query, (food_name,))
        row = result.fetchone()
        connection.close()
        if row:
            # return cls(*row)
            return {
                "Foods": row
            }

    # @classmethod
    def insert(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "INSERT INTO foods VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (
            self.food_name, self.food_calorie, self.food_type, self.food_cuisine, self.food_image,
            self.food_category, self.food_description, self.spice1, self.spice2, self.spice3,
            self.spice4))
        connection.commit()
        connection.close()

    # @classmethod
    def update(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "UPDATE foods SET food_calorie=?, food_type=?, food_cuisine=?, food_image=?, food_category=?, food_description=?, spice1=?, spice2=?, spice3=?, spice4=? WHERE food_name=?"
        cursor.execute(query, (
            self.food_calorie, self.food_type, self.food_cuisine, self.food_image,
            self.food_category, self.food_description, self.spice1, self.spice2, self.spice3,
            self.spice4, self.food_name,))
        connection.commit()
        connection.close()