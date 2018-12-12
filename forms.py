from flask_wtf import FlaskForm as Form
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms import TextField, validators, StringField, SubmitField, \
SelectField, IntegerField, SelectMultipleField
from wtforms.validators import Required

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class QueryForm(Form):
    start_year = SelectField(u'Start year',\
               choices=[('2010', '2010'), ('2011', '2011'), ('2012', '2012'), \
                        ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), \
                        ('2016', '2016'), ('2017', '2017'), ('2018', '2018')])
    end_year = SelectField(u'End year',\
               choices=[('2010', '2010'), ('2011', '2011'), ('2012', '2012'), \
                        ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), \
                        ('2016', '2016'), ('2017', '2017'), ('2018', '2018')])
    director = TextField('Director Name:')
    actor = TextField('Actor Name:')
    genres = MultiCheckboxField('Genres',
           choices=[('adventure', 'Adventure'), \
           ('sport', 'Sport'), ('musical', 'Musical'), ('documentary', 'Documentary'), \
           ('fantasy', 'Fantasy'), ('family', 'Family'), ('crime', 'Crime'), \
           ('sci-fi', 'Sci-Fi'), ('drama', 'Drama'), ('thriller', 'Thriller'), \
           ('comedy', 'Comedy'), ('romance', 'Romance'), ('biography', 'Biography'), \
           ('western', 'Western'), ('animation', 'Animation'), ('war', 'War'), \
           ('mystery', 'Mystery'), ('action', 'Action'), ('history', 'History'), ('music', 'Music'), \
           ('horror', 'Horror')], coerce=str)

