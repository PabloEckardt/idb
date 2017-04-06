"""
models.py
"""

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from db_manager import Base

# -------------
# Reviews
# -------------


class Reviews(Base):
    """
    Primary Key = review_id (Surrogate key)
    Foreign Keys: to Locations Table, and Restaurants Table
    """
    __tablename__ = 'reviews'

    # pk
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(String(250), nullable=False)
    # identifiers
    yelp_restaurant_id = Column(String(250), nullable=False)

    # Review Data
    date = Column(String(250), nullable=False)
    rating = Column(Integer, nullable=False)
    username = Column(String(250), nullable=False)
    review = Column(String(900), nullable=False)

    # urls
    profile_picture_url = Column(String(250), nullable=True)
    review_url = Column(String(350), nullable=False)

    zipcode = Column(Integer, ForeignKey('locations.zipcode'), nullable=False)
    location = relationship("Locations", foreign_keys=[zipcode])

    def __init__(self,
                 restaurant_id,
                 yelp_restaurant_id,
                 date,
                 rating,
                 username,
                 review,
                 profile_picture_url,
                 review_url,
                 zipcode
                 ):

        assert (type(date) is unicode)
        assert (type(rating) is int)
        assert (type(username) is unicode)

        assert (type(review_url) is unicode)

        assert (type(zipcode) is unicode)

        self.restaurant_id=restaurant_id
        self.yelp_restaurant_id=yelp_restaurant_id

        self.date=date
        self.rating=rating
        self.username=username
        self.review=review

        self.profile_picture_url=profile_picture_url
        self.review_url=review_url

        self.zipcode=zipcode

# -------------
# Food Types
# -------------

class Food_Types(Base):
    """
    Primary Key = food_type (Natural Key)
    Foreign Keys: to Locations Table, and Restaurants Table
    """
    __tablename__='food_types'

    food_type=Column(String(250), primary_key=True)

    average_price=Column(Integer, nullable=False)
    average_rating=Column(Integer, nullable=False)
    image_url=Column(String(250), nullable=False)
    number_restaurants=Column(Integer, nullable=False)


    highest_rated_restaurant=Column(
        Integer, ForeignKey('restaurants.id'), nullable=False)
    restaurant=relationship("Restaurants", foreign_keys=[
                            highest_rated_restaurant])

    best_location=Column(Integer, ForeignKey(
        "locations.zipcode"), nullable=False)
    location=relationship("Locations", foreign_keys=[best_location])

    def __init__(self,
                 food_type,
                 average_price,
                 average_rating,
                 image_url,
                 highest_rated_restaurant,
                 best_location
                 ):

        assert (type(food_type) is str)

        assert (type(average_price) is int)
        assert (type(average_rating) is int)
        assert (type(image_url) is str)

        assert (type(highest_rated_restaurant) is int)
        assert (type(best_location) is int)

        self.food_type=food_type

        self.average_price=average_price
        self.average_rating=average_rating
        self.image_url=image_url

        self.highest_rated_restaurant=highest_rated_restaurant
        self.best_location=best_location

# -------------
# Restaurants
# -------------

class Restaurants(Base):
    """
    Primary Key = id (Surrogate key)
    Foreign Keys: to Food_Types Table, and Reviews Table
    """
    __tablename__='restaurants'

    # pk
    id=Column(String(250), primary_key=True)
    # identifiers
    name=Column(String(250), nullable=False)
    yelp_id = Column(String(250), nullable=False)
    # location data
    location=Column(Integer, nullable=False)
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)
    city = Column(String(250), nullable=False)
    address = Column(String(250), nullable=True)
    phone = Column(String(250), nullable=False)
    # business data
    price=Column(String(40), nullable=True)
    rating=Column(Float, nullable=False)
    review=Column(String(500), nullable=False)
    review_date=Column(String(250), nullable=False)
    review_count=Column(Integer, nullable=False)
    review_key=Column(String(50), nullable=False)
    # urls
    url = Column(String(400), nullable=False)
    img_url = Column(String(400), nullable=True)



    food_type=Column(String(250), ForeignKey(
        'food_types.food_type'), nullable=True)
    food=relationship("Food_Types", foreign_keys=[food_type])

    food_type2=Column(String(250), ForeignKey(
        'food_types.food_type'), nullable=True)
    food=relationship("Food_Types", foreign_keys=[food_type])

    food_type3=Column(String(250), ForeignKey(
        'food_types.food_type'), nullable=True)
    food=relationship("Food_Types", foreign_keys=[food_type])

    def __init__(self,
                 id,
                 name,
                 yelp_id,
                 location,
                 lat,
                 long,
                 city,
                 address,
                 phone,
                 price,
                 rating,
                 review,
                 review_date,
                 review_count,
                 review_key,
                 url,
                 img_url,
                 food_type,
                 food_type2 = None,
                 food_type3 = None):

        assert (type(name) is unicode)
        assert (type(location) is int)
        assert (type(rating) is float)

        assert (type(review) is unicode)
        assert (type(review_date) is unicode)

        self.id=id

        self.name=name
        self.yelp_id=yelp_id

        self.location=location
        self.lat=lat
        self.long=long
        self.city=city
        self.address=address
        self.phone=phone

        self.price=price
        self.rating=rating
        self.review=review
        self.review_date=review_date
        self.review_count=review_count
        self.review_key=review_key

        self.url=url
        self.img_url=img_url
        self.food_type=food_type
        self.food_type2=food_type2
        self.food_type3=food_type3
# -------------
# Locations
# -------------

class Locations(Base):
    """
    Primary Key = Zipcode (Natural Key)
    Foreign Keys: to Food_Types Table, and Restaurants Table
    """
    __tablename__='locations'

    # columns
    zipcode=Column(Integer, primary_key=True)

    average_rating=Column(Integer, nullable=False)
    average_price=Column(Integer, nullable=False)
    highest_price=Column(Integer, nullable=False)

    popular_food_type=Column(String(250), ForeignKey(
        'food_types.food_type'), nullable=False)
    food=relationship("Food_Types", foreign_keys=[popular_food_type])

    highest_rated_restaurant=Column(
        Integer, ForeignKey('restaurants.id'), nullable=False)
    restaurant=relationship("Restaurants", foreign_keys=[
                            highest_rated_restaurant])

    def __init__(self,
                 average_rating,
                 average_price,
                 zipcode,
                 highest_price,
                 popular_food_type,
                 highest_rated_restaurant):

        assert (type(zipcode) is int)

        assert (type(average_rating) is int)
        assert (type(average_price) is int)
        assert (type(highest_price) is int)

        assert (type(popular_food_type) is str)
        assert (type(highest_rated_restaurant) is str)

        self.zipcode=zipcode

        self.average_rating=average_rating
        self.average_price=average_price
        self.highest_price=highest_price

        self.highest_rated_restaurant=highest_rated_restaurant
        self.popular_food_type=popular_food_type
