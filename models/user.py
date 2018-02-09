from db import db

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(100))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(1))
    location = db.Column(db.String(80))
    non_veg = db.Column(db.String(80))
    user_guid = db.Column(db.Integer)
    mobileno = db.Column(db.Integer)

    def __init__(self, username, password, email, firstname, lastname, age, sex, location, non_veg, user_guid):
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
        self.mobileno = mobileno

    # def __repr__(self):
    #     return self.username

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()