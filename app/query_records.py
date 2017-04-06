#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
import json
from app import *
from flask import Flask, request, jsonify
from app.models import Restaurants, Locations, Food_Types, Reviews, Base


def query_all_restaurants(sortby):
    session = Session()
    if sortby == None:
        sortby = "name"
    result = session.query(Restaurants).filter(Restaurants.price != "").order_by(sortby).all()
    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)


def query_all_locations(sortby):
    session = Session()
    if sortby == None:
        sortby = "zipcode"
    result = session.query(Locations).order_by(sortby).all()
    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)
	

def query_all_food_types(sortby):
    session = Session()
    if sortby == None:
        sortby = "food_type"
    result = session.query(Food_Types).order_by(sortby).all()
    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)


def query_all_reviews(sortby):
    if sortby == None:
        sortby = "username"
    session = Session()
    result = session.query(Reviews).order_by(sortby).all()
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)

