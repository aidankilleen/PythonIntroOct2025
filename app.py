# app.py

# create a web application


from flask import Flask, render_template

from UserDAO import UserDAO


app = Flask(__name__)



@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/info")
def info():
    return "<h1>Info</h1>"

@app.route("/users")
def users():
    dao = UserDAO("./users.db")
    users = dao.get_all_users()

    html = ""
    for user in users:
        html += user.name

    dao.close()

    title = "User Information List"
    return render_template("user_list.html", 
                           title=title, 
                           users=users)


if __name__ == "__main__":

    app.run(debug=True)