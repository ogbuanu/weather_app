from wtforms import  StringField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length
# from wtforms.fields import 

from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    location = StringField(validators=[DataRequired(),Length(min=3,max=15)])
    submit = SubmitField('search')