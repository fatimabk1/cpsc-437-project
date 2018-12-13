import os

from flask import Flask, session, render_template, flash, request, redirect,\
        url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine
from forms import QueryForm
import psycopg2
import subprocess
import json


# Flask setup
app = Flask(__name__)

# Database for SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# API Key for WTForm
# TODO: ideally should take this out for prod
app.config["SECRET_KEY"] = "7d4e41f27d441f27567d441f2b6176a"

# Turn debug mode on, for development purposes (TODO: can take out in prod!)
app.debug = True

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# Database object
proc = subprocess.Popen('heroku config:get DATABASE_URL -a wimpdb', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'

engine = create_engine(db_url)
cur = engine.connect()

def moviesByYear(yr):
    movieList = cur.execute("""SELECT * FROM movies WHERE release_year=%s""", yr)
    result = []
    for row in movieList:
        result.append(row)
    return result

# Bootstrap setup
bootstrap = Bootstrap(app)

# Homepage (form)
@app.route("/", methods=['GET'])
def index():
	form = QueryForm(request.form)
	return render_template('index.html', form=form)

# Form submission
@app.route("/submit", methods=["POST"])
def process_form():
    form = QueryForm(request.form)
    start_year = request.form["start_year"]
    end_year = request.form["end_year"]
    director = request.form["director"]
    actor = request.form["actor"]
    genres = form.genres.data

    # MVP of database operations
    # TODO: we should do the set operations in the DB queries, not Python!
    results = set()
    movie_genres = None

    if start_year:
        # Since these values are required, I guess we don't really need this check?
        results = moviesByYear(start_year)
        
    # Render result in order of release year, alphabetical order within a year
    sorted_results = sorted(results,
            key=lambda movie: (movie[1], movie[2]))
    return render_template("result.html",
           # message=f"",
           movies=enumerate(sorted_results, 1))

# Run Flask
if __name__ == '__main__':
    app.run()