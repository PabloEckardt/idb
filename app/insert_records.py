from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import our models
from models import Restaurants, Locations, Food_Types, Reviews, Base

db_name = 'sqlite:///sql_example.db'

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
def init_session():
    engine = create_engine(db_name)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session_obj = DBSession()
    return session_obj


def add_restaurant(session_obj, name, location, price, rating, hours,
                   food_type, Recent_Review):

    new_restaurant = Restaurants(name=name,
                                 location=location,
                                 price=price,
                                 rating=rating,
                                 hours=hours,
                                 food_type=food_type,
                                 Recent_Review=Recent_Review)

    session_obj.add(new_restaurant)
    session_obj.commit()


def add_location(session_obj, zipcode, average_price, popular_food_type,
                 highest_rated_restaurant, lowest_rated_restaurant,
                 average_rating, average_health_rating, adjacent_location):
    new_location = Locations(
        average_rating=average_rating,
        average_price=average_price,
        ajacent_location=adjacent_location,
        average_health_rating=average_health_rating,
        zipcode=zipcode,
        popular_food_type=popular_food_type,
        highest_rated_restaurant=highest_rated_restaurant
    )

    session_obj.add(new_location)
    session_obj.commit()


def add_food_type(session_obj, food_type, average_price,
                  average_rating, country_of_origin,
                  image_url, open_restaurants,
                  highest_rated_restaurant, best_location,):

    new_food_type = Food_Types(
        food_type=food_type,
        average_price=average_price,
        average_rating=average_rating,
        country_of_origin=country_of_origin,
        image_url=image_url,
        open_restaurants=open_restaurants,
        highest_rated_restaurant=highest_rated_restaurant,
        best_location=best_location
    )

    session_obj.add(new_food_type)
    session_obj.commit()


def add_review(session_obj, date, rating, username, profile_picture_url,
               restaurant_id, restaurant_pictures_url, zipcode):

    # I realized that having zipcode and restaurant id is wasteful.
    new_review = Reviews(
        date=date,
        rating=rating,
        username=username,
        profile_picture_url=profile_picture_url,
        restaurant_pictures_url=restaurant_pictures_url,
        restaurant_id=restaurant_id,
        zipcode=zipcode
    )

    session_obj.add(new_review)
    session_obj.commit()
