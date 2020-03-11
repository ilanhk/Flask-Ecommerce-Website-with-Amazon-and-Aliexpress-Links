from app import app, db
from app.models import Products, Categories, Subcategories, Imagesandvideos
from flask import redirect, render_template, flash, url_for, request
from app.forms import Loginform, AddCustomer, AddProductForm
from app.models import Categories, Subcategories, Products


# flash is for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/About_Us')
def about():
    return render_template('about.html', )


@app.route('/allproductspage')
def all_products():
    categories = Categories.query.all()
    subcategories= Subcategories.query.all()
    products = Products.query.all()

    return render_template('allproductspage.html', products=products, categories=categories, subcategories=subcategories)


@app.route('/Category/<int:cat_id>')
def category(cat_id):
    categories = Categories.query.filter_by(category_id=cat_id).first()
    print(f'this is the {categories}')
    subcategories= Subcategories.query.filter_by(category_id=cat_id).all()
    products = Products.query.filter_by(category_id=cat_id).all()

    return render_template('allproductspage.html', products=products, categories=categories, subcategories=subcategories)



@app.route('/productdetails/<int:prod_id>')
def product_details(prod_id):
    product = Products.query.filter_by(product_id=prod_id).first()
    imgvids = Imagesandvideos.query.filter_by(product_id=prod_id).all()
    countimgvids=Imagesandvideos.query.filter_by(product_id=prod_id).count()

    return render_template('productdetailspage.html', product=product, imgvids=imgvids, countimgvids=countimgvids)


#Forms Section:

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = AddCustomer()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('all_products'))
    elif None:
        return redirect(url_for('register'))
    else:
        flash(f'Account NOT Created for {form.username.data}!', 'danger')
    # not validating add errors section 

    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        flash(f'Welcome {form.username.data}!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



# Search Bar Section

@app.route('/search', methods=['GET','POST'])
def search():
    text = request.form['searchbar']

    categories = Categories.query.filter(Categories.category_name.ilike(text)).all()

    subcategories = Subcategories.query.filter(Subcategories.subcategory_name.ilike(text)).all()

    products = Products.query.filter(Products.product_name.ilike(text)).all()

    # Post.query.filter(Post.title.ilike('%some_phrase%'))

    # tag = request.form["tag"]
    # search = "%{}%".format(tag)
    # posts = Post.query.filter(Post.tags.like(search)).all()


    return render_template('search.html', products=products, categories=categories, subcategories=subcategories)
