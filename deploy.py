
from flask import Flask, render_template, make_response
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

@app.route("/simple")
def simple():
    import datetime
    import StringIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

# app.logger.addHandler(logging.StreamHandler(sys.stdout))
# app.logger.setLevel(logging.ERROR)

# app.run(debug=True)