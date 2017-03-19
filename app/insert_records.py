from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import our models
from models.py import Restaurants, Locations, Food_types, Reviews

absolute_path = 'sqlite:////home/pablo/git/idb/'
db_name = 'alchemy_test_1'

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
def init_session():
    engine = create_engine(absolute_path + db_name)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session_obj = DBSession()
    return session_obj

def add_restaurant(session_obj, name, location, price, rating, hours, \
                   food_type, recent_review):

    new_restaurant = Restaurants(name=name,\
                                location=location,\
                                price=price, \
                                rating=rating,\
                                hours=hours,\
                                food_type=food_type \
                                recent_review=recent_review)

    session_obj.add(new_restaurant)
    session_obj.commit()

def add_location(session_obj, zipcode, average_price, popular_food_type, \
                 highest_rated_restaurant, lowest_rated_restaurant):

    new_location = Locations(zipcode=zipcode, \
                             average_price=average_price, \
                             popular_food_type=popular_food_type, \
                             highest_rated_restaurant=highest_rated_restaurant, \
                             lowest_rated_restaurant=lowest_rated_restaurant)

    session_obj.add(new_location)
    session_obj.commit()

def add_food_type(session_obj, food_type, average_price, average_rating, \
                  highest_rated_restaurant, best_location):

    new_food_type = Food_types(food_type=food_type,\
                               average_rating=average_rating,\
                               average_price=average_price,\
                               highest_rated_restaurant=highest_rated_restaurant,\
                               best_location=best_location)

    session_obj.add(new_food_type)
    session_obj.commmi()

def add_review(session_obj, date, rating, username, restaurant_id,\
              zipcode):
    # I realized that having zipcode and restaurant id is wasteful. 
    new_review = Reviews(date=date,\
                         rating=rating,\
                         username=username,\
                         restaurant_id=restaurant_id,\
                         zipcode=zipcode)
    session_obj.add(new_review)
    session_obj.commit()
