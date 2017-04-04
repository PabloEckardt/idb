#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

import json
from flask import jsonify
from insert_records import init_session
from models import Restaurants, Locations, Food_Types, Reviews, Base

def query_restaurant_by_id(session_obj, i):
    restaurant = session_obj.query(Restaurants).filter_by(id = i).first()
    return jsonify(json_list = restaurant)

def query_all_restaurants(session_obj):
    return jsonify(json_list = session_obj.query(Restaurants).all())

def query_location_by_zip(session_obj, z):
    location = session_obj.query(Locations).filter_by(zip = z).first()
    return jsonify(json_list = location)

def query_all_locations(session_obj):
    return jsonify(json_list = session_obj.query(Locations).all())
	
def query_food_type_by_name(session_obj, n):
    food_types = session_obj.query(Food_Types).filter_by(food_type = n).first()
    return jsonify(json_list = food_types)

def query_all_food_types(session_obj):
    food_types = session_obj.query(Food_Types).all()
    return jsonify(json_list = food_types)

def query_review_by_id(session_obj, id):
    review = session_obj.query(Reviews).filter_by(review_id = id).first()
    return jsonify(json_list = review)

def query_all_reviews(session_obj):
    reviews = session_obj.query(Reviews).all()
    return jsonify(json_list = reviews)

