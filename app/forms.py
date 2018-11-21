# forms
from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class ALLForm(Form):
    Description = StringField('Description', validators=[DataRequired()])
    Status = SelectField('Status', choices=[('C', 'C'), ('U', 'U')])
    Deadline = DateField('Deadline', validators=[DataRequired()])
