import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text, email text, firstname text, lastname text, age int, sex char, location text, non_veg text, user_guid text)"
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS foods(food_id INTEGER PRIMARY KEY, food_name text, food_calorie int, food_type text, food_cuisine text, food_image text, food_category text, food_description blob, spice1 text, spice2 text, spice3 text, spice4 text)"
cursor.execute(create_table)
cursor.execute("INSERT INTO foods VALUES (NULL, 'dodo', 123, 'lunch', 'kashmiri', 'http://somewhere.world', 'veg', 'a good food with healty diet', 'mirchi', 'dhaniya', 'haldi', 'secret')")
connection.commit()
connection.close()