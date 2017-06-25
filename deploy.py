
from flask import Flask, render_template
# import sys
# import logging

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")

@app.route("/dashboard/")
def dashboard():
	return render_template("dashboard.html")

# app.logger.addHandler(logging.StreamHandler(sys.stdout))
# app.logger.setLevel(logging.ERROR)

# app.run(debug=True)