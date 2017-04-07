"""
models.py
"""

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.db_manager import Base

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
    # identifiers
    restaurant_id = Column(String(250), nullable=False)
    restaurant_name = Column(String(250), nullable=False)
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

    def to_dict(self):
        return {"id": self.id,
                "restaurant_id": self.restaurant_id,
                "restaurant_name": self.restaurant_name,
                "yelp_restaurant_id": self.yelp_restaurant_id,
                "date": self.date,
                "rating": self.rating,
                "username": self.username,
                "review": self.review,
                "profile_picture_url": self.profile_picture_url,
                "review_url": self.review_url,
                "zipcode": self.zipcode}

    def __init__(self,
                 restaurant_id,
                 restaurant_name,
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
        self.restaurant_name=restaurant_name
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

    food_type_display_name=Column(String(250),nullable=False)

    average_price=Column(Float, nullable=False)
    average_rating=Column(Float, nullable=False)
    image_url=Column(String(250), nullable=False)
    number_restaurants=Column(Integer, nullable=False)
    most_popular_restaurant=Column(String(250), nullable=False)
    food_type_display_name=Column(String(250),nullable=False)

    highest_rated_restaurant=Column(
        Integer, ForeignKey('restaurants.id'), nullable=False)
    restaurant=relationship("Restaurants", foreign_keys=[
                            highest_rated_restaurant])

    best_location=Column(Integer, ForeignKey(
        "locations.zipcode"), nullable=False)
    location=relationship("Locations", foreign_keys=[best_location])

    def to_dict(self):
        return {"food_type": self.food_type,
                "food_type_display_name": self.food_type_display_name,
                "average_price": self.average_price,
                "average_rating": self.average_rating,
                "image_url": self.image_url,
                "number_restaurants": self.number_restaurants,
                "most_popular_restaurant": self.most_popular_restaurant,
                "highest_rated_restaurant": self.highest_rated_restaurant,
                "best_location": self.best_location}

    def __init__(self,
                 food_type,
                 food_type_display_name,
                 average_price,
                 average_rating,
                 image_url,
                 number_restaurants,
                 most_popular_restaurant,
                 highest_rated_restaurant,
                 best_location
                 ):


        assert (type(average_price) is float)
        assert (type(average_rating) is float)


        self.food_type=food_type
        self.food_type_display_name=food_type_display_name

        self.average_price=average_price
        self.average_rating=average_rating
        self.image_url=image_url
        self.number_restaurants=number_restaurants

        self.most_popular_restaurant=most_popular_restaurant
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

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "yelp_id": self.yelp_id,
                "location": self.location,
                "lat": self.lat,
                "long": self.long,
                "city": self.city,
                "address": self.address,
                "phone": self.phone,
                "price": self.price,
                "rating": self.rating,
                "review": self.review,
                "review_date": self.review_date,
                "review_count": self.review_count,
                "url": self.url,
                "img_url": self.img_url,
                "food_type": self.food_type,
                "food_type2": self.food_type2,
                "food_type3": self.food_type3
                }

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
    zipcode=Column(String(250), primary_key=True)

    average_rating=Column(Float, nullable=False)
    average_price=Column(Float, nullable=False)
    highest_price=Column(String(250), nullable=False)
    lowest_price=Column(String(250), nullable=False)
    most_popular_restaurant=Column(String(250),nullable=False)
    number_restaurants=Column(Integer, nullable=False)

    popular_food_type=Column(String(250), ForeignKey(
        'food_types.food_type'), nullable=False)
    food=relationship("Food_Types", foreign_keys=[popular_food_type])

    highest_rated_restaurant=Column(
        Integer, ForeignKey('restaurants.id'), nullable=False)
    restaurant=relationship("Restaurants", foreign_keys=[
                            highest_rated_restaurant])
    def to_dict(self):
        return {"zipcode": self.zipcode,
                "average_rating": self.average_rating,
                "average_price": self.average_price,
                "highest_price": self.highest_price,
                "lowest_price": self.lowest_price,
                "popular_food_type": self.popular_food_type,
                "highest_rated_restaurant": self.highest_rated_restaurant,
                "most_popular_restaurant": self.most_popular_restaurant,
                "number_restaurants": self.number_restaurants}

    def __init__(
                    self,
                    zipcode,
                    average_rating,
                    average_price,
                    highest_price,
                    lowest_price,
                    popular_food_type,
                    highest_rated_restaurant,
                    most_popular_restaurant,
                    number_restaurants
                 ):


        self.zipcode=zipcode

        self.average_rating=average_rating
        self.average_price=average_price
        self.highest_price=highest_price
        self.lowest_price=lowest_price

        self.popular_food_type=popular_food_type
        self.highest_rated_restaurant=highest_rated_restaurant
        self.most_popular_restaurant=most_popular_restaurant
        self.number_restaurants=number_restaurants
