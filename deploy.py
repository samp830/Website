
from flask import Flask, render_template
from content_management import Content 
# import sys
# import logging

TOPIC_DICT = Content()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")

@app.route("/dashboard/")
def dashboard():
	try:
		return render_template("dashboard.html", TOPIC_DICT =TOPIC_DICT )
	except Exception as e:
		return (str(e))

@app.route("/lecture1/")
def prop_logic():
	return render_template("lecture1.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")

# app.logger.addHandler(logging.StreamHandler(sys.stdout))
# app.logger.setLevel(logging.ERROR)

# app.run(debug=True)