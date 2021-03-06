#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

from .divide_parameters import *
from app import *
from flask import Flask, request, jsonify
from app.models import Restaurants, Locations, Food_Types, Reviews, Base
from sqlalchemy import or_
# Query all instances


def query_all_restaurants(sortby, rating, price, foodtype, name, id):
    """
    Returns a list of restaurants filtered for the given qualities.
    sortby - the attribute by which to sort the results. Defaults to "name".
    rating - (int) the desired rating
    price - (string) the desired price, formatted as a string of $'s
    foodtype - (string) the desired name of the foodtype
    name - (string) the desired restaurant name
    id - the desired restaurant id
    """
    session = Session()
    if sortby is None:
        sortby = "name"
    queries = [Restaurants.price != ""]
    if price is not None:
        prices = price.split(",")
        pQ = []
        for a in prices:
            pQ.append(Restaurants.price == a)
        if len(pQ) > 0:
            queries.append(or_(*pQ))
    if rating is not None:
        ratings = rating.split(",")
        rQ = []
        for a in ratings:
            rQ.append(Restaurants.rating == a)
        if len(rQ) > 0:
            queries.append(or_(*rQ))
    if foodtype is not None:
        foodtypes = foodtype.split(",")
        fQ = []
        for a in foodtypes:
            fQ.append(Restaurants.food_type.like('%' + a + '%'))
        if len(fQ) > 0:
            queries.append(or_(*fQ))

    if name is not None:
        fQ = [Restaurants.name.like('%' + name + '%')]
        queries.append(*fQ)

    if id is not None:
        fQ = [Restaurants.id == id]
        queries.append(*fQ)
    # queries.append(or_(*price))

    # ratings = [Restaurants.rating == 1]
    # ratings.append(Restaurants.rating ==2)

    # queries.append(or_(*ratings))

    result = session.query(Restaurants).filter(*queries).order_by(sortby).all()

    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)


def query_all_locations(sortby, avgrating, avgprice, foodtype):
    """
    Returns a list of locations based on given attributes.
    sortby - attribute by which to sort, defaults to zipcode
    avgrating - (double) desired average rating
    avgprice - (double) desired average price
    foodtype - (string) desired food type
    """
    session = Session()
    if sortby is None:
        sortby = "zipcode"

    queries = []

    if avgprice is not None:
        prices = avgprice.split(",")
        pQ = []
        for a in prices:
            pQ.append(Locations.average_price == a)
        if len(pQ) > 0:
            queries.append(or_(*pQ))
    if avgrating is not None:
        ratings = avgrating.split(",")
        rQ = []
        for a in ratings:
            rQ.append(Locations.average_rating == int(a))
        if len(rQ) > 0:
            queries.append(or_(*rQ))
    if foodtype is not None:
        foodtypes = foodtype.split(",")
        fQ = []
        for a in foodtypes:
            fQ.append(Locations.popular_food_type.like('%' + a + '%'))
        if len(fQ) > 0:
            queries.append(or_(*fQ))

    result = session.query(Locations).filter(*queries).order_by(sortby).all()
    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)


def query_all_food_types(sortby, avgrating, avgprice, foodtype):
    """
    Returns a list of food types based on given attributes.
    sortby - attribute by which to sort, defaults to food type
    avgrating - (double) desired average rating
    avgprice - (double) desired average price
    foodtype - (string) desired food type
    """
    session = Session()
    if sortby is None:
        sortby = "food_type"

    queries = []

    if avgprice is not None:
        prices = avgprice.split(",")
        pQ = []
        for a in prices:
            pQ.append(Food_Types.average_price == a)
        if len(pQ) > 0:
            queries.append(or_(*pQ))
    if avgrating is not None:
        ratings = avgrating.split(",")
        rQ = []
        for a in ratings:
            rQ.append(Food_Types.average_rating == int(a))
        if len(rQ) > 0:
            queries.append(or_(*rQ))
    if foodtype is not None:
        foodtypes = foodtype.split(",")
        fQ = []
        for a in foodtypes:
            fQ.append(Food_Types.food_type.like('%' + a + '%'))
        if len(fQ) > 0:
            queries.append(or_(*fQ))

    result = session.query(Food_Types).filter(*queries).order_by(sortby).all()
    # TODO: Figure out more efficient way to do this
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)


def query_all_reviews(sortby, rating, hasimg, foodtype, id):
    """
    Returns a list of reviews with the desired attributes.
    sortby - attribute by which to sort, defaults to username
    rating - (int) the desired rating
    hasimg - (boolean) whether or not the returned review author has a profile picture
    foodtype - (string) the desired food type
    id - (int) the desired review id
    """
    if sortby == None:
        sortby = "username"
    session = Session()

    queries = []

    if rating is not None:
        ratings = rating.split(",")
        rQ = []
        for a in ratings:
            rQ.append(Reviews.rating == int(a))
        if len(rQ) > 0:
            queries.append(or_(*rQ))
    if foodtype is not None:
        foodtypes = foodtype.split(",")
        fQ = []
        for a in foodtypes:
            fQ.append(Reviews.food_type.like('%' + a + '%'))
        if len(fQ) > 0:
            queries.append(or_(*fQ))
    if hasimg is not None:
        queries.append(Reviews.profile_picture_url !=
                       "/static/img/default.jpg")
    if id is not None:
        tQ = [Reviews.id == int(id)]
        queries.append(*tQ)

    result = session.query(Reviews).filter(*queries).order_by(sortby).all()
    result2 = [e.to_dict() for e in result]
    return jsonify(result2)

# Query one instance by id


def query_restaurant(id):
    """
    Return the restaurant with the given id
    """
    session = Session()
    result = session.query(Restaurants).filter(Restaurants.id == id).all()
    assert (len(result) == 1)
    return result[0].to_dict()


def query_review(id):
    """
    Return the review with the given id
    """
    session = Session()
    result = session.query(Reviews).filter(Reviews.id == id).all()
    assert (len(result) == 1)
    return result[0].to_dict()


def query_restaurant_reviews(id):
    """
    Return all reviews for the restaurant with the given id
    """
    session = Session()
    result = session.query(Reviews).filter(Reviews.restaurant_id == id).all()
    result2 = [e.to_dict() for e in result]
    print(result2)
    return result2


def query_food_type(food_type):
    """
    Return the food type with the given name.
    """
    session = Session()
    result = session.query(Food_Types).filter(
        Food_Types.food_type == food_type).all()
    # result = session.query(Food_Types).all()
    # result2 = [e.to_dict() for e in result]
    # print(result[0].to_dict())
    assert (len(result) == 1)
    print(result[0].to_dict())
    # return result2[0]
    return result[0].to_dict()


def query_location(zipcode):
    """
    Return the location with the given zip code.
    """
    session = Session()
    result = session.query(Locations).filter(
        Locations.zipcode == zipcode).all()
    assert (len(result) == 1)
    return result[0].to_dict()


# Searching via arbitrary parameters

def rest_build_query(param):
    """
    :param string user is using to search: 
    :return a list of queries adept to the Restaurant model: 
    Some queries make sense to look into substrings
    """
    rest_queries = []
    if (param.isdigit()):
        rest_queries.append(Restaurants.location == int(param))
        rest_queries.append(Restaurants.lat == float(param))
        rest_queries.append(Restaurants.long == float(param))
        rest_queries.append(Restaurants.rating == int(param))
        # rest_queries.append(Restaurants.id == int(param))

    rest_queries.append(Restaurants.name.like('%' + param + '%'))
    rest_queries.append(Restaurants.yelp_id.like('%' + param + '%'))
    rest_queries.append(Restaurants.city.like('%' + param + '%'))
    rest_queries.append(Restaurants.address.like('%' + param + '%'))
    rest_queries.append(Restaurants.phone.like('%' + param + '%'))
    rest_queries.append(Restaurants.review_date.like('%' + param + '%'))
    rest_queries.append(Restaurants.price.like('%' + param + '%'))
    rest_queries.append(Restaurants.url.like('%' + param + '%'))
    rest_queries.append(Restaurants.food_type.like('%' + param + '%'))
    rest_queries.append(Restaurants.food_type2.like('%' + param + '%'))
    rest_queries.append(Restaurants.food_type3.like('%' + param + '%'))
    rest_queries.append(Restaurants.food_type_disp.like('%' + param + '%'))
    rest_queries.append(Restaurants.food_type_disp2.like('%' + param + '%'))
    rest_queries.append(Restaurants.food_type_disp3.like('%' + param + '%'))
    return or_(*rest_queries)


def loc_build_query(param):
    """
    :param  string user is using to search: 
    :return a list of queries adept to the Locations model: 
    Some queries make sense to look into substrings
    """
    query = []
    if (param.isdigit()):
        query.append(Locations.average_rating == float(param))
        query.append(Locations.average_price == float(param))
        query.append(Locations.number_restaurants == int(param))
        query.append(Locations.highest_rated_restaurant == int(param))

    query.append(Locations.zipcode == param)
    query.append(Locations.highest_price == param)
    query.append(Locations.lowest_price == param)
    query.append(Locations.most_popular_restaurant.like('%' + param + '%'))
    query.append(Locations.popular_food_type.like('%' + param + '%'))
    query.append(Locations.most_popular_restaurant.like('%' + param + '%'))
    return or_(*query)


def food_build_query(param):
    """
    :param  string user is using to search: 
    :return a list of queries adept to the Food_Types model: 
    Some queries make sense to look into substrings
    """
    query = []
    if (param.isdigit()):
        query.append(Food_Types.average_price == float(param))
        query.append(Food_Types.average_rating == float(param))
        query.append(Food_Types.number_restaurants == int(param))
        query.append(Food_Types.average_price == float(param))

    query.append(Food_Types.food_type.like('%' + param + '%'))
    query.append(Food_Types.image_url.like('%' + param + '%'))
    query.append(Food_Types.most_popular_restaurant.like('%' + param + '%'))
    query.append(Food_Types.food_type_display_name.like('%' + param + '%'))
    query.append(Food_Types.highest_rated_restaurant.like('%' + param + '%'))
    query.append(Food_Types.best_location.like('%' + param + '%'))
    return or_(*query)


def rev_build_query(param):
    """
    :param  string user is using to search: 
    :return a list of queries adept to the Reviews model: 
    Some queries make sense to look into substrings
    """
    query = []
    if (param.isdigit()):
        query.append(Reviews.id == int(param))
        query.append(Reviews.rating == int(param))
        query.append(Reviews.zipcode == int(param))

    query.append(Reviews.restaurant_name.like('%' + param + '%'))
    # query.append(Reviews.yelp_restaurant_id == param)
    query.append(Reviews.food_type.like('%' + param + '%'))
    query.append(Reviews.food_type_disp.like('%' + param + '%'))
    query.append(Reviews.date.like('%' + param + '%'))
    query.append(Reviews.username.like("%" + param + "%"))
    query.append(Reviews.review.like('%' + param + '%'))
    query.append(Reviews.profile_picture_url.like('%' + param + '%'))
    query.append(Reviews.date.like('%' + param + '%'))
    query.append(Reviews.review_url.like('%' + param + '%'))
    query.append(Reviews.profile_picture_url.like('%' + param + '%'))
    return or_(*query)


def merge_models(search_output, candidate_output, high_p_out=None, i=None):
    """
    :param search_output: Where caller expects results without duplicates
    :param candidate_output: Output before checking for duplicates
    :param high_p_out: search_output compares against this.
           Set of results to be shown first.
    :return: None
    """
    # Eliminate duplicates
    keys = ["id", "zipcode", "food_type", "id"]

    if high_p_out is None:
        for r in candidate_output:
            if not r[keys[i]] in search_output[i]:
                search_output[i][r[keys[i]]] = r
    else:
        for r in candidate_output:
            if not r[keys[i]] in search_output[i] and not r[keys[i]
                                                            ] in high_p_out[i]:
                search_output[i][r[keys[i]]] = r


def search_models(session_token, param, search_output, high_p_out=None):
    """
    :param session_token: Alchemy Session
    :param param: Simplified search keyword
    :param search_output: base priority search results
    :param high_p_out: high priority search results
    :return: None, functions has effect on parameters
    """
    queries_builders = [rest_build_query, loc_build_query,
                        food_build_query, rev_build_query]
    models = [Restaurants, Locations, Food_Types, Reviews]

    for i in range(4):
        query = queries_builders[i](param)
        instances = session_token.query(models[i]).filter(query)
        instances_dict = [inst.to_dict() for inst in instances]

        if high_p_out is None:
            merge_models(search_output, instances_dict, None, i)
        else:
            merge_models(search_output, instances_dict, high_p_out, i)


def search_query(params):
    """
    :params: List of strings user passed to search
    :return: list of 8 dictionaries with return values first 4 dicts
             are higher priority, meaning they should be displayed first
             the other 4 are basic results
    """
    params = [str(p) for p in params]           # make sure its always strings

    # assume all strings are 1 argument
    whole_param = params[0]
    for i in range(1, len(params)):
        whole_param += " "
        whole_param += params[i]

    # make all logical groups from a set
    param_groups = make_divisions(params)
    # of strings, exclude last 2 cases

    # Results that contain >1 matching
    high_pri_output = [{}, {}, {}, {}]
    # strings ordered in rest,loc,food,rev

    # Any result containing 1 matching string
    search_output = [{}, {}, {}, {}]

    session = Session()

    # do search for whole string assumption
    search_models(session, whole_param, high_pri_output)

    for search in param_groups:
        # do search with second weakest assumption
        search_models(session, search, high_pri_output)

    for param in params:
        # do search for any matches
        search_models(session, param, search_output, high_pri_output)

    return [*high_pri_output, *search_output]
