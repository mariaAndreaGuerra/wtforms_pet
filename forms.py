from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import InputRequired, URL, AnyOf, NumberRange
from wtforms import Form, validators

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message='Invalid species')])
    photo_url = StringField('Photo URL', validators=[URL(require_tld=False, message='Invalid URL')])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30, message='Age should be between 0 and 30')])
    notes = TextAreaField('Notes')
    available = BooleanField('Available')

class EditPetForm(Form):
    photo_url = StringField('Photo URL', validators=[URL(require_tld=False, message='Invalid URL')])
    notes = TextAreaField('Notes')
    available = BooleanField('Available')
