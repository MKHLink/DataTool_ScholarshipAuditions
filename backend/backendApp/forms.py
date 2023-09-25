from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

class FacultyForm(FlaskForm):
    # schoolName, schoolDepartment, firstName, lastName, title, disipline, email, city, state, schoolUrl
    schoolName = StringField("School Name", validators=[DataRequired()])
    schoolDepartment = StringField("School Department", validators=[DataRequired()])
    firstName = StringField("First Name", validators=[DataRequired()])
    lastName = StringField("Last Name", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    disipline = StringField("Disipline", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    state = StringField("State", validators=[DataRequired()])
    schoolUrl = StringField("School URL", validators=[DataRequired()])

    submit = SubmitField("Submit")
    
    