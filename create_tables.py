import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text, email text, firstname text, lastname text, age int, sex char, location text, non_veg text, user_guid text)"
cursor.execute(create_table)
connection.commit()
connection.close()