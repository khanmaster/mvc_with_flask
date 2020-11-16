from flask import Flask, jsonify, redirect, url_for

# create an instance of our app
app = Flask(__name__)

students = [
    {"id": 0, "title": "Mr.", "first_name": "Shahrukh", "last_name": "Khan", "course": "DevOps"}
]


# decorator - to create our api/url for user to access our data in the browser
@app.route("/")  # localhost:5000 is default port for Flask
def home():
    return "<h1>This is a dream team of DevOps consultants celebrating a WOW moment!!!</h1> "

@app.route("/welcome/")
def greet_user():
    return " <h1>Welcome to DevOps team</h1>"

# This function runs when the URL/API is accessed

# Creating our own API to display data on the specific route/URL/End point/API
@app.route("/api/v1/student/data/", methods=["GET"])
# this will add this API/URL to  http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students)  # transforms data into Json
    # Utilising Extract Transform Load

@app.route("/login/")
def login():
    return redirect(url_for("greet_user"))

@app.route("/<username>/")
def welcome_user(username):
    return f"<h1>Welcome to the dream team of DevOps dear {username}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
