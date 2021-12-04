from wtforms import BooleanField, StringField, FloatField, SubmitField, IntegerField, validators
from flask_wtf import FlaskForm

class AddMessageForm(FlaskForm):
	content = StringField('Texte', [validators.InputRequired()])
	add = SubmitField('Ajouter')
