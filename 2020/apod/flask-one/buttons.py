from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email, DataRequired

class emailButton(FlaskForm):
    email = StringField('Enter email', validators=[DataRequired(), Email()])
    submit = SubmitField('and send email')
