
from app import db
from app.models import Products, Imagesandvideos, Categories, Subcategories
import requests




# create instances for categories:
Kitchen_Appliances = Categories(category_name= 'Kitchen Appliances')
Household_and_Home_Appliances = Categories(category_name = 'Household and Home Appliances')
Cookware = Categories(category_name = 'Cookware')
Sports_Equipment = Categories(category_name = 'Sports Equipment')
Consumer_Electronics = Categories(category_name = 'Consumer Electronics')
Beauty_and_Cosmetics = Categories(category_name = 'Beauty and Cosmetics')

# #adding b to the database
# list_of_cat = []
#
# for cat in list_of_cat:
#     db.session.add(cat)

# #create instances for subcategories:
# Air_Fryers = Subcategories(subcategory_name= 'Air Fryers', category_id= 1)
# Coffee_Makers = Subcategories(subcategory_name= 'Coffee Makers', category_id= 1)
# Kitchen_Knives = Subcategories(subcategory_name= 'Kitchen Knives', category_id= 3)
# Oven_Gloves =Subcategories(subcategory_name= 'Oven_Gloves', category_id= 3)
# Speakers =Subcategories(subcategory_name= 'Speakers', category_id= 5)
# Yoga_mat =Subcategories(subcategory_name= 'Yoga_Mats', category_id= 4)
# Makeup_Mirrors =Subcategories(subcategory_name= 'Makeup_Mirrors', category_id= 6)
# Robot_Vacuums =Subcategories(subcategory_name= 'Robot_Vacuums', category_id= 2)
# Mops =Subcategories(subcategory_name= 'Mops', category_id= 2)
# Garment_Steamers=Subcategories(subcategory_name= 'Garment Steamers', category_id= 2)
#
# # adding subcat to the database
# list_of_subcat = []
#
# for sub in list_of_subcat:
#      db.session.add(sub)

 # create instances for products:
nespresso = Products(
product_name= 'Nespresso Machine',
category_id= 1,
subcategory_id=2,
short_product_description='Nespresso Machine by Aicok, 24 OZ, 1255W',
product_description='ONE-TOUCH PROGRAMMABLE BUTTON - Aicok Nespresso Machine has one-touch buttons with two cup capacities (Espresso and Lungo) can be programmed to custom volumes and are backlit for ease of use, blue light flashing means preheating, blue light stable means ready, yellow light flashing means empty water tank alert.',
product_dimensions='31.5 x 12.5 x 22.5 cm',
power_wattage='1255W',
product_color='Black&Red',
price_USD= 30.45,
amazon_link='https://www.amazon.fr/dp/B07PYZK9VB',
aliexpress_link='https://www.aliexpress.com/item/4000281485763.html?spm=a2g0o.productlist.0.0.55d82b17mbKWFd&s=p&algo_pvid=b6ea2417-60e1-4ca0-bea0-2ea89e54770a&algo_expid=b6ea2417-60e1-4ca0-bea0-2ea89e54770a-3&btsid=11b6052a-05fd-4faa-a650-edc56ecce60b&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_53'
)

knivesset= Products(
product_name='6-Piece Kitchen Knife Block Set',
category_id= 3, subcategory_id=3,
short_product_description='6-Piece Kitchen Knife Block Set',
product_description='GERMAN STAINLESS STEEL: The knives are made of high carbon content, 420-grade stainless steel. 6 PIECE KNIFE SET: 8” Chef Knife, 8” Carving Knife, 8” Bread Knife, 5” Utility Knife, 3.5” Paring Knife and a Wooden Knife Block.',
product_dimensions='8.7 x 5.5 x 14.2 inches',
power_wattage= None,
product_color='Black&Steel',
price_USD= 22.94,
amazon_link='https://www.amazon.com/dp/B07JNNZ88Z',
aliexpress_link='https://www.aliexpress.com/item/32949717464.html?spm=a2g0o.productlist.0.0.b0ad26eedkMYHP&algo_pvid=32a9645b-082c-48f0-bd1e-ac0f46d93e2f&algo_expid=32a9645b-082c-48f0-bd1e-ac0f46d93e2f-27&btsid=2e0dbeef-ff40-4130-8211-403314a04420&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_53'
)

digairfryer = Products(
product_name= '5L Digital Air fryer',
category_id= 1,
subcategory_id= 1,
short_product_description= '5L Digital Air fryer',
product_description='SIMPLE TO USE: Touchscreen combines with the smart timer buttons to make cooking a breeze, and the memory function will remember the settings for your favorite dishes. GUILT FREE FRYER: Cut back on the calories by up to 80% compared to traditional deep fryers and enjoy a more balanced diet.',
product_dimensions= '9.1 x 12.2 x 12.6 inches',
power_wattage= '1400W',
product_color='Black',
price_USD= 33.45,
amazon_link= 'https://www.amazon.com/Aicok-Temperature-Circulation-Technology-Low-Fat-Cooker/dp/B073DZTBM2',
aliexpress_link='https://www.aliexpress.com/item/4000262733211.html?spm=a2g0o.productlist.0.0.206b19f5PaNKZN&algo_pvid=a75d79cc-4560-42f1-8e9b-686b29b0c684&algo_expid=a75d79cc-4560-42f1-8e9b-686b29b0c684-27&btsid=ae57355f-2b08-4cfd-a92f-f4bad608db5f&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_53'
)

ovengloves = Products(
product_name= 'Red Oven Gloves',
category_id= 3,
subcategory_id= 4,
short_product_description= 'Heat Resistance Red Gloves',
product_description= 'HEAT RESISTANT: The gloves protect your arms and forearms from hot dishes, pots and oven racks for up to 240°C (464°F). COTTON QUILTED LINING: The gloves provide a flexible and comfortable grip on your hot dishes, oven racks and pots.',
product_dimensions= '11.5 x 7.7 x 2.3 inches',
power_wattage= None,
product_color= 'Red',
price_USD= 10.77,
amazon_link= 'https://www.amazon.com/dp/B07FFTT9HY',
aliexpress_link='https://www.aliexpress.com/item/4000083798885.html?spm=a2g0o.productlist.0.0.6f1179dc91MRoi&algo_pvid=40124213-66e7-4bb3-ae71-29c7fbf1e9c7&algo_expid=40124213-66e7-4bb3-ae71-29c7fbf1e9c7-5&btsid=1d056565-e7c4-453f-a00e-2ac35b11ff0c&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_53'
)

fivecupcoffeemachine = Products(
product_name= '5 Cup Coffee maker',
category_id= 1,
subcategory_id= 2,
short_product_description= '5-Cup Drip Coffee Maker for 5 books of Moses',
product_description= 'Lighted I/O Switch - Just one simple button, press power switch to I" position to start and press switch to "O" to stop the coffee maker, brews   a full pot of coffee very soon, boil dry protection prevent continuous brewing.',
product_dimensions= '11.1 x 8.1 x 6.4 inches',
power_wattage= '600W',
product_color= 'Black',
price_USD= 20.34,
amazon_link= 'https://www.amazon.com/Aicok-Coffeemaker-Automatic-Anti-Drip-Technology/dp/B074P4262D',
aliexpress_link='https://www.aliexpress.com/item/4000134289485.html?spm=a2g0o.productlist.0.0.526137f5t9lXwq&algo_pvid=56547f12-064a-40bb-912b-f9b289a9b18a&algo_expid=56547f12-064a-40bb-912b-f9b289a9b18a-0&btsid=38c35828-6307-4c81-9966-625010b47ed9&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_53'
)

aicokclothessteamer = Products(
product_name= 'AICOK Clothes Steamer',
category_id= 2,
subcategory_id= 10,
short_product_description= 'AICOK Clothes Steamer',
product_description= 'Fast Refresh Your Clothes - Smart 1000W Ultra-Compact Handheld Garment Steamer will let you prep your clothes faster than ever, as it heats up in just 15 seconds, with large 260ml (8.79 oz.) water tank for 15~20 minutes of continuous steaming.',
product_dimensions='11.4 x 7.6 x 5.7 inches',
power_wattage= '1000W',
product_color= 'White and Blue',
price_USD= 24.98,
amazon_link= 'https://www.amazon.com/AICOK-Clothes-Steamer-Version-Leak-Proof/dp/B07PLGLBKR',
aliexpress_link='https://www.aliexpress.com/item/32874557593.html?spm=a2g0o.productlist.0.0.731e71cfvlK0jY&s=p&algo_pvid=27951a0a-1911-41de-8fc2-85cb07038981&algo_expid=27951a0a-1911-41de-8fc2-85cb07038981-1&btsid=83bab821-e855-4527-a4fd-601316e862fb&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_53'
)

sonos_one_speaker = Products(
product_name= 'Sonos One Speaker',
category_id= 5,
subcategory_id= 5,
short_product_description= 'Great Quality Sonos One Speaker',
product_description= 'Ask Alexa to Play music from Amazon Music, Spotify, Pandora, iHeartRadio, TuneIn and SiriusXM. Listen to hundreds of other streaming services with the Sonos app',
product_dimensions='11.4 x 9.6 x 4.7 inches',
power_wattage= '1200W',
product_color= 'Black',
price_USD= 50.1,
amazon_link= 'https://www.amazon.com/All-new-Sonos-One-Streaming-Incredible/dp/B074XLMYY5?ref_=fsclp_pl_dp_2',
aliexpress_link='https://www.aliexpress.com/item/4000149856356.html?spm=a2g0o.productlist.0.0.7fa6776aFPj55J&algo_pvid=7ef25a85-1962-4230-91f1-0744107b2eac&algo_expid=7ef25a85-1962-4230-91f1-0744107b2eac-2&btsid=bda665a5-ba6f-455d-82fe-fa3aae6d2d4e&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_53'
)

double_sided_makeup_mirror = Products(
product_name= '1X & 10X Double Sided Makeup Mirror',
category_id= 6,
subcategory_id= 7,
short_product_description= 'Double Sided Makeup Mirror, 1X & 10X Magnification with 360 Degree Rotation',
product_description= 'I feel pretty Oh, so pretty I feel pretty and witty and bright! And I pity Any girl who isnt me tonight I feel charming Oh, so charming Its alarming how charming I feel! And so pretty That I hardly can believe Im real See the pretty girl in that mirror there',
product_dimensions='17.4 x 2.6 x 7.7 inches',
power_wattage= '1000W',
product_color= 'Silver',
price_USD= 40.34,
amazon_link= 'https://www.amazon.com/Gotofine-Magnifying-Magnification-Rotation-Transparent/dp/B06VWBGYTS/ref=sr_1_16?keywords=makeup+mirror&qid=1576518564&sr=8-16',
aliexpress_link='https://www.aliexpress.com/item/33055381088.html?spm=a2g0o.productlist.0.0.7e0d49e5OwZpwh&algo_pvid=e5dfdf39-6709-490e-898e-0fd944734650&algo_expid=e5dfdf39-6709-490e-898e-0fd944734650-10&btsid=6765906f-e30a-447a-b1a6-90f9857f9842&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_53'
)

yoga_mat_onefourth_inch = Products(
product_name= '1/4 inch Pro Yoga Mat',
category_id= 4,
subcategory_id= 6,
short_product_description= 'Yoga Mat - Classic 1/4 inch Pro Yoga Mat Eco Friendly Non Slip Fitness Exercise Mat',
product_description= 'NEW ECO FRIENDLY MATERIAL: The upgraded TOPLUS Yoga mat is made with premium TPE friendly material. It costs more to make, however it’s worth it when you compare it to the traditional non-green PVC, NBR and EVA yoga mats. TPE material offers the latest technological improvement over traditional yoga mats.',
product_dimensions='20.4 x 10.6 x 3.7 inches',
power_wattage= None,
product_color= 'Blue, Pink, Orange and more',
price_USD= 9.45,
amazon_link= 'https://www.amazon.com/TOPLUS-Friendly-Exercise-Strap-Workout-Exercises/dp/B0776T7372/ref=sr_1_3_sspa?keywords=yoga+mat&qid=1576519405&sr=8-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUUVNWUVVMkpWQ0lCJmVuY3J5cHRlZElkPUExMDA2NTA4MUk2SldWM0FXUTkySyZlbmNyeXB0ZWRBZElkPUEwNjIyOTM4MlZKUjVENzlGV0EyVCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=',
aliexpress_link='https://www.aliexpress.com/item/4000087171998.html?spm=a2g0o.productlist.0.0.2c623f74JXxoFu&algo_pvid=269b672c-8198-40d3-bc95-419e226e24cc&algo_expid=269b672c-8198-40d3-bc95-419e226e24cc-8&btsid=f0518e57-8284-4ae5-b0ca-5f2ec5b255c4&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_53'
)

#adding products to the database
# list_of_products = []
#
# for prod in list_of_products:
#     db.session.add(prod)

#create instances for imgs and vids:

nespresso1 =Imagesandvideos(imgOrvid_link= 'Nespresso1.png', product_id= 1)
nespresso2 =Imagesandvideos(imgOrvid_link= 'Nespresso2.png', product_id= 1)
nespresso3 =Imagesandvideos(imgOrvid_link= 'Nespresso3.png', product_id= 1)

ovengloves1 =Imagesandvideos(imgOrvid_link= 'OvenGloves1.png', product_id= 4)
ovengloves2 =Imagesandvideos(imgOrvid_link= 'OvenGloves2.png', product_id= 4)
ovengloves3 =Imagesandvideos(imgOrvid_link= 'OvenGloves3.png', product_id= 4)

yogamatblue =Imagesandvideos(imgOrvid_link= 'yogamatblue.png', product_id= 6)
yogamatorange =Imagesandvideos(imgOrvid_link= 'yogamatorange.png', product_id= 6)
yogamatpink =Imagesandvideos(imgOrvid_link= 'yogamatpink.png', product_id= 6)

fiveDrip_Coffee_Maker1 =Imagesandvideos(imgOrvid_link= '5Drip_Coffee_Maker1.png', product_id= 5)
fiveDrip_Coffee_Maker2 =Imagesandvideos(imgOrvid_link= '5Drip_Coffee_Maker2.png', product_id= 5)
fiveDrip_Coffee_Maker3 =Imagesandvideos(imgOrvid_link= '5Drip_Coffee_Maker3.png', product_id= 5)

AirFryer1 =Imagesandvideos(imgOrvid_link= 'AirFryer1.png', product_id= 3)
AirFryer2 =Imagesandvideos(imgOrvid_link= 'AirFryer2.png', product_id= 3)
AirFryer3 =Imagesandvideos(imgOrvid_link= 'AirFryer3.png', product_id= 3)
AirFryer4 =Imagesandvideos(imgOrvid_link= 'AirFryer4.png', product_id= 3)

knifeSet1 =Imagesandvideos(imgOrvid_link= 'knifeSet1.png', product_id= 2)
knifeSet2 =Imagesandvideos(imgOrvid_link= 'knifeSet2.png', product_id= 2)
knifeSet3 =Imagesandvideos(imgOrvid_link= 'knifeSet3.png', product_id= 2)

Sonos1 =Imagesandvideos(imgOrvid_link= 'Sonos1.png', product_id= 8)
Sonos2 =Imagesandvideos(imgOrvid_link= 'Sonos2.png', product_id= 8)
Sonos3 =Imagesandvideos(imgOrvid_link= 'Sonos3.png', product_id= 8)

Mmirror1 =Imagesandvideos(imgOrvid_link= 'Mmirror1.png', product_id= 7)
Mmirror2 =Imagesandvideos(imgOrvid_link= 'Mmirror2.png', product_id= 7)
Mmirror3 =Imagesandvideos(imgOrvid_link= 'Mmirror3.png', product_id= 7)

Gsteamer1 =Imagesandvideos(imgOrvid_link= 'Gsteamer1.png', product_id= 9)
Gsteamer2 =Imagesandvideos(imgOrvid_link= 'Gsteamer2.png', product_id= 9)
Gsteamer3 =Imagesandvideos(imgOrvid_link= 'Gsteamer3.png', product_id= 9)


#adding imgs or vids to db
# list_of_imgorvids = [nespresso1, nespresso2, nespresso3, ovengloves1, ovengloves2, ovengloves3, yogamatblue, yogamatorange,
#                      yogamatpink, fiveDrip_Coffee_Maker1, fiveDrip_Coffee_Maker2, fiveDrip_Coffee_Maker3, AirFryer1,
#                      AirFryer2, AirFryer3, AirFryer4, knifeSet1, knifeSet2, knifeSet3, Sonos1, Sonos2, Sonos3,
#                      Mmirror1, Mmirror2, Mmirror3, Gsteamer1, Gsteamer2, Gsteamer3]
#
# for imgvid in list_of_imgorvids:
#     db.session.add(imgvid)
#
# db.session.commit()





