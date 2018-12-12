from flask_wtf import FlaskForm as Form
from wtforms import TextField, validators, StringField,\
SubmitField, SelectField, IntegerField

class QueryForm(Form):
    year = SelectField(u'Release year',\
               choices=[('2010', '2010'), ('2011', '2011'), ('2012', '2012'), \
                        ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), \
                        ('2016', '2016'), ('2017', '2017'), ('2018', '2018')])
    genre = SelectField(u'Genre',\
               choices=[('none', 'Choose one'), ('adventure', 'Adventure'), \
               ('sport', 'Sport'), ('musical', 'Musical'), ('documentary', 'Documentary'), \
               ('fantasy', 'Fantasy'), ('family', 'Family'), ('crime', 'Crime'), \
               ('sci-fi', 'Sci-Fi'), ('drama', 'Drama'), ('thriller', 'Thriller'), \
               ('comedy', 'Comedy'), ('romance', 'Romance'), ('biography', 'Biography'), \
               ('western', 'Western'), ('animation', 'Animation'), ('war', 'War'), \
               ('mystery', 'Mystery'), ('action', 'Action'), ('history', 'History'), ('music', 'Music'), \
               ('horror', 'Horror')])
