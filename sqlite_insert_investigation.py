# sqlite_insert_investigation.py


import sqlite3


conn=sqlite3.connect("./users.db")
cursor = conn.cursor()

name = input("Enter a name to be inserted into the database:")
email = f"{name.lower()}@gmail.com"

sql = f"INSERT INTO users (name, email, active) VALUES('{name}', '{email}', 0)"

result_set = cursor.execute(sql)

conn.commit()

conn.close()







