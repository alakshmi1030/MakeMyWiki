from flask import Flask
from flask import render_template
from flask import request
from backend import friendSearch

app = Flask("start")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/",methods=['POST'])
def generate():
	token = request.form["token"]
	friendSearch(token)
	return render_template("index.html")

app.run()