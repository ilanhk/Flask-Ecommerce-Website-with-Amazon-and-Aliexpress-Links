from app import app, db
from app.models import Products, Categories, Subcategories, Imagesandvideos
from flask import redirect, render_template


@app.route('/')
def index():
    categories = Categories.query.all()
    subcategories= Subcategories.query.all()
    products = Products.query.all()


    # do logic here
    return render_template('allproductspage.html', products=products, categories=categories, subcategories=subcategories)


@app.route('/productdetails/<int:prod_id>')
def product_details(prod_id):
    product = Products.query.filter_by(product_id=prod_id).first()
    imgvids = Imagesandvideos.query.filter_by(product_id=prod_id).all()
    countimgvids=Imagesandvideos.query.filter_by(product_id=prod_id).count()

    return render_template('productdetailspage.html', product=product, imgvids=imgvids, countimgvids=countimgvids)

#
# @app.route('/add', methods=['GET', 'POST']) #get, post gets info from the client in the browser to send to database
# def addbook():
#     form = AddForm()
#
#     if form.validate_on_submit():  #if statement bc change of book table column from author to author_id to show example of relationships
#         title = form.title.data  #form.title.data - gets title info from the form
#         author_name = form.author.data
#         price = form.price.data
#
#         if author_name.lower() not in [aut.name.lower() for aut in Author.query.all()]: # all objects/instances of Author that has been added to the database
#             author = Author(name=author_name)
#             db.session.add(author)
#         else:
#             author = Author.query.filter_by(name=author_name).first() #get the first match
#
#         newbook = Book(title=title, author=author, price=price)
#         db.session.add(newbook)
#         db.session.commit()
#         return redirect('/')   #redirect is from flask to redirect in what view/html you want. In This case  once new object (a book) has been added it would redirect to ('/') which would add the title and author of all books from the database.
#     return render_template('addbook.html', form=form)

