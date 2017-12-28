import sqlite3

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