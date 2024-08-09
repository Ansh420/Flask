from flask import Flask , render_template, url_for
from employess import employess_data


# create the flask app
app = Flask(__name__)

# home page
@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title="Home")

@app.route("/MorningStar")
def MorningStar():
    return render_template("MorningStar.html", title="MorningStar")

# about page
@app.route("/about")
def about():
	return render_template("about.html", title="about")

@app.route("/employees")
def employees():
	return render_template("emps.html", title="employees", employees=employess_data)

@app.route("/employees/managers")
def managers():
	return render_template("managers.html", title="managers", employees=employess_data)
    

@app.route("/solve/<int:num>")
def solve(num):
	return render_template("solve.html", title="solve", number=num)

# example of path parameter
@app.route("/welcome/<name>")
def welcome(name):
	return f"<h1>Hi {name.title()}, you're welcome to this Page!</h1>"


# example of integer path parameter
@app.route("/addition/<int:num>")
def addition(num):
	return f"<h1>Input is {num}, Output is {num + 10}</h1>"


# example of two integer path parameters
@app.route("/addition_two/<int:num1>/<int:num2>")
def addition_two(num1, num2):
	return f"<h1>{num1} + {num2} is {num1 + num2}</h1>"


# start the app
if __name__ == "__main__":
	app.run(debug=True)