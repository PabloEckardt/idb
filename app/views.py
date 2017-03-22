from flask import render_template, Blueprint, render_template
spoof_db =[
    {"name" : "Little Italy",\
     "img": "italy.jpeg", \
    "last review" : "Excellent Garlic Bread. -Tom", \
    "location" : "1215 S Congress", \
    "zip" : "78701", \
    "price" : "$$", \
    "hours": "11:00am to 11:00pm", \
    "food type": "Italian Food", \
    "rating": "3.4",\
    "img": "italy.jpg",\
    "id" : "1"
    },
    {"name" : "Gato",\
     "img": "gato.jpg", \
    "last review" : "They actually don't serve cat 1/10. -Tom", \
    "location" : "5568 N Lamar Blvd", \
    "zip" : "78702", \
    "price" : "$$$", \
    "hours": "11:00am to 9:00pm", \
    "food type": "Mediterranean Food", \
    "rating": "4",\
    "id" : "2"
    }, 
    {"name" : "Stack Burgers",\
    "img": "stack.jpg", \
    "last review" : "I tried their waffles, not impressed. -Jen", \
    "location" : "1231 Wells Branch Pwy", \
    "zip" : "78703", \
    "price" : "$", \
    "hours": "11:00am to 11:00am", \
    "food type": "American Food", \
    "rating": "5",\
    "id" : "3"
    }]
views = Blueprint('views', __name__)

@views.route('/')
@views.route('/index')
def index():
    return render_template("index.html")
# Model Views

@views.route('/Restaurants')
def Restaurants():
    global spoof_db
    return render_template("restaurants.html", model_elements = spoof_db)

@views.route('/Locations')
def Locations():
    return render_template(
        "grid.html",\
        model_elements = [
            {"name" : "78701", "img": "temp_image.png"},\
            {"name" : "78702", "img": "temp_image.png"},\
            {"name" : "78703", "img": "temp_image.png"}
        ])

@views.route('/Food_Types')
def Food_types():
    return render_template(
        "grid.html",\
        model_elements = [
            {"name" : "Italian", "img": "temp_image.png"},\
            {"name" : "American", "img": "temp_image.png"},\
            {"name" : "Spanish", "img": "temp_image.png"}
        ])

@views.route('/Reviews')
def Reviews():
    return render_template(
        "grid.html",\
        model_elements = [
            {"name" : "Gato - John", "img": "temp_image.png"},\
            {"name" : "Stack Burgerz - Roney", "img": "temp_image.png"},\
            {"name" : "Little Italy - Tom", "img": "temp_image.png"}
        ])

@views.route('/About')
def About():
    return render_template("about.html")
# Model Elements Views
@views.route('/Restaurants/<pk>')
def restaurant(pk):
    global spoof_db
    for d in spoof_db:
	if d["id"] == pk:
	    return render_template("restaurant_instance.html",instance=d)
