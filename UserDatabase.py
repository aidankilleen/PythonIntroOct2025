# UserDatabase.py


import sqlite3

from User import User


class UserDatabase:

    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
    
    def get_all_users(self):
        users = []
        cursor = self.conn.cursor()
        sql = "SELECT * FROM users"
        result_set = cursor.execute(sql)
        for record in result_set:
            (id, name, email, active) = record
            users.append(User(id, name, email, active))
        return users

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db_file = "./users.db"

    udb = UserDatabase(db_file)
    users = udb.get_all_users()

    print (users)
    for user in users:
        print (user.name)

    udb.close()

