from flask import Flask, session, render_template, flash, request, redirect,\
url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import QueryForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/wimpdb'
app.config['SECRET_KEY'] = '7d4e41f27d441f27567d441f2b6176a'
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def index():
	form = QueryForm(request.form)
	print('here')
	if request.method=='POST':
		year = request.form['year']
		genre=request.form['genre']
		print(genre)
		if form.validate():
			flash(str(year) + " " + str(genre))
			return redirect(url_for('index'))
		else:
			flash("All the form fields are required")
	print('about to render')
	return render_template('index.html', form=form)

@app.route("/name/<name>")
def get_movie_name(name):
    return "name : {}".format(name)

if __name__ == '__main__':
    app.debug = True
    app.run()

