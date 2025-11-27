from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters."),
        Regexp(r'.*[A-Z].*', message="Password must contain at least one uppercase letter."),
        Regexp(r'.*[a-z].*', message="Password must contain at least one lowercase letter."),
        Regexp(r'.*\d.*', message="Password must contain at least one digit."),
        Regexp(r'.*[^A-Za-z0-9].*', message="Password must contain at least one special character.")
    ])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
