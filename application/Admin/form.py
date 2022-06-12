from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,TextAreaField,FileField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from flask_login import current_user

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5,max=30)])
    
    submit = SubmitField('Login')



class AddUserForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5,max=30)])
    name = StringField('Name',validators=[DataRequired()])
    code = StringField('Code',validators=[DataRequired()])
    account = StringField('Account',validators=[DataRequired()])
    routing = StringField('Routing',validators=[DataRequired()])
    address = StringField('Address',validators=[DataRequired()])
    product_name = StringField('Product Name',validators=[DataRequired()])
    phone_no = StringField('Phone Number',validators=[DataRequired()])
    
    submit = SubmitField('Add')


class EditUserForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5,max=30)])
    name = StringField('Name',validators=[DataRequired()])
    code = StringField('Code',validators=[DataRequired()])
    account = StringField('Account',validators=[DataRequired()])
    routing = StringField('Routing',validators=[DataRequired()])
    address = StringField('Address',validators=[DataRequired()])
    product_name = StringField('Product Name',validators=[DataRequired()])
    phone_no = StringField('Phone Number',validators=[DataRequired()])
    
    submit = SubmitField('Update')