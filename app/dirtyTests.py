
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import our models
from models import Restaurants, Reviews, Food_Types, Locations, Base
from insert_records import *
db_name = 'sqlite:///sql_example.db'

engine = create_engine(db_name)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session_obj = DBSession()

print("testing restaurants")
new_r = Restaurants (
    name = "Little Italy",
    location = 78701,
    price = "$$",
    rating = "3",
    hours = "9 to 5",
    Recent_Review = "hello",
    food_type = "Italian"
    )

session_obj.add(new_r)
session_obj.commit()
print (session_obj.query(Restaurants).first())
r = session_obj.query(Restaurants).first()
print (r.location)
print(r.Recent_Review)
print(r.food_type)

print("testing food types")

new_ft = Food_Types (food_type = "American",
    average_price = "$$",
    average_rating = "4",
    highest_rated_restaurant = "1",
    best_location = "78701")

session_obj.add(new_ft)
session_obj.commit()


print (session_obj.query(Food_Types).first())
ft = session_obj.query(Food_Types).first()
print (ft.best_location)

print ("testing location")
new_l = Locations (
    zipcode = "78701",
    average_price = "$$$",
    popular_food_type = "italian",
    highest_rated_restaurant = "Litte Italy")


session_obj.add(new_l)
session_obj.commit()

print (session_obj.query(Locations).first())
new_l = session_obj.query(Locations).first()
print (new_l.average_price)

print ("testing review")

new_rev = Reviews (
    review_id = "1",
    date = "12/1/2014",
    rating = "5",
    username ="Fernando",
    restaurant_id = "1",
    zipcode = "78701")


session_obj.add(new_rev)
session_obj.commit()

print (session_obj.query(Reviews).first())
new_rev = session_obj.query(Reviews).first()
print (new_rev.username)


print ("testing functions")

add_restaurant(session_obj,
    name = "big  Italy",
    location = 78702,
    price = "$$$",
    rating = "4",
    hours = "9 to 5",
    Recent_Review = "hello",
    food_type = "Italian"
    )

res = session_obj.query(Restaurants).all()
print (res)

add_location (session_obj,
    zipcode = "78742",
    average_price = "$$$",
    popular_food_type = "italian",
    highest_rated_restaurant = "Litte Italy"
    )

locs = session_obj.query(Locations).all()



