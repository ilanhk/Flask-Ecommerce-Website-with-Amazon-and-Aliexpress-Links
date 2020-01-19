from flask_wtf import FlaskForm
from wtforms.validators import data_required
from wtforms import StringField, SubmitField, FloatField


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
    last_name = StringField('Last Name', validators=[data_required()])
    first_name = StringField('First Name', validators=[data_required()])
    email= StringField('Email Address', validators=[data_required()])
    password = StringField('Password', validators=[data_required()])
    submit = SubmitField('Submit')
