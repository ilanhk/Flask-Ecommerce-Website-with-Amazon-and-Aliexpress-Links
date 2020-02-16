from app import app, db
from app.models import Products, Categories, Subcategories, Imagesandvideos
from flask import redirect, render_template, flash, url_for
from app.forms import Loginform, AddCustomer, AddProductForm

# flash is for flash messages

@app.route('/')
def index():
    return render_template('index.html', )

@app.route('/allproductspage')
def all_products():
    categories = Categories.query.all()
    subcategories= Subcategories.query.all()
    products = Products.query.all()

    return render_template('allproductspage.html', products=products, categories=categories, subcategories=subcategories)

# @app.route('/<str:cat_id>')
# def product_details(cat_di):
#     categories = Categories.query.filter_by(product_id=prod_id).first()
#     subcategories = Subcategories.query.all()
#     products = Products.query.all()

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

    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        flash(f'Welcome {form.username.data}!', 'success')
        return redirect(url_for('all_products'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



# Search Bar Section

@app.route('/search', methods=['GET','POST'])
def search():
    if method != 'POST':
        return render_template(request, 'search.html')
    text = request.POST.get('search', '')

    categories_list = Categories.query.filter(Categories.category_name.like(text)).all()

    subcategories_list = Subcategories.query.filter(Subcategories.subcategory_name.like(text)).all()

    products_list = Products.query.filter(Products.product_name.like(text)).all()

    # Post.query.filter(Post.title.ilike('%some_phrase%'))

    # tag = request.form["tag"]
    # search = "%{}%".format(tag)
    # posts = Post.query.filter(Post.tags.like(search)).all()

    print(f'this is a list of cat: {categories_list}')
    print(f'this is a list of subcat: {subcategories_list}')
    print(f'this is a list of products: {products_list}')

    
    return render_template('search.html', categories_list, subcategories_list, products_list)
