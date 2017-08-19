
from flask import Flask, render_template, make_response, request, url_for, redirect
from content_management import Content 
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from io import BytesIO
# import sys
# import logging

TOPIC_DICT = Content()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")

@app.route("/dashboard/", methods=["GET", "POST"])
def dashboard():
	error = None
	try:
		if request.method == "POST":
			attempted_username = request.form["username"]
			attempted_password = request.form["password"]
			if attempted_username == "admin" and attempted_password == "password":
				return redirect(url_for('index'))
			else:
				error = "Wrong Credentials :)"
				return render_template("dashboard.html", TOPIC_DICT =TOPIC_DICT, error = error)
	except Exception as e:
		return (str(e))
	return render_template("dashboard.html", TOPIC_DICT =TOPIC_DICT)

#Notes
@app.route("/QuickNotes/")
def QuickNotes():
	return render_template("quicknotes.html")

@app.route("/MatPlotlib/")
def Matplotlib():
	return render_template("MatPlotlib.html")

#CS70 pages

@app.route("/lecture1/")
def prop_logic():
	return render_template("lecture1.html")

# Neural Net pages
@app.route("/chapter1/")
def basic_nn():
	return render_template("chapter1nn.html")

@app.route("/convnets/")
def convnets():
	return render_template("convnets.html")
@app.route("/deeplearning/")
def deeplearning():
	return render_template("deeplearning.html")
@app.route("/hyperparameters/")
def hyperparameters():
	return render_template("hyperparameters.html")

#Math pages
@app.route("/2012_AIME_6/")
def AIME_2012():
	return render_template("2012_AIME_6.html")

@app.route("/Taylor+Fourier/")
def Taylor_Fourier():
	return render_template("taylor_fourier.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")


@app.route('/plot.png')
def plot():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]

    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

# app.logger.addHandler(logging.StreamHandler(sys.stdout))
# app.logger.setLevel(logging.ERROR)

# app.run(debug=True)