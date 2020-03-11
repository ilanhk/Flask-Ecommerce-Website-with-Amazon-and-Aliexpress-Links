from app import db

# Users Section:

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
      return f'<User: {self.first_name} {self.last_name} with Username: {self.username} >'


class Categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(64))
    subcategories= db.relationship('Subcategories', backref='categories', lazy='dynamic')
    products = db.relationship('Products', backref='categories', lazy='dynamic')

    def __repr__(self):
      return f'<Categories: {self.category_name}>'

class Subcategories(db.Model):
    subcategory_id = db.Column(db.Integer, primary_key=True)
    subcategory_name = db.Column(db.String(64))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    products = db.relationship('Products', backref='subcategories', lazy='dynamic')

    def __repr__(self):
        return f'<Subcategories: {self.subcategory_name}>'

class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategories.subcategory_id'))
    short_product_description = db.Column(db.String(200))
    product_description = db.Column(db.String(2000))
    product_dimensions = db.Column(db.String(100))
    power_wattage = db.Column(db.String(100))
    product_color = db.Column(db.String(100))
    price_USD = db.Column(db.Float)
    amazon_link = db.Column(db.String(2000))
    aliexpress_link = db.Column(db.String(2000))
    imagesandvideos = db.relationship('Imagesandvideos', backref='products', lazy='dynamic')



    def __repr__(self):
        return f"<Products: {self.product_name}>"


class Imagesandvideos(db.Model):
    imgandvid_id = db.Column(db.Integer, primary_key=True)
    imgOrvid_link = db.Column(db.String(400))
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id', related_name='imv'))

    def __repr__(self):
        return f"<Imagesandvideos:{self.imgOrvid_link}>"

    def __str__(self):   ##Omer put this to show links in string format bc html shows in s
        return self.imgOrvid_link








