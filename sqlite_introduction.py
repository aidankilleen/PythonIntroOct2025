# sqlite_introduction.py


import sqlite3


conn=sqlite3.connect("./users.db")
cursor = conn.cursor()
sql = "SELECT * FROM users"
result_set = cursor.execute(sql)

for record in result_set:
    (id, name, email, active) = record
    print (f"{id} {name} {email} {("Active" if active else "Inactive")}")


conn.close()







