import psycopg2
conn = psycopg2.connect("host=localhost dbname=wimpdb user=postgres")
cur = conn.cursor()


create tables
cur.execute("""
CREATE TABLE directed(
    dir_id INT,
    movie_id INT,
    CONSTRAINT pk_director PRIMARY KEY(dir_id, movie_id)
);
CREATE TABLE movie(
    id INT,
    name VARCHAR(100),
    release_year INT,
    CONSTRAINT pk_movie PRIMARY KEY(id)
);
CREATE TABLE people(
    id INT,
    name VARCHAR(40),
    death_year INT,
    birth_year INT,
    CONSTRAINT pk_person PRIMARY KEY(id)
);
CREATE TABLE genre(
    movie_id INT,
    genre VARCHAR(40),
    CONSTRAINT pk_genre PRIMARY KEY(movie_id, genre)
);
CREATE TABLE appeared(
    actor_id INT,
    movie_id INT,
    CONSTRAINT pk_appeared PRIMARY KEY(actor_id, movie_id)
);
""")
conn.commit()

with open('data/appeared.tsv', 'r') as f:
    # Notice that we don't need the `csv` module.
    cur.copy_from(f, 'appeared', sep='\t')
conn.commit()
f.close()

with open('data/directed.tsv', 'r') as f:
    # Notice that we don't need the `csv` module.
    cur.copy_from(f, 'directed', sep='\t')
conn.commit()
f.close()

with open('data/movies.tsv', 'r') as f:
    # Notice that we don't need the `csv` module.
    cur.copy_from(f, 'movie', sep='\t')
conn.commit()

f.close()

with open('data/genres.tsv', 'r') as f:
    # Notice that we don't need the `csv` module.
    cur.copy_from(f, 'genre', sep='\t')
conn.commit()

f.close()

with open('data/people.tsv', 'r') as f:
    # Notice that we don't need the `csv` module.
    cur.copy_from(f, 'people', sep='\t')
conn.commit()

f.close()