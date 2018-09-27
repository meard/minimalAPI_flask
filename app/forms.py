from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, InputRequired

class searchForm(FlaskForm):

    firstName = StringField('First Name', [InputRequired(), Length(min=3, max=50)])
    middleName = StringField('Middle Name')
    lastName = StringField('Last Name')
    submit = SubmitField('Submit Query')
    