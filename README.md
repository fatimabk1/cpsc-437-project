# wimpdb
("Worse Internet Movie [Project] Database")
For Yale's CPSC 437: Database Systems.

## Authors
* Fatima Kahbi '19
* Sanya Nijhawan '20
* Sean Walker '19

## Technologies
* Database: PostgreSQL
* Frontend: Bootstrap, Jinja
* Backend: Python (Flask)
* Hosted on Heroku

## Data
[From IMDB](https://www.imdb.com/interfaces/)

Only including movies since 2010, due to Heroku DB size constraints.

See the `util/` directory for scripts we wrote to transform data from the format it is in the IMDB files into the format we used for our database. In particular, we excluded all films made before 2010 (and, of course, all actors & directors who don't appear/direct any films 2010 and after) and re-did the id system for people and movies s.t. each are merely id'd by the natural numbers (a different set, i.e. there's movie id 1, 2, 3, ... and person id 1, 2, 3, ...).

## Schema
MOVIES(__id__, name, release\_year)

GENRES(__movie\_id__, __genre__)

PEOPLE(__id__, name, birth\_year, death\_year)

APPEARED(__actor\_id__, **movie\_id**)

DIRECTED(__director\_id__, **movie\_id**)

