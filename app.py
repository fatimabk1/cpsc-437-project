import os

from flask import Flask, session, render_template, flash, request, redirect,\
	url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import QueryForm

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
db = SQLAlchemy(app)

# Movie, Genre, Person, Appearance, Direction
from models import *

# Bootstrap setup
bootstrap = Bootstrap(app)

# Homepage (form)
@app.route("/", methods=['GET'])
def index():
    form = QueryForm(request.form)
    return render_template('index.html', form=form)

@app.route("/search", methods=["GET"])
def search():
    """
    Endpoint for searchbox to query to get search suggestions.
    """
    if not request.args.get("q"):
        raise RuntimeError("missing search query")

    result = Person.query.filter(Person.name.ilike("%" + request.args.get("q")
	    + "%")).all()
    json = []
    for person in result:
        json.append({"name": person.name})
    return jsonify(json)

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

    if start_year:
	# Since these values are required, I guess we don't really need this check?
        movies_in_year_range = Movie.query.filter(
		Movie.release_year >= start_year,
		Movie.release_year <= end_year).order_by(Movie.release_year)
        results = set(movies_in_year_range)
    if director:
        movies_with_director = Movie.query.join(Direction,
                Movie.id == Direction.movie_id).join(Person,
                Direction.director_id == Person.id).filter(
                        Person.name == director)
        results &= set(movies_with_director)
    if actor:
        movies_with_actor = Movie.query.join(Appearance,
		        Movie.id == Appearance.movie_id).join(Person,
			        Appearance.actor_id == Person.id).filter(
				            Person.name == actor)
        results &= set(movies_with_actor)

    if genres:
        movies_of_genre = Movie.query.join(Genre,
                Movie.id == Genre.movie_id).filter(Genre.genre.in_(genres))
        results &= set(movies_of_genre)


    # Render result in order of release year, alphabetical order within a year
    sorted_results = sorted(list(results),
	    key=lambda movie: (movie.release_year, movie.name))
    return render_template("result.html",
	   message=f"",
	   movies=enumerate(sorted_results, 1))

# Run Flask
if __name__ == '__main__':
    app.run()