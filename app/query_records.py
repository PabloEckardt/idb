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


## Searching via arbitrary parameters

def rest_build_query(param):
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
    return or_(*rest_queries)

def merge_rests(search_output, candidate_output, modelidx = None): # Eliminate duplicates
    if modelidx == None:
        modelidx = 0
    for r in candidate_output:
        if not r["id"] in search_output[modelidx]:
            search_output[modelidx][r["id"]] = r

def search_rests(param, search_output, session_token):
    # TODO for every element in query check where is the match and mark it.
    query = rest_build_query(param)
    restaurants = session_token.query(Restaurants).filter(query).all()
    restaurants = [r.to_dict() for r in restaurants]
    merge_rests(search_output, restaurants)

def loc_build_query (param):
    query = []
    if (param.isdigit()):
        query.append(Locations.average_rating == float(param))
        query.append(Locations.average_price == float(param))
        query.append(Locations.number_restaurants == int(param))
        query.append(Locations.highest_rated_restaurant == int(param))

    query.append(Locations.zipcode == param)
    query.append(Locations.highest_price == param)
    query.append(Locations.lowest_price == param)
    query.append(Locations.most_popular_restaurant == param)
    query.append(Locations.popular_food_type == param)
    query.append(Locations.most_popular_restaurant == param)
    return or_(*query)

def merge_locs(search_output, candidate_output):
    for r in candidate_output:
        if not r["zipcode"] in search_output[0]:
            search_output[1][r["zipcode"]] = r

def search_locs(param, search_output, session_token):
    # TODO mark params in elems
    query = loc_build_query(param)
    locs = session_token.query(Locations).filter(query).all()
    locs = [r.to_dict() for r in locs]
    merge_locs(search_output, locs)


def food_build_query(param):
    query = []
    if (param.isdigit()):
        query.append(Food_Types.average_price == float(param))
        query.append(Food_Types.average_rating == float(param))
        query.append(Food_Types.number_restaurants == int(param))
        query.append(Food_Types.average_price == float(param))

    query.append(Food_Types.food_type == param)
    query.append(Food_Types.image_url == param)
    query.append(Food_Types.most_popular_restaurant == param)
    query.append(Food_Types.food_type_display_name == param)
    query.append(Food_Types.highest_rated_restaurant == param)
    query.append(Food_Types.best_location == param)
    return or_(*query)

def merge_foods(search_output, candidate_output):
    for r in candidate_output:
        if not r["food_type"] in search_output[0]:
            search_output[2][r["food_type"]] = r

def search_foods(param, search_output, session_token):
    query = food_build_query(param)
    foods = session_token.query(Food_Types).filter(query).all()
    foods = [r.to_dict() for r in foods]
    merge_foods(search_output, foods)

def rev_build_query(param):
    query = []
    if (param.isdigit()):
        query.append(Reviews.id == int(param))
        query.append(Reviews.rating == int(param))
        query.append(Reviews.zipcode == int(param))

    query.append(Reviews.restaurant_name == param)
    query.append(Reviews.yelp_restaurant_id == param)
    query.append(Reviews.food_type == param)
    query.append(Reviews.food_type_disp == param)
    query.append(Reviews.date == param)
    query.append(Reviews.username == param)
    query.append(Reviews.review == param)
    query.append(Reviews.profile_picture_url == param)
    query.append(Reviews.date == param)
    query.append(Reviews.review_url == param)
    query.append(Reviews.profile_picture_url == param)
    return or_(*query)

def search_revs(param, search_output, session_token):
    query = rev_build_query(param)
    revs = session_token.query(Reviews).filter(query).all()
    revs = [r.to_dict() for r in revs]
    merge_rests(search_output, revs, 3) # reuse rests merge function because both models
                                        # have a id attribute as primary key

def search_query(*params):
    # for every param we want to build 4 jsons.
    search_output = [{},{},{},{}] #restaurants, locations, foodtypes, reviews
    # TODO make a list of dictionaries of pks to reduce search time in merge funcs
    model_searches = [search_rests, search_locs, search_foods, search_revs]
    session = Session()
    for param in params:
        for model,search_func in enumerate(model_searches):
            search_func(param,search_output, session) # this line searches a given parameter in all attributes
                                                            # to in a model and places all results without
                                                            # duplicates inside of search output
    return search_output

# un comment to see a how to use
"""
print ("test #####################")
p = ["Aakash P."] # test with a reviewer id
results = search_query(*p)
print ("testing query:", p)
print()
print ("result is an array of 4 jsons, Restaurants, locatios, foodtypes, reviews")
for dict in results:
    print ("elements found for table:", len (dict))
print()
print ("search query results")
for e in results:
    for d in e:
        print (d)
        print (e[d])
"""
