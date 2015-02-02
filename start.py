from flask import Flask
from flask import render_template
from flask import request
from backend import friendSearch
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore

app = Flask("start")
app.config['SOCIAL_FACEBOOK'] = {
    'consumer_key': '764244473658268',
    'consumer_secret': 'c2d3bf09dcc94bc043fa27c5fe9a9e95'
}

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/",methods=['POST'])
def generate():
	token = request.form["token"]
	friendSearch(token)
	return render_template("index.html")

app.run()