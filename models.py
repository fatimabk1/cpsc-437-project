from app import db

class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    release_year = db.Column(db.Integer)

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f"<Movie {self.name} ({self.release_year})>"

class Person(db.Model):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Person {self.name}>"

class Appearance(db.Model):
    __tablename__ = "appeared"

    actor_id = db.Column(db.Integer, db.ForeignKey("people.id"),
            primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"),
            primary_key=True)

    def __repr__(self):
        return f"<Appearance {self.actor_id} appeared in {self.movie_id}>"

class Direction(db.Model):
    __tablename__ = "directed"

    director_id = db.Column(db.Integer, db.ForeignKey("people.id"), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"),
            primary_key=True)

    def __repr__(self):
        return f"<Direction {self.director_id} directed {self.movie_id}>"

class Genre(db.Model):
    __tablename__ = "genres"

    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"),
            primary_key=True)
    genre = db.Column(db.Text, primary_key=True)

    movie = db.relationship("Movie")

    def __repr__(self):
        return f"<Genre {self.movie_id}, {self.genre}>"
