
from flask import Flask

app = Flask(__name__)

@app.route("/yo")
def blogs():
    return "<h1> Using Virtualenv w/ flask and heroku </h1> <p> Go to python directory, cd into scripts and pip install vituralenv </p> <p> cd into directory you want to create project </p><p> to create virtualenv type virtualenv *name* </p><p> to activate virtualenv type source *name*/bin/activate </p><p> pip install flask </p><p> pip install gunicorn - better webserver </p><p> create Procfile  - web: gunicorn helloflask:app </p><p> git add ., git commit, git push heroku master </p><p> pip freeze > requirements.txt </p>"

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

# app.run(debug=True)