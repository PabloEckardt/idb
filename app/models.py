"""
models.py
"""

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
try:
    from app.db_manager import Base, init_session, setupdb
except ImportError:
    from db_manager import *

# -------------
# Reviews
# -------------


class Reviews(Base):
    """
    Primary Key = id (Surrogate key)
    Foreign Keys: to Locations

    restaurant_id = a unique number different from the pk to id restaurants
    associaed with this review

    restaurant_name = name of restaurant associated with review

    yelp_restaurant_id = the string yelp would require to get detail info
    in Yelp API

    food_type = category associated with the restaurant in the review
    food_type_display = a presentable version of the food_type

    date/rating/username/review = review specific information

    review_url/profile_picture_url = yelp links to the review in
    and user profile picture in yelp.com

    zipcode = zipcode associated with restaurant associated with review

    to_dict is a "serialize' type function that allows this object
    to become a json in a much more efficient way

    """
    __tablename__ = 'reviews'
    __table_args__ = {'extend_existing': True}

    # pk
    id = Column(Integer, primary_key=True)
    # identifiers
    restaurant_id = Column(String(250), nullable=False)
    restaurant_name = Column(String(250), nullable=False)
    yelp_restaurant_id = Column(String(250), nullable=False)
    food_type = Column(String(250), nullable=False)
    food_type_disp = Column(String(250), nullable=False)

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
                "food_type": self.food_type,
                "food_type_disp": self.food_type_disp,
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
                 food_type,
                 food_type_disp,
                 date,
                 rating,
                 username,
                 review,
                 profile_picture_url,
                 review_url,
                 zipcode
                 ):

        assert (type(restaurant_id) is str)
        assert (type(restaurant_name) is str)
        assert (type(yelp_restaurant_id) is str)
        assert (type(food_type) is str)
        assert (type(food_type_disp) is str)

        assert (type(date) is str)
        assert (type(rating) is int)
        assert (type(username) is str)
        assert (type(review) is str)

        assert (type(profile_picture_url) is str)
        assert (type(review_url) is str)

        assert (type(zipcode) is str)

        self.restaurant_id = restaurant_id
        self.restaurant_name = restaurant_name
        self.yelp_restaurant_id = yelp_restaurant_id
        self.food_type = food_type
        self.food_type_disp = food_type_disp

        self.date = date
        self.rating = rating
        self.username = username
        self.review = review

        self.profile_picture_url = profile_picture_url
        self.review_url = review_url

        self.zipcode = zipcode

# -------------
# Food Types
# -------------


class Food_Types(Base):
    """
    Primary Key = food_type (Natural Key)
    Foreign Keys: to Locations Table, and Restaurants Table

    average_price = average price of restaurants of a certain food type
    ex: average price of American is 2 where American is a set of
    2 restaurants, one with $ as price, another is $$$

    average_rating = similar to above, average_rating represents how
    is a food type represented as a whole. ex: American 3/5, etc

    number_restaurants = restaurant instances from the Restaurant table
    associated with this food type. ex: 2 American food Restaurants

    most_popular_restaurant = most reviewed restaurant in set of
    restaurants associated with food type

    food_type_display_name = printable version of the food type string

    best_location = zipcode associated with the best and most numerous
    instances of restaurants associated with each specific food type

    to_dict is a "serialize' type function that allows this object
    to become a json in a much more efficient way
    """
    __tablename__ = 'food_types'

    __table_args__ = {'extend_existing': True}

    food_type = Column(String(250), primary_key=True)

    average_price = Column(Float, nullable=False)
    average_rating = Column(Float, nullable=False)
    image_url = Column(String(250), nullable=False)
    number_restaurants = Column(Integer, nullable=False)
    most_popular_restaurant = Column(String(250), nullable=False)
    food_type_display_name = Column(String(250), nullable=False)

    highest_rated_restaurant = Column(
        String(250), ForeignKey('restaurants.id'), nullable=False)
    restaurant = relationship("Restaurants", foreign_keys=[
        highest_rated_restaurant])

    best_location = Column(String(250), ForeignKey(
        "locations.zipcode"), nullable=False)
    location = relationship("Locations", foreign_keys=[best_location])

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

        self.food_type = food_type
        self.food_type_display_name = food_type_display_name

        self.average_price = average_price
        self.average_rating = average_rating
        self.image_url = image_url
        self.number_restaurants = number_restaurants

        self.most_popular_restaurant = most_popular_restaurant
        self.highest_rated_restaurant = highest_rated_restaurant
        self.best_location = best_location

# -------------
# Restaurants
# -------------


class Restaurants(Base):
    """
    Primary Key = id (Surrogate key)
    Foreign Keys: to Food_Types

    name = restaurant name

    yelp_id = id granted by yelp to use in yelp_fusion API

    location = zip where restaurant is located

    lat/long = lat/long of the address of the restaurant

    price = restaurant's user reported rating

    rating = restaurant's performance as far as user ratings

    review = latest or a relevant recent review associated with
    the restaurant.

    review_count = number of reviews given to restaurant

    review_date = date associate with review above.

    url/img_url = links to yelp.com associated with this restaurant

    food_types#/food_type_disp#: restaurants can have up to
    3 food types, and at least one. ex: American Food, Bar.
    Each food_type needs an associated printable format string.

    to_dict is a "serialize' type function that allows this object
    to become a json in a much more efficient way.
    """
    __tablename__ = 'restaurants'

    __table_args__ = {'extend_existing': True}

    # pk
    id = Column(String(250), primary_key=True)
    # identifiers
    name = Column(String(250), nullable=False)
    yelp_id = Column(String(250), nullable=False)
    # location data
    location = Column(Integer, nullable=False)
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)
    city = Column(String(250), nullable=False)
    address = Column(String(250), nullable=True)
    phone = Column(String(250), nullable=False)
    # business data
    price = Column(String(40), nullable=True)
    rating = Column(Float, nullable=False)
    review = Column(String(500), nullable=False)
    review_date = Column(String(250), nullable=False)
    review_count = Column(Integer, nullable=False)
    # urls
    url = Column(String(400), nullable=False)
    img_url = Column(String(400), nullable=True)

    food_type = Column(String(250), ForeignKey(
        'food_types.food_type'), nullable=True)
    food = relationship("Food_Types", foreign_keys=[food_type])

    food_type2 = Column(String(250), ForeignKey(
        'food_types.food_type'), nullable=True)
    food = relationship("Food_Types", foreign_keys=[food_type])

    food_type3 = Column(String(250), ForeignKey(
        'food_types.food_type'), nullable=True)
    food = relationship("Food_Types", foreign_keys=[food_type])

    food_type_disp = Column(String(250), nullable=False)
    food_type_disp2 = Column(String(250), nullable=True)
    food_type_disp3 = Column(String(250), nullable=True)

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
            "food_type3": self.food_type3,
            "food_type_disp": self.food_type_disp,
            "food_type_disp2": self.food_type_disp2,
            "food_type_disp3": self.food_type_disp3
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
                 food_type_disp,
                 food_type2=None,
                 food_type3=None,
                 food_type_disp2=None,
                 food_type_disp3=None):

        assert (type(id) is str)
        assert (type(name) is str)
        assert (type(yelp_id) is str)
        assert (type(location) is int)
        assert (type(lat) is float)
        assert (type(long) is float)
        assert (type(city) is str)

        assert (type(rating) is float)

        assert (type(review) is str)
        assert (type(review_date) is str)
        assert (type(review_count) is int)
        assert (type(url) is str)
        assert (type(img_url) is str)

        assert (type(food_type) is str)
        t = type(food_type_disp)
        assert (t is str or t is None)

        self.id = id

        self.name = name
        self.yelp_id = yelp_id

        self.location = location
        self.lat = lat
        self.long = long
        self.city = city
        self.address = address
        self.phone = phone

        self.price = price
        self.rating = rating
        self.review = review
        self.review_date = review_date
        self.review_count = review_count

        self.url = url
        self.img_url = img_url
        self.food_type = food_type
        self.food_type2 = food_type2
        self.food_type3 = food_type3

        self.food_type_disp = food_type_disp
        self.food_type_disp2 = food_type_disp2
        self.food_type_disp3 = food_type_disp3
# -------------
# Locations
# -------------


class Locations(Base):
    """
    Primary Key = Zipcode (Natural Key)
    Foreign Keys: to Food_Types Table, and Restaurants Table

    average_rating = averaged ratings of all restaurants associated
    with the zipcode

    average_price = averaged price of all restaurants associated
    with the zipcode

    highest_price = highest price found among set of restaurants
    associated with the zipcode

    lowest_price = lowest price found amoung set of restaurants
    associated with the zipcode

    most_popular_restaurant = restaurant key to restaurant
    associated with the zipcode that has the largest number of revies

    number_of_restuarants = number of restaurants associated with zipcode

    popular_food_type = food_type with best performing reviews in quality
    and number in the zipcode. ex: 78704, Tex-Mex

    highest_restaurant = restaurant associated with zipcode with highest
    number of reviews and ratings.

    to_dict is a "serialize' type function that allows this object
    to become a json in a much more efficient way.
    """
    __tablename__ = 'locations'

    __table_args__ = {'extend_existing': True}

    # columns
    zipcode = Column(String(250), primary_key=True)

    average_rating = Column(Float, nullable=False)
    average_price = Column(Float, nullable=False)
    highest_price = Column(String(250), nullable=False)
    lowest_price = Column(String(250), nullable=False)
    most_popular_restaurant = Column(String(250), nullable=False)
    number_restaurants = Column(Integer, nullable=False)

    popular_food_type = Column(String(250), ForeignKey(
        'food_types.food_type'), nullable=False)
    food = relationship("Food_Types", foreign_keys=[popular_food_type])

    highest_rated_restaurant = Column(
        Integer, ForeignKey('restaurants.id'), nullable=False)
    restaurant = relationship("Restaurants", foreign_keys=[
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
        assert (type(zipcode) is str)
        assert (type(average_rating) is float)
        assert (type(average_price) is float)
        assert (type(highest_price) is str)
        assert (type(lowest_price) is str)
        assert (type(most_popular_restaurant) is str)
        assert (type(number_restaurants) is int)
        assert (type(popular_food_type) is str)

        self.zipcode = zipcode

        self.average_rating = average_rating
        self.average_price = average_price
        self.highest_price = highest_price
        self.lowest_price = lowest_price

        self.popular_food_type = popular_food_type
        self.highest_rated_restaurant = highest_rated_restaurant
        self.most_popular_restaurant = most_popular_restaurant
        self.number_restaurants = number_restaurants
