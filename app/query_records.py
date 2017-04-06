#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
import json
from app import *
from flask import Flask, request, jsonify
from app.models import Restaurants, Locations, Food_Types, Reviews, Base

def query_restaurant_by_id(session_obj, i):
    restaurant = session_obj.query(Restaurants).filter_by(id = i).first()
    result = {"id": i,
            "name": restaurant.name,
            "location": restaurant.location,
            "price": restaurant.price,
            "rating": restaurant.rating,
            "food_type": restaurant.food_type,
            "Recent_Review": restaurant.Recent_Review
            }
    return json.dumps(result)

def query_all_restaurants(sortby):
    session = Session()
    if sortby == None:
        sortby = "name"
    result = session.query(Restaurants).filter(Restaurants.price != "").order_by(sortby).all()
    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)

def query_location_by_zip(session_obj, z):
    location = session_obj.query(Locations).filter_by(zipcode = z).first()
    result = {"zipcode":z,
            "average_rating":location.average_rating,
            "average_price":location.average_price,
            "adjacent_location":location.adjacent_location,
            "average_health_rating":location.average_health_rating,
            "highest_price":location.highest_price,
            "popular_food_type":location.popular_food_type,
            "highest_rated_restaurant":location.highest_rated_restaurant
            }
    return json.dumps(result)

def query_all_locations(session_obj):
    result = session_obj.query(Locations).all()
    ret = []
    for location in result :
        conv = {"zipcode":location.zipcode,
            "average_rating":location.average_rating,
            "average_price":location.average_price,
            "adjacent_location":location.adjacent_location,
            "average_health_rating":location.average_health_rating,
            "highest_price":location.highest_price,
            "popular_food_type":location.popular_food_type,
            "highest_rated_restaurant":location.highest_rated_restaurant
            }
        ret.append(conv)
    return json.dumps(ret)
	
def query_food_type_by_name(session_obj, n):
    food_type = session_obj.query(Food_Types).filter_by(food_type = n).first()
    result = {"food_type": food_type.food_type,
            "average_price":food_type.average_price,
            "average_rating":food_type.average_rating,
            "country_of_origin":food_type.country_of_origin,
            "image_url":food_type.image_url,
            "open_restaurants":food_type.open_restaurants,
            "highest_rated_restaurant":food_type.highest_rated_restaurant,
            "best_location":food_type.best_location
            }
    return json.dumps(result)

def query_all_food_types(sortby):
    session = Session()
    if sortby == None:
        sortby = "food_type"
    result = session.query(Food_Types).order_by(sortby).all()
    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)

def query_review_by_id(session_obj, id):
    review = session_obj.query(Reviews).filter_by(review_id = id).first()
    result = {"review_id":review.review_id,
            "date":review.date,
            "rating":review.rating,
            "username":review.username,
            "profile_picture_url":review.profile_picture_url,
            "restaurant_pictures_url":review.restaurant_pictures_url,
            "restaurant_id":review.restaurant_id,
            "zipcode":review.zipcode
            }
    return json.dumps(result)

def query_all_reviews(sortby):
    if sortby == None:
        sortby = "username"
    session = Session()
    result = session.query(Reviews).order_by(sortby).all()
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)

