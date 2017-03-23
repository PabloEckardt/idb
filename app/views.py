from flask import render_template, Blueprint, render_template
restaurant_db=[
    {"name" : "Little Italy",
    "img": "italy.jpeg",
    "last_review" : "Excellent Garlic Bread. -Tom",
    "location" : "1215 S Congress",
    "zip" : "78701",
    "price" : "$$",
    "hours": "11:00am to 11:00pm",
    "food_type": "Italian",
    "rating": "3.4",
    "img": "italy.jpg",
    "id" : "1"
    },
    {"name" : "Gato",
    "img": "gato.jpg",
    "last_review" : "They actually don't serve cat 1/10. -Tom",
    "location" : "5568 N Lamar Blvd",
    "zip" : "78702",
    "price" : "$$$",
    "hours": "11:00am to 9:00pm",
    "food_type": "Mediterranean",
    "rating": "4",
    "id" : "2"
    },
    {"name" : "Stack Burgers",
    "img": "stack.jpg",
    "last_review" : "I tried their waffles, not impressed. -Jen",
    "location" : "1231 Wells Branch Pwy",
    "zip" : "78703",
    "price" : "$",
    "hours": "11:00am to 11:00am",
    "food_type": "American",
    "rating": "5",
    "id" : "3"
    },
    {"name" : "Biryani Pot",
    "img": "biryani.jpg",
    "last_review" : "Try their Chicken Dum Biryani! It's absolutely heavenly. -Jeff",
    "location" : "12407 N Mopac Expy",
    "zip" : "78704",
    "price" : "$$",
    "hours": "11:00am to 10:00am",
    "food_type": "Indian",
    "rating": "5",
    "id" : "4"
    },
    {"name" : "Ho Ho Chinese BBQ",
    "img": "hoho.jpg",
    "last_review" : "I loved their bbq pork fried rice. -Nathan",
    "location" : "12407 N Mopac Expy",
    "zip" : "78705",
    "price" : "$$",
    "hours": "11:00am to 9:30am",
    "food_type": "Chinese",
    "rating": "5",
    "id" : "5"
    }]

location_db=[
    {"zip": "78701",
    "average_price": "$$",
    "average_rating": "4",
    "popular_food_type": "Italian",
    "highest_rated_restaurant": "Little Italy",
    "highest_rated_restaurant_id": "1",
    "cheapest_restaurant": "Niki's Pizza"
    },
    {"zip": "78702", 
    "average_price": "$$$",
    "average_rating": "5",
    "popular_food_type": "Mediterranean",
    "highest_rated_restaurant": "Gato",
    "highest_rated_restaurant_id": "2",
    "cheapest_restaurant": "Verts"
    },
    {"zip": "78703", 
    "average_price": "$",
    "average_rating": "3",
    "popular_food_type": "American",
    "highest_rated_restaurant": "Stack Burgers",
    "highest_rated_restaurant_id": "3",
    "cheapest_restaurant": "McDonalds"
    },
    {"zip": "78704", 
    "average_price": "$$",
    "average_rating": "2",
    "popular_food_type": "Indian",
    "highest_rated_restaurant": "Biryani",
    "highest_rated_restaurant_id": "4",
    "cheapest_restaurant": "Tarka"
    },
    {"zip": "78705", 
    "average_price": "$",
    "average_rating": "4.5",
    "popular_food_type": "Chinese",
    "highest_rated_restaurant": "Ho ho Chinese BBQ",
    "highest_rated_restaurant_id": "5",
    "cheapest_restaurant": "Panda Express"
    }]

food_type_db=[
    {"food_type": "Chinese",
     "average_price": "$",
     "average_rating": "3",
     "highest_rated_restaurant": "Ho Ho chinese BBQ",
     "highest_rated_restaurant_id": "5",
     "best_location": "78705"
    },
    {"food_type": "Mediterranean",
     "average_price": "$$$",
     "average_rating": "4.2",
     "highest_rated_restaurant": "Gato",
     "highest_rated_restaurant_id": "2",
     "best_location": "78702"
    },
    {"food_type": "Italian",
     "average_price": "$$$",
     "average_rating": "4.8",
     "highest_rated_restaurant": "Little Italy",
     "highest_rated_restaurant_id": "1",
     "best_location": "78701"
    },
    {"food_type": "Indian",
     "average_price": "$$",
     "average_rating": "3.8",
     "highest_rated_restaurant": "Biryani",
     "highest_rated_restaurant_id": "4",
     "best_location": "78704"
    },
    {"food_type": "American",
     "average_price": "$",
     "average_rating": "3.1",
     "highest_rated_restaurant": "Stack Burgers",
     "highest_rated_restaurant_id": "3",
     "best_location": "78703"
     }]

review_db =[
    {"review_id": "1",
     "date": "1/10/2014",
     "rating": "4",
     "username": "Federico",
     "restaurant": "Little Italy",
     "location": "78701",
     "review": "Incredible Garlic Bread",
     "restaurant_id": "1"
    },
    {"review_id": "2",
     "date": "2/11/2015",
     "rating": "3",
     "username": "Chuck",
     "restaurant": "Gato",
     "location": "78702",
     "review": "Great Hummus",
     "restaurant_id": "2"
    },
    {"review_id": "3",
     "date": "1/4/2017",
     "rating": "5",
     "username": "Gabriel",
     "restaurant": "Stack Burgers",
     "location": "78703",
     "review": "Didn't like their Waffles",
     "restaurant_id": "3"
    },
    {"review_id": "4",
     "date": "1/10/2017",
     "rating": "4",
     "username": "Dominique",
     "restaurant": "Biryani Pot",
     "location": "78704",
     "review": "Great Basmati rice",
     "restaurant_id": "4"
    },
    {"review_id": "5",
     "date": "1/11/2004",
     "rating": "4",
     "username": "Maggie",
     "restaurant": "Ho Ho Chinese BBQ",
     "location": "78705",
     "review": "I didn't like the General Tso Chicken",
     "restaurant_id": "5"
     }]

views = Blueprint('views', __name__)

# Splash Screen
@views.route('/')
@views.route('/index')
def index():
    return render_template("index.html")
# Model Views
@views.route('/Restaurants')
def Restaurants():
    global restaurant_db
    return render_template("restaurants.html", model_elements = restaurant_db)

@views.route('/Locations')
def Locations():
    global location_db
    return render_template(
        "locations.html", model_elements = location_db)

@views.route('/Food_Types')
def Food_Types():
    global food_type_db
    return render_template(
        "food_types.html", model_elements = food_type_db)

@views.route('/Reviews')
def Reviews():
    global review_db
    return render_template(
        "reviews.html", model_elements = review_db)

@views.route('/About')
def About():
    return render_template("about.html")

# Model Elements Views

# RESTAURANTS

@views.route('/Restaurants/<pk>')
def restaurant(pk):
    global restaurant_db
    for d in restaurant_db:
        if d["id"] == pk:
            return render_template("restaurant_instance.html",instance=d)

# LOCATIONS

@views.route('/Locations/<pk>')
def location(pk):
    global location_db
    for d in location_db:
        if d["zip"] == pk:
            return render_template("location_instance.html",instance=d)

# FOOD TYPES

@views.route('/Food_Types/<pk>')
def food_type(pk):
    global food_type_db
    for d in food_type_db:
        if d["food_type"] == pk:
            return render_template("food_type_instance.html", instance=d)

# REVIEWS

@views.route('/Reviews/<pk>')
def review(pk):
    global review_db
    for d in review_db:
        if d["review_id"] == pk:
            return render_template("review_instance.html",instance=d)
