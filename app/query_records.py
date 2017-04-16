#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
import json
from app import *
from flask import Flask, request, jsonify
from app.models import Restaurants, Locations, Food_Types, Reviews, Base
from sqlalchemy import or_

# Query all instances


def query_all_restaurants(sortby, rating, price, foodtype, name, id):
    session = Session()
    if sortby == None:
        sortby = "name"
    queries = [Restaurants.price != ""]
    if price != None:
        prices = price.split(",")
        pQ = []
        for a in prices:
            pQ.append(Restaurants.price == a)
        if len(pQ) > 0:
            queries.append(or_(*pQ))
    if rating != None:
        ratings = rating.split(",")
        rQ = []
        for a in ratings:
            rQ.append(Restaurants.rating == a)
        if len(rQ) > 0:
            queries.append(or_(*rQ))
    if foodtype != None:
        foodtypes = foodtype.split(",")
        fQ = []
        for a in foodtypes:
            fQ.append(Restaurants.food_type == a)
        if len(fQ) > 0:
            queries.append(or_(*fQ))

    if name != None:
        fQ = [Restaurants.name.like('%' + name + '%')]
        queries.append(*fQ)

    if id != None:
        fQ = [Restaurants.id == id]
        queries.append(*fQ)
    # queries.append(or_(*price))

    #ratings = [Restaurants.rating == 1]
    #ratings.append(Restaurants.rating ==2)

    # queries.append(or_(*ratings))

    result = session.query(Restaurants).filter(*queries).order_by(sortby).all()

    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)


def query_all_locations(sortby, avgrating, avgprice, foodtype):
    session = Session()
    if sortby == None:
        sortby = "zipcode"

    queries = []

    if avgprice != None:
        prices = avgprice.split(",")
        pQ = []
        for a in prices:
            pQ.append(Locations.average_price == a)
        if len(pQ) > 0:
            queries.append(or_(*pQ))
    if avgrating != None:
        ratings = avgrating.split(",")
        rQ = []
        for a in ratings:
            rQ.append(Locations.average_rating == int(a))
        if len(rQ) > 0:
            queries.append(or_(*rQ))
    if foodtype != None:
        foodtypes = foodtype.split(",")
        fQ = []
        for a in foodtypes:
            fQ.append(Locations.popular_food_type == a)
        if len(fQ) > 0:
            queries.append(or_(*fQ))

    result = session.query(Locations).filter(*queries).order_by(sortby).all()
    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)


def query_all_food_types(sortby, avgrating, avgprice, foodtype):
    session = Session()
    if sortby == None:
        sortby = "food_type"

    queries = []

    if avgprice != None:
        prices = avgprice.split(",")
        pQ = []
        for a in prices:
            pQ.append(Food_Types.average_price == a)
        if len(pQ) > 0:
            queries.append(or_(*pQ))
    if avgrating != None:
        ratings = avgrating.split(",")
        rQ = []
        for a in ratings:
            rQ.append(Food_Types.average_rating == int(a))
        if len(rQ) > 0:
            queries.append(or_(*rQ))
    if foodtype != None:
        foodtypes = foodtype.split(",")
        fQ = []
        for a in foodtypes:
            fQ.append(Food_Types.food_type == a)
        if len(fQ) > 0:
            queries.append(or_(*fQ))

    result = session.query(Food_Types).filter(*queries).order_by(sortby).all()
    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)


def query_all_reviews(sortby, rating, hasimg, foodtype, id):
    if sortby == None:
        sortby = "username"
    session = Session()

    queries = []

    if rating != None:
        ratings = rating.split(",")
        rQ = []
        for a in ratings:
            rQ.append(Reviews.rating == int(a))
        if len(rQ) > 0:
            queries.append(or_(*rQ))
    if foodtype != None:
        foodtypes = foodtype.split(",")
        fQ = []
        for a in foodtypes:
            fQ.append(Reviews.food_type == a)
        if len(fQ) > 0:
            queries.append(or_(*fQ))
    if hasimg != None:
        queries.append(Reviews.profile_picture_url !=
                       "/static/img/default.jpg")
    if id != None:
        tQ = [Reviews.id == int(id)]
        queries.append(*tQ)

    result = session.query(Reviews).filter(*queries).order_by(sortby).all()
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)

# Query one instance by id


def query_restaurant(id):
    session = Session()
    result = session.query(Restaurants).filter(Restaurants.id == id).all()
    assert (len(result) == 1)
    return result[0].to_dict()


def query_review(id):
    session = Session()
    result = session.query(Reviews).filter(Reviews.id == id).all()
    assert (len(result) == 1)
    return result[0].to_dict()


def query_restaurant_reviews(id):
    session = Session()
    result = session.query(Reviews).filter(Reviews.restaurant_id == id).all()
    result2 = [e.to_dict() for e in result]
    print(result2)
    return result2


def query_food_type(food_type):
    session = Session()
    result = session.query(Food_Types).filter(
        Food_Types.food_type == food_type).all()
    #result = session.query(Food_Types).all()
    #result2 = [e.to_dict() for e in result]
    # print(result[0].to_dict())
    assert (len(result) == 1)
    print(result[0].to_dict())
    # return result2[0]
    return result[0].to_dict()


def query_location(zipcode):
    session = Session()
    result = session.query(Locations).filter(
        Locations.zipcode == zipcode).all()
    assert (len(result) == 1)
    return result[0].to_dict()


def rest_build_query(param):
    print ("param")
    print (param)
    rest_queries = []
    if (param.isdigit()):
        rest_queries.append(Restaurants.location == int(param))
        rest_queries.append(Restaurants.lat == float(param))
        rest_queries.append(Restaurants.long == float(param))
        rest_queries.append(Restaurants.rating == int(param))
        rest_queries.append(Restaurants.id == int(param))

    rest_queries.append(Restaurants.name == param)
    rest_queries.append(Restaurants.yelp_id == param)
    rest_queries.append(Restaurants.city == param)
    rest_queries.append(Restaurants.address == param)
    rest_queries.append(Restaurants.phone == param)
    rest_queries.append(Restaurants.review_date == param)
    rest_queries.append(Restaurants.price == param)
    rest_queries.append(Restaurants.url == param)
    rest_queries.append(Restaurants.food_type == param)
    rest_queries.append(Restaurants.food_type2 == param)
    rest_queries.append(Restaurants.food_type3 == param)
    rest_queries.append(Restaurants.food_type_disp == param)
    rest_queries.append(Restaurants.food_type_disp2 == param)
    rest_queries.append(Restaurants.food_type_disp3 == param)
    for c in rest_queries:
        print (str(c))
    return or_(*rest_queries)

def merge_rests(search_output, candidate_output): # Eliminate duplicates
    # TODO make a dictionary so we can reduce the O(n^2) to O(n)
    f = True
    for r in candidate_output:
        for r2 in search_output[0]:
            if r.id == r2.id:
                f = False
                break
        if f:
            search_output[0][r.id] = r
        else:
            f = True

def search_rests(param, search_output, session_token):
    query = rest_build_query(param)
    restaurants = session_token.query(Restaurants).filter(*query).all()
    print (restaurants)
    merge_rests(search_output, restaurants)

def search_locs(parameter, model_idx, search_output, session_token):
    pass

def search_foods(parameter, model_idx, search_output, session_token):
    pass

def search_revs(parameter, model_idx, search_output, session_token):
    pass

def search_query(*params):
    # for every param we want to build 4 jsons.
    search_output = [{},{},{},{}] #restaurants, locations, foodtypes, reviews
    # TODO make a list of dictionaries of pks to reduce search time in merge funcs
    model_searches = [search_rests]
    #model_searches = [search_rests, search_locs, search_foods, search_revs]
    session = Session()
    for param in params:
        for model,search_func in enumerate(model_searches):
            search_func(param,search_output, session) # this line searches a given parameter in all attributes
                                                            # to in a model and places all results without
                                                            # duplicates inside of search output
    """
    for param in params:
        for model in models:
            for attribute in model:
                if param == attribute:
                   if instance_id not in search_output[model]:
                       search_output[model][instance_id] = instance
    """
    return search_output
print ("test #####################")
print (search_query('1234'))
print( "end test ##################")
print ("search 2")
s = Session
result = s.query(Reviews).filter(Reviews.restaurant_id == 1234).all()
result2 = [e.to_dict() for e in result]
print(result2)
print ("end test2")



