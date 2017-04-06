from flask import render_template, Blueprint, render_template, jsonify
from app.query_records import *


food_types = [
     ["acaibowls","Acai Bowls"],
     ["african","African"],
     ["argentine","Argentine"],
     ["asianfusion","Asian Fusion"],
     ["bagels","Bagels"],
     ["bakeries","Bakeries"],
     ["bars","Bars"],
     ["bbq","Barbeque"],
     ["beer_and_wine","Beer, Wine & Spirits"],
     ["beerbar","Beer Bar"],
     ["beergardens","Beer Gardens"],
     ["beertours","Beer Tours"],
     ["beverage_stores","Beverage Store"],
     ["bistros","Bistros"],
     ["brasseries","Brasseries"],
     ["brazilian","Brazilian"],
     ["breakfast_brunch","Breakfast & Brunch"],
     ["breweries","Breweries"],
     ["british","British"],
     ["bubbletea","Bubble Tea"],
     ["buffets","Buffets"],
     ["burgers","Burgers"],
     ["burmese","Burmese"],
     ["cafes","Cafes"],
     ["cafeteria","Cafeteria"],
     ["cajun","Cajun","Creole"],
     ["cakeshop","Patisserie","Cake Shop"],
     ["candy","Candy Stores"],
     ["cantonese","Cantonese"],
     ["caribbean","Caribbean"],
     ["cheese","Cheese Shops"],
     ["cheesesteaks","Cheesesteaks"],
     ["chicken_wings","Chicken Wings"],
     ["chickenshop","Chicken Shop"],
     ["chinese","Chinese"],
     ["chocolate","Chocolatiers & Shops"],
     ["cideries","Cideries"],
     ["cocktailbars","Cocktail Bars"],
     ["coffee","Coffee & Tea"],
     ["coffeeroasteries","Coffee Roasteries"],
     ["colombian","Colombian"],
     ["comfortfood","Comfort Food"],
     ["creperies","Creperies"],
     ["cuban","Cuban"],
     ["cupcakes","Cupcakes"],
     ["customcakes","Custom Cakes"],
     ["delicatessen","Delicatessen"],
     ["delis","Delis"],
     ["desserts","Desserts"],
     ["dimsum","Dim Sum"],
     ["diners","Diners"],
     ["distilleries","Distilleries"],
     ["divebars","Dive Bars"],
     ["diyfood","Do-It-Yourself Food"],
     ["dominican","Dominican"],
     ["donuts","Donuts"],
     ["empanadas","Empanadas"],
     ["ethiopian","Ethiopian"],
     ["falafel","Falafel"],
     ["filipino","Filipino"],
     ["fishnchips","Fish & Chips"],
     ["fondue","Fondue"],
     ["food_court","Food Court"],
     ["food","Food"],
     ["foodstands","Food Stands"],
     ["foodtrucks","Food Trucks"],
     ["french","French"],
     ["gastropubs","Gastropubs"],
     ["gelato","Gelato"],
     ["german","German"],
     ["gluten_free","Gluten-Free"],
     ["gourmet","Specialty Food"],
     ["greek","Greek"],
     ["halal","Halal"],
     ["hawaiian","Hawaiian"],
     ["herbsandspices","Herbs & Spices"],
     ["himalayan","Himalayan","Nepalese"],
     ["hookah_bars","Hookah Bars"],
     ["hotdog","Hot Dogs"],
     ["hotdogs","Fast Food"],
     ["hotpot","Hot Pot"],
     ["icecream","Ice Cream & Frozen Yogurt"],
     ["importedfood","Imported Food"],
     ["indonesian","Indonesian"],
     ["indpak","Indian"],
     ["international","International"],
     ["irish_pubs","Irish Pub"],
     ["irish","Irish"],
     ["italian","Italian"],
     ["izakaya","Izakaya"],
     ["japanese","Japanese"],
     ["juicebars","Juice Bars & Smoothies"],
     ["karaoke","Karaoke"],
     ["kombucha","Kombucha"],
     ["korean","Korean"],
     ["kosher","Kosher"],
     ["latin","Latin American"],
     ["lebanese","Lebanese"],
     ["localflavor","Local Flavor"],
     ["lounges","Lounges"],
     ["macarons","Macarons"],
     ["markets","Fruits & Veggies"],
     ["meats","Meat Shops"],
     ["mediterranean","Mediterranean"],
     ["mexican","Mexican"],
     ["mideastern","Middle Eastern"],
     ["modern_european","Modern European"],
     ["mongolian","Mongolian"],
     ["moroccan","Moroccan"],
     ["newamerican","American (New)"],
     ["noodles","Noodles"],
     ["oliveoil","Olive Oil"],
     ["pakistani","Pakistani"],
     ["panasian","Pan Asian"],
     ["persian","Persian","Iranian"],
     ["peruvian","Peruvian"],
     ["pizza","Pizza"],
     ["poke","Poke"],
     ["poolhalls","Pool Halls"],
     ["popcorn","Popcorn Shops"],
     ["pretzels","Pretzels"],
     ["provencal","Provencal"],
     ["pubs","Pubs"],
     ["puertorican","Puerto Rican"],
     ["ramen","Ramen"],
     ["raw_food","Live","Raw Food"],
     ["restaurants","Restaurants"],
     ["russian","Russian"],
     ["salad","Salad"],
     ["salvadoran","Salvadoran"],
     ["sandwiches","Sandwiches"],
     ["scandinavian","Scandinavian"],
     ["seafood","Seafood"],
     ["seafoodmarkets","Seafood Markets"],
     ["shavedice","Shaved Ice"],
     ["smokehouse","Smokehouse"],
     ["soulfood","Soul Food"],
     ["soup","Soup"],
     ["southern","Southern"],
     ["spanish","Spanish"],
     ["sportsbars","Sports Bars"],
     ["steak","Steakhouses"],
     ["streetvendors","Street Vendors"],
     ["sud_ouest","French Southwest"],
     ["supperclubs","Supper Clubs"],
     ["sushi","Sushi Bars"],
     ["szechuan","Szechuan"],
     ["tacos","Tacos"],
     ["taiwanese","Taiwanese"],
     ["tapas","Tapas Bars"],
     ["tapasmallplates","Tapas","Small Plates"],
     ["tea","Tea Rooms"],
     ["teppanyaki","Teppanyaki"],
     ["tex-mex","Tex-Mex"],
     ["thai","Thai"],
     ["tradamerican","American (Traditional)"],
     ["turkish","Turkish"],
     ["tuscan","Tuscan"],
     ["vegan","Vegan"],
     ["vegetarian","Vegetarian"],
     ["venezuelan","Venezuelan"],
     ["vietnamese","Vietnamese"],
     ["waffles","Waffles"],
     ["wine_bars","Wine Bars"],
     ["wineries","Wineries"],
     ["winetastingroom","Wine Tasting Room"],
     ["winetours","Wine Tours"],
     ["wraps","Wraps"]]

views = Blueprint('views', __name__)

# Splash Screen


@views.route('/')
@views.route('/index')
def index():
    return render_template("index.html")
# Model Views


@views.route('/Restaurants')
def Restaurants():
    return render_template("restaurants.html", food_types = food_types)


@views.route('/Locations')
def Locations():
    return render_template(
        "locations.html", food_types = food_types)


@views.route('/Food_Types')
def Food_Types():
    return render_template(
        "food_types.html", food_types=food_types)


@views.route('/Reviews')
def Reviews():
    return render_template(
        "reviews.html", food_types=food_types)


@views.route('/About')
def About():
    return render_template("about.html")

# Model Elements Views

# RESTAURANTS

@views.route('/Restaurants/<pk>')
def restaurant(pk):
    d = query_restaurant(pk)
    return render_template("restaurant_instance.html", instance=d)

# LOCATIONS


@views.route('/Locations/<pk>')
def location(pk):
    d = query_location(pk)
    return render_template("location_instance.html", instance=d)

# FOOD TYPES


@views.route('/Food_Types/<pk>')
def food_type(pk):
    print(pk)
    d = query_food_type(pk)
    return render_template("food_type_instance.html", instance=d)

# REVIEWS


@views.route('/Reviews/<pk>')
def review(pk):
    d = query_review(pk)
    return render_template("review_instance.html", instance=d)

# Tech Report


@views.route('/About/TechReport')
def techreport():
    return render_template("techreport.html")

# API
@views.route('/API/Restaurants', methods=['GET'])
def restaurants_api():
    return query_all_restaurants(request.args.get('sortby'))

@views.route('/API/Reviews', methods=['GET'])
def reviews_api():
    return query_all_reviews(request.args.get('sortby'))

@views.route('/API/Food_Types', methods=['GET'])
def food_types_api():
    return query_all_food_types(request.args.get('sortby'))

@views.route('/API/Locations', methods=['GET'])
def locations_api():
    return query_all_locations(request.args.get('sortby'))
