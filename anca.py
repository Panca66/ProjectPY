from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')

# def index():
# 	return "<h1>Proiect final</h1>"
def index():
	first_name = "Anca"
	return render_template('index.html', first_name=first_name)

@app.route('/user/<name>')

def user(name):
	return render_template('users.html', user_name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500