from server.py import conn, cur

# all movies from a given release_year (id, name, year)
def moviesByYear(yr):
    cur.execute("""
    SELECT *
    FROM movies
    WHERE release_year=(?)
    """, (yr))
    movieList = cur.fetchall()
    return movieList

# genre count breakdown for a movie list (genre, count)
def genreCount(yr):
    cur.execute("""
    SELECT genre, COUNT(genre)
    FROM movies
    JOIN genre
    ON movies.id=genre.movie_id
    WHERE release_year=(?)
    GROUP BY genre;
    """, (yr))
    genreNumbers = cur.fetchall()
    return genreNumbers
