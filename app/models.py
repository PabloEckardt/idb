import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Reviews(Base):
    __tablename__ = 'reviews'

    # Unless we have both a name and a time of publication (to the minute)
    # we have to use another surrogate key
    review_id = Column(Integer, primary_key=True)

    date = Column(String(250), nullable=False)
    rating = Column(Integer, nullable=False)
    username = Column(String(250), nullable=False)
    profile_picture_url = Column(String(250), nullable=False)
    restaurant_pictures_url = Column(String(250), nullable=False)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    restaurant = relationship("Restaurants", foreign_keys=[restaurant_id])

    zipcode = Column(Integer, ForeignKey('locations.zipcode'), nullable=False)
    location = relationship("Locations", foreign_keys=[zipcode])


class Food_Types(Base):
    __tablename__ = 'food_types'

    food_type = Column(String(250), primary_key=True)

    average_price = Column(Integer, nullable=False)
    average_rating = Column(Integer, nullable=False)
    country_of_origin = Column(String(250), nullable=False)
    image_url = Column(String(250), nullable=False)
    open_restaurants = Column(Integer, nullable=True)

    highest_rated_restaurant = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    restaurant = relationship("Restaurants", foreign_keys=[highest_rated_restaurant])

    best_location = Column(Integer, ForeignKey("locations.zipcode"), nullable=False)
    location = relationship("Locations", foreign_keys=[best_location])


class Restaurants(Base):
    __tablename__ = 'restaurants'

    # columns
    # We need a surrogate key because name is not a unique key

    id = Column(Integer, primary_key=True)

    name = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)
    price = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    hours = Column(String(250), nullable=False)

    food_type = Column(String(250), ForeignKey('food_types.food_type'), nullable=False)
    food = relationship("Food_Types", foreign_keys=[food_type])

    Recent_Review = Column(String(250), ForeignKey('reviews.review_id'), nullable=False)
    review = relationship("Reviews", foreign_keys=[Recent_Review])


class Locations(Base):
    __tablename__ = 'locations'

    # columns
    zipcode = Column(Integer, primary_key=True)

    average_rating = Column(Integer, nullable=False)
    average_price = Column(Integer, nullable=False)
    adjacent_location = Column (Integer, nullable=False)
    average_health_rating = Column(Integer,nullable=False)
    highest_price = Column(String(250), nullable=False)

    popular_food_type = Column(String(250), ForeignKey('food_types.food_type'), nullable=False)
    food = relationship("Food_Types", foreign_keys=[popular_food_type])

    highest_rated_restaurant = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    restaurant = relationship("Restaurants", foreign_keys=[highest_rated_restaurant])


# create an engine that stores data in the local directory's db file
#db_name = 'sqlite:///sql_example.db'
#engine = create_engine(db_name)

# Create all tables in the engine. Equivalent to Create Table in sql
Base.metadata.create_all(engine)
