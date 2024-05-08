from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class MembershipForm(FlaskForm):
    duration_months = SelectField('Duration', choices=[(6, '6 Months'), (12, '1 Year'), (24, '2 Years')], coerce=int, default=6, validators=[DataRequired()])
    submit = SubmitField('Submit')
