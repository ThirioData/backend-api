from db import db

class FoodModel(db.Model):
    __tablename__ = "foods"
    food_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_name = db.Column(db.String(80))
    food_calorie = db.Column(db.String(80))
    food_type = db.Column(db.String(80))
    food_cuisine = db.Column(db.String(80))
    food_image = db.Column(db.String(200))
    food_category = db.Column(db.String(80))
    food_description = db.Column(db.String)
    spice1 = db.Column(db.String(80))
    spice2 = db.Column(db.String(80))
    spice3 = db.Column(db.String(80))
    spice4 = db.Column(db.String(80))

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
        return cls.query.filter_by(food_name=food_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()