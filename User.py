# User.py

# an object is a programming construct that has data and methods in single unit
# properties / member variables / fields
# methods / member functions

# promote code reuse
# model things from the real world using objects

# oo programming came to prominence in the 80's with C++

class User:
    def __init__(self, id, name, email, active):
        self.id = id
        self.name = name
        self.email = email
        self.active = active

    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return f"{self.id} {self.name} {self.email} {"Active" if self.active else "Inactive"}"
    
    def display(self):
        print ("User Object")
        print (self.id)
        print (self.name)
        print (self.email)
        print ("Active" if self.active else "Inactive")


if __name__ == "__main__":
    users = [User(1, "Alice", "alice@gmail.com", True), 
            User(2, "Bob", "bob@gmail.com", True), 
            User(3, "Carol", "carol@gmail.com", True), 
            User(4, "Dan", "dan@gmail.com", False)]

    for user in users:
        user.display()

    active_users = [user for user in users if user.active == True]

    for user in active_users:
        print (user.name)

    print (active_users)

    u = User(5, "Eve", "eve@gmail.com", False)


    print (u)

