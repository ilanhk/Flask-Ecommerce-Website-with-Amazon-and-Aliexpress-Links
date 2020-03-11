from app import db
from app.models import Products, Imagesandvideos, Categories, Subcategories
import requests
import random

from bs4 import BeautifulSoup
# need to pip install requests and beautifulsoup4


source = requests.get('http://aicok.cc/list/coffer-grinder#Coffee_Grinders').text

# .text will give you the text of a tag/div/etc

soup = BeautifulSoup(source, 'lxml')
#lxml is a parser i had to install (recommended). Need a parser to parse the html. html5lib is popular as well.

# use inspect element to find the thing you want to take

mydivs = soup.findAll("div", {"class": "detail-shop-box"})
# can also be class_=''


# MAKE LIST OF SUBCATEGORIES SECTION AND ADD THEM:
numbers_not_to_add = [1, 8, 24, 27, 31]
list_of_newsubcats_toadd = []
list_of_subcat_ids = soup.findAll("div", {"class": "c-row clearfix"})

for i in range(len(list_of_subcat_ids)):
    # print(f'{i}. '+ list_of_subcat_ids[i]['id']) # to get the id of name of a subcategory
    subcat_name = list_of_subcat_ids[i]['id']
    subcat_name_with_spaces = subcat_name.replace("_", " ")

    # ADD NEW SUBCATEGORY TO DB IF DOESNT EXIST:
    if i in numbers_not_to_add:
        continue

    elif i == 2 or i == 29:
        sub = Subcategories(subcategory_name=f'{subcat_name_with_spaces}', category_id=3)



    elif i == 25 or i == 26:
        sub = Subcategories(subcategory_name=f'{subcat_name_with_spaces}', category_id=2)


    else:
        sub = Subcategories(subcategory_name=f'{subcat_name_with_spaces}', category_id=1)



    # db.session.add(sub)
    # db.session.commit()

# TO GET ALL PRODUCTS OF A SUBCATEGORY:
#
# for i in range(len(list_of_subcat_ids)):
#     subcat_name = list_of_subcat_ids[i]['id']
#     subcat_name_with_spaces = subcat_name.replace("_", " ")


for subcat in list_of_subcat_ids:

    subcat_cont = soup.find("div", {"id": f"{subcat['id']}"})
    # print(subcat_cont.prettify())
    subcat_cont_with_spaces = subcat['id'].replace("_", " ")
    shopboxlist= subcat_cont.findAll("div", {"class": "detail-shop-box"})

    for box in shopboxlist:
        # print(box.prettify())

# in order to get an href from an a tag:
        product_href=shopboxlist[0].find('a', href=True)['href']

#How to Scrape a new page (SOUP WITHIN A SOUP):
        product_details_url = requests.get(f'http://aicok.cc/{product_href}').text

# product_detail_page = requests.get("http://aicok.cc/products/aicok-electric-kettle,-adjustable-temperature-stainless-steel-bpa-free-kettle,-with-led-lighting-and-thermometer,-professional-strix-cordless-control-thermostat-electric-kettle-1-5-l").text

        sup = BeautifulSoup(product_details_url, 'lxml')

# print(sup.prettify())

# PRODUCT PARAGRAPH SECTION:
# span class: a-list-item for bullet point description
        list_of_bulletpoints = sup.findAll("span", {"class": "a-list-item"})

# print(list_of_bulletpoints[0].text) #to get one bullet point paragraph

        def bullet_paragraph_maker(list):
            block = ''
            for bullet in list:
                block =f'{bullet.text}/{block}'
            return block
            # print(block.split('/')) # to make to a list of sentences by cutting out  '/'.

        # bullet_paragraph_maker(list_of_bulletpoints) #to get all bullet points in one paragraph to add to data base
# need to make a function in view to separate and make bullet points


# Short Product Description:
        product_decription_short = sup.find("h1", {"class": "uk-text-xlarge"}).text


# Product Specifications SECTION:
        product_specs = sup.find_all("span", {"class": "meta-cont"})

# 0 -model#, 1-material type, 2- color, 3- dimensions, 4- weight, 5- power wattage
        def product_spec_present(n):
            try:
                product_specs[n].text
                product_spec = product_specs[n].text
                return product_spec

            except:
                return None


# print(product_specs[1].text)

# US AMAZON Link SECTION:
        list_of_links = sup.findAll("div", {"class": "item"})
        us_amazon_link = list_of_links[244]['data-value']

# print(list_of_links[244]['data-value']) #link to US amazon

        # TO GET CATEGORY ID AND SUBCATEGORY ID OF EACH PRODUCT
        if Subcategories.query.filter_by(subcategory_name=subcat_cont_with_spaces).first().subcategory_id != None:

            subcat_id = Subcategories.query.filter_by(subcategory_name=subcat_cont_with_spaces).first().subcategory_id
            cat_id = Subcategories.query.filter_by(subcategory_name=subcat_cont_with_spaces).first().category_id

        else:
            subcat_id =1
            cat_id = 1

#1 Make Product Objects :

        prod = Products(
        product_name=f'{product_specs[0].text}',
        category_id= cat_id,
        subcategory_id=subcat_id,
        short_product_description= f'{product_decription_short}',
        product_description=f'{bullet_paragraph_maker(list_of_bulletpoints)}',
        product_dimensions=f'{product_spec_present(3)}',
        power_wattage=f'{product_spec_present(5)}',
        product_color=f'{product_spec_present(2)}',
        price_USD= random.uniform(10, 50),
        amazon_link= f'{us_amazon_link}',
        aliexpress_link='https://www.aliexpress.com/item/32920568211.html?spm=a2g0o.productlist.0.0.6fc4ce64FQjDmc&algo_pvid=8b5beb74-4fdb-4725-ac26-c429359d808e&algo_expid=8b5beb74-4fdb-4725-ac26-c429359d808e-4&btsid=0ab6fa8115830593653781513e5f76&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_'
        )

        # db.session.add(prod)
        # db.session.commit()

#2 Make Photo Objects:

    sop = BeautifulSoup(us_amazon_link, 'lxml')
# Gsteamer1 =Imagesandvideos(imgOrvid_link= 'Gsteamer1.png', product_id= 9)







#if in coffee div scrap all products :
#       to each product detail page and scrap
#       add new product object
#       then go to amazon site scrap images
#       add new images of each product.


# Additional Beautifulsoup tips:

# .prettify() makes the code readable

# soup.div and soup.find('div') would give you first div tag on the page