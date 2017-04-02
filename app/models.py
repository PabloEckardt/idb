"""
models.py
"""

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# -------------
# Reviews
# -------------


class Reviews(Base):
    """
    Primary Key = review_id (Surrogate key)
    Foreign Keys: to Locations Table, and Restaurants Table
    """
    __tablename__ = 'reviews'

    review_id = Column(Integer, primary_key=True)

    date = Column(String(250), nullable=False)
    rating = Column(Integer, nullable=False)
    username = Column(String(250), nullable=False)
    profile_picture_url = Column(String(250), nullable=False)
    restaurant_pictures_url = Column(String(250), nullable=False)

    restaurant_id = Column(Integer, ForeignKey(
        'restaurants.id'), nullable=False)
    restaurant = relationship("Restaurants", foreign_keys=[restaurant_id])

    zipcode = Column(Integer, ForeignKey('locations.zipcode'), nullable=False)
    location = relationship("Locations", foreign_keys=[zipcode])

    def __init__(self, date, rating, username, profile_picture_url,
                  restaurant_pictures_url, restaurant_id, zipcode):

        assert (type(date) is str)
        assert (type(rating) is str)
        assert (type(username) is int)
        assert (type(profile_picture_url) is int)
        assert (type(restaurant_pictures_url) is str)

        assert (type(restaurant_id) is int)
        assert (type(zipcode) is int)


        self.date=date
        self.rating=rating
        self.username=username
        self.profile_picture_url=profile_picture_url
        self.restaurant_pictures_url=restaurant_pictures_url

        self.restaurant_id=restaurant_id
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
    country_of_origin=Column(String(250), nullable=False)
    image_url=Column(String(250), nullable=False)
    open_restaurants=Column(Integer, nullable=True)

    highest_rated_restaurant=Column(
        Integer, ForeignKey('restaurants.id'), nullable=False)
    restaurant=relationship("Restaurants", foreign_keys=[
                            highest_rated_restaurant])

    best_location=Column(Integer, ForeignKey(
        "locations.zipcode"), nullable=False)
    location=relationship("Locations", foreign_keys=[best_location])

    def __init__(self, food_type, average_price, average_rating, country_of_origin,
                  image_url, open_restaurants, highest_rated_restaurant,
                  best_location):

        assert (type(food_type) is String)

        assert (type(average_price) is int)
        assert (type(average_rating) is int)
        assert (type(country_of_origin) is String)
        assert (type(image_url) is String)
        assert (type(open_restaurants) is String)

        assert (type(highest_rated_restaurant) is int)
        assert (type(best_location) is int)

        self.food_type=food_type

        self.average_price=average_price
        self.average_rating=average_rating
        self.country_of_origin=country_of_origin
        self.image_url=image_url
        self.open_restaurants=open_restaurants

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

    id=Column(Integer, primary_key=True)

    name=Column(String(250), nullable=False)
    location=Column(Integer, nullable=False)
    price=Column(Integer, nullable=False)
    rating=Column(Integer, nullable=False)
    hours=Column(String(250), nullable=False)

    food_type=Column(String(250), ForeignKey(
        'food_types.food_type'), nullable=False)
    food=relationship("Food_Types", foreign_keys=[food_type])

    Recent_Review=Column(Integer, ForeignKey(
        'reviews.review_id'), nullable=False)
    review=relationship("Reviews", foreign_keys=[Recent_Review])

    def __init__(self, name, location, price, rating, hours, food_type,
                 Recent_Review):

        assert (type(name) is str)
        assert (type(location) is int)
        assert (type(price) is int)
        assert (type(rating) is int)
        assert (type(hours) is str)

        assert (type(Recent_Review) is int)
        assert (type(food_type) is str)

        self.name=name
        self.location=location
        self.price=price
        self.rating=rating
        self.hours=hours

        self.food_type=food_type
        self.Recent_Review=Recent_Review
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
    adjacent_location=Column(Integer, nullable=False)
    average_health_rating=Column(Integer, nullable=False)
    highest_price=Column(String(250), nullable=False)

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
                 adjacent_location,
                 average_health_rating,
                 zipcode,
                 highest_price,
                 popular_food_type,
                 highest_rated_restaurant):

        assert (type(zipcode) is int)

        assert (type(average_rating) is int)
        assert (type(average_price) is int)
        assert (type(adjacent_location) is int)
        assert (type(average_health_rating) is int)
        assert (type(highest_price) is String)

        assert (type(popular_food_type) is str)
        assert (type(highest_rated_restaurant) is str)

        self.zipcode=zipcode

        self.average_rating=average_rating
        self.average_price=average_price
        self.adjacent_location=adjacent_location
        self.average_health_rating=average_health_rating
        self.highest_price=highest_price

        self.highest_rated_restaurant=highest_rated_restaurant
        self.popular_food_type=popular_food_type

# create an engine that stores data in the local directory's db file
db_name = 'sqlite:///sql_example.db'
engine = create_engine(db_name)

# Create all tables in the engine. Equivalent to Create Table in sql
Base.metadata.create_all(engine)
