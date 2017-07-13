
from flask import Flask, render_template, make_response
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

@app.route("/dashboard/")
def dashboard():
	try:
		return render_template("dashboard.html", methods=["GET", "POST"], TOPIC_DICT =TOPIC_DICT, )
	except Exception as e:
		return (str(e))

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

#Math pages
@app.route("/2012_AIME_6/")
def AIME_2012():
	return render_template("2012_AIME_6.html")

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