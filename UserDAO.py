# UserDatabase.py
import sqlite3

from User import User

class UserDAO:
    """ UserDAO class
    Data Access Object for the user.db 

    Please call the .close() method when finished with the database.
    """

    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
    
    def get_all_users(self):
        """return all user objects in the database"""
        users = []
        cursor = self.conn.cursor()
        sql = "SELECT * FROM users"
        result_set = cursor.execute(sql)
        for record in result_set:
            (id, name, email, active) = record
            users.append(User(id, name, email, active))
        return users

    def get_user_by_id(self, id):
        """get user with specified id, return None if user doesn't exist"""
        cursor = self.conn.cursor()
        # sql = f"SELECT * FROM users WHERE id = {id}"
        sql = f"SELECT * FROM users WHERE id = ?"
        result_set = cursor.execute(sql, (id,))
        record = result_set.fetchone()

        if record is None:
            return None
        
        (id, name, email, active) = record#
        user = User(id, name, email, active)
        return user
     
    def delete(self, id):
        """delete the user with this id, returns True or False"""
        cursor = self.conn.cursor()     
        sql = "DELETE FROM users WHERE id = ?"   
        res = cursor.execute(sql, (id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def add(self, user):
        """Function to add a new user
        
        Returns the newly created user, including the id that was assigned by the database
        Note user.id is ignored it will not be used for the new user
        """
        cursor = self.conn.cursor() 
        sql = "INSERT INTO users (name, email, active) VALUES(?, ?, ?)"

        cursor.execute(sql, (user.name, user.email, user.active))
        self.conn.commit()

        # read the new id from the database
        user.id = cursor.lastrowid

        return user
    
    def update(self, user):
        """update the record with user.id returns True if record exists"""
        sql = "UPDATE users SET name = ?, email = ?, active = ? WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (user.name, user.email, int(user.active), user.id))
        self.conn.commit()
        return cursor.rowcount > 0  # returns True if a row was updated

    def close(self):
        """Close the database"""
        self.conn.close()

if __name__ == "__main__":
    db_file = "./users.db"

    udb = UserDAO(db_file)

    new_user = User(-1, "New User", "new.user@gmail.com", True)

    added_user = udb.add(new_user)

    print (added_user)

    added_user.name = "CHANGED"
    added_user.email = "changed@gmail.com"
    added_user.active = not added_user.active

    udb.update(added_user)


    # CRUD
    # Create
    # Retrieve
    # Update
    # Delete







    if udb.delete(5):
        print ("deleted")
    else:
        print ("not deleted")

    user5 = udb.get_user_by_id(5)
    print (user5)


    users = udb.get_all_users()

    print (users)
    for user in users:
        print (user.name)

    udb.close()

  