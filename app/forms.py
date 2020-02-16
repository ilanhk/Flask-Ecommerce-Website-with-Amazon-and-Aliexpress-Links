from flask_wtf import FlaskForm
from wtforms.validators import data_required, Length, Email, EqualTo
from wtforms import StringField, SubmitField, FloatField, PasswordField, BooleanField
# importing email will check if its a valid email address, Equalto to make sure the input is the same value as the other input
# Booleanfield is to see if its true/false useful to remember current users

class AddProductForm(FlaskForm):

    product_name =StringField('Product Name', validators=[data_required()])
    category_name =StringField('Category Name', validators=[data_required()])
    subcategory_id =StringField('Subcategory Name', validators=[data_required()])
    short_product_description = StringField('Short Product Desciption', validators=[data_required()]) #possible to get big textbox
    product_description = StringField('Product Description', validators=[data_required()])
    product_dimensions = StringField('Product Dimensions', validators=[data_required()])
    power_wattage = StringField('Wattage', validators=[data_required()])
    product_color = StringField('Product Color', validators=[data_required()])
    price_USD = FloatField('Price(USD)', default=0)
    amazon_link = StringField('Amazon Link', validators=[data_required()])
    aliexpress_link =StringField('Aliexpress Link', validators=[data_required()])
    # add photos and videos ?????????????????????????????????
    submit = SubmitField('Add a New Product')

class AddCustomer(FlaskForm):
    username = StringField('Username: ', validators=[data_required(), Length(min=2, max=20)])
    last_name = StringField('Last Name: ', validators=[data_required(), Length(min=2, max=20)])
    first_name = StringField('First Name: ', validators=[data_required(), Length(min=2, max=20)])
    email= StringField('Email Address: ', validators=[data_required(), Email()])
    password = PasswordField('Password: ', validators=[data_required()])
    confirm_password = PasswordField('Confirm Password: ', validators=[data_required(), EqualTo(password)])
    submit = SubmitField('Signup')


class Loginform(FlaskForm):
    email = StringField('Email Address: ', validators=[data_required(), Email()])
    password = PasswordField('Password: ', validators=[data_required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


# for Search Bar:

class SearchForm(FlaskForm):
  search = StringField('search', [data_required()])
  submit = SubmitField('Search')




