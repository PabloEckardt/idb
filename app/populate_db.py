from app.insert_records import *
from os import listdir
from os.path import isfile, join
import app
import json


def add_restaurants(flask_app):
    session_token = app.Session()
    default = "static/img/default.jpg"
    with open(flask_app.config["REVIEWS"], "r") as rj:
        r = json.load(rj)
        with open(flask_app.config["RESTAURANTS"], "r") as me:
            m = json.load(me)
            for key in m:

                rest_dict=m[key]

                cat_len = len(rest_dict["categories"])
                l = [None] * 3
                for i in range(cat_len):
                    l[i] = (rest_dict["categories"][i]["alias"] + "||" + rest_dict["categories"][i]["title"])

                price = None if not "price" in rest_dict.keys() else rest_dict["price"]
                addr = rest_dict["location"]["address1"] if not rest_dict["location"]["address1"] == "" else "No Entry"
                phone = rest_dict["display_phone"] if not rest_dict["display_phone"] == "" else "No Entry"
                img_url = default if rest_dict["image_url"] == "" else rest_dict["image_url"]

                add_restaurant (
                                session_token,
                                key,
                                rest_dict["name"],
                                rest_dict["id"],
                                int(rest_dict["location"]["zip_code"]),
                                rest_dict["coordinates"]["latitude"],
                                rest_dict["coordinates"]["longitude"],
                                rest_dict["location"]["city"],
                                addr,
                                phone,
                                price,
                                float(rest_dict["rating"]),
                                r[key][0]["text"],
                                r[key][0]["time_created"],
                                rest_dict["review_count"],
                                rest_dict["url"],
                                img_url,
                                *l
                                )


def add_reviews(flask_app):
    session_token = app.Session()
    default = "static/img/default.jpg"
    with open(flask_app.config["REVIEWS"], "r") as rj:
        r = json.load(rj)
        with open(flask_app.config["RESTAURANTS"], "r") as me:
            m = json.load(me)
            for k in r:
                rev_list = r[k]
                for rev_dict in rev_list:
                    img_url = default if rev_dict["user"]["image_url"] == None else rev_dict["user"]["image_url"]

                    add_review(
                        session_token,
                        k,
                        m[k]["id"],
                        rev_dict["time_created"],
                        rev_dict["rating"],
                        rev_dict["user"]["name"],
                        rev_dict["text"],
                        img_url,
                        rev_dict["url"],
                        m[k]["location"]["zip_code"]
                    )



def loc_find_avg_rating (l):
    avg = 0.0
    rest_no = len(l)
    for rest_key in l:
        avg += l[rest_key]["rating"]

    return round(avg/rest_no, 2)

def loc_find_avg_price (l):
    avg = 0.0
    rest_no = len(l)
    for id in l:
        if "price" in l[id]:
            avg += len(l[id]["price"])
        else:
            rest_no = max( 1 ,rest_no - 1)

    total = round(avg / rest_no, 2)
    return 1.0 if total < 1 else total

def loc_find_hi_lo_price (l):

    hi = 1
    lo = 4
    prices = {1:"$",2:"$$",3:"$$$",4:"$$$$"}

    hi_rating = 1.0
    hi_rating_id = ""

    hi_review_count = 0
    popular = ""

    for key in l.keys():
        if "price" in l[key].keys():
            price = len(l[key]["price"])
            hi = hi if hi > price else price
            lo = lo if lo < price else price

        if l[key]["rating"] > hi_rating:
            hi_rating = l[key]["rating"]
            hi_rating_id = key

        if l[key]["review_count"] > hi_review_count:
            hi_review_count = l[key]["review_count"]
            popular = key

    return (prices[hi], prices[lo], popular, hi_rating_id)

def loc_find_popular_food_type (l):
    cats = {}
    cat = l[l.keys()[0]]["categories"][0]["alias"]
    highest = 0

    for key in l:
        for dict in l[key]["categories"]:
            alias = dict["alias"]
            if not alias in cats:
                cats[alias] = 1
            else:
                cats[alias] += 1
                if cats[alias] > highest:
                    highest = cats[alias]
                    cat = alias

    return cat

def add_locations(flask_app):
    session_token = app.Session()
    with open (flask_app.config["LOCATIONS"], "r") as l:
        locs = json.load(l)
        for zip in locs:
            avg_rating = loc_find_avg_rating(locs[zip])
            avg_price = loc_find_avg_price(locs[zip])
            hi_lo_pop_rate = loc_find_hi_lo_price(locs[zip])
            popular_food_type = loc_find_popular_food_type(locs[zip])

            add_location(
                session_token,
                zip,
                avg_rating,
                avg_price,
                hi_lo_pop_rate[0],
                hi_lo_pop_rate[1],
                popular_food_type,
                hi_lo_pop_rate[2],
                hi_lo_pop_rate[3],
                len(locs[zip])
            )





def find_avg_price(l):
    price = 0.0
    rest_no = len(l)
    for dict in l:
        if "price" in dict.keys():
            price += len(dict["price"])
        else:
            rest_no = max( 1 ,rest_no - 1)

    total = round(price / rest_no,2)
    return 1.0 if total < 1 else total

def find_avg_rating(l):

    rating = 0.0
    rest_no = len(l)
    for dict in l:
        rating += dict["rating"]

    return round(rating/ max(rest_no,1.0),2)

def find_img_url (food_type, img_list):

    if food_type in img_list:
        return "static/img/" + food_type + ".jpg"
    else:
        return "/static/img/default.jpg"

def find_highest_rated_r(rl):
    rating = 1
    highest_rate_no = 1
    best = ""
    for dict in rl:
        if dict["rating"] > rating and dict["review_count"] > highest_rate_no:
            best = dict["key"]

    return best if not best == "" else rl[0]["key"]

def find_best_location(rl,ft):
    loc_tally = {}
    for dict in rl:
        if "zip_code" in dict["location"].keys():
            zip = dict["location"]["zip_code"]
            if not zip in loc_tally:
                loc_tally[zip] = 1
            else:
                loc_tally[zip] += 1
    if len(loc_tally) > 1:
        highest = ""
        count = 0
        for zip in loc_tally:
            if loc_tally[zip] > count:
                highest = zip
                count = loc_tally[zip]
        return highest
    else:
        for dict in rl:
            if "zip_code" in dict["location"].keys():
                return dict["location"]["zip_code"]
        print ("WARNING: could not determine the best location for food type, FOOD_TYPE:",ft)
        print ("seting up default 78704 for:", ft)
        return "78704"

def find_most_popular_restaurant(rl):
    n = 0
    id = ""
    for dict in rl:
        if n < dict["review_count"]:
            n = dict["review_count"]
            id = dict["key"]

    return id


def  add_food_types(flask_app):
    session_token = app.Session()
    p = "app/static/img/"
    img_files = [f for f in listdir(p) if isfile(join(p, f))]
    img_files_short = [e.split(".")[0] for e in img_files]
    count = 0
    with open (flask_app.config["FOOD_TYPES"]) as f:
        ft = json.load(f)
        for k in ft:
            count += 1
            restaurant_list = ft[k]
            food_type_display_name = k.split("/")[1]
            k=k.split("/")[0]
            avg_rating = find_avg_rating(restaurant_list)
            avg_price = find_avg_price(restaurant_list)
            img_url = find_img_url(k, img_files_short)
            best_restaurant = find_highest_rated_r(restaurant_list)
            best_location = find_best_location(restaurant_list, k)
            most_popular_restaurant = find_most_popular_restaurant(restaurant_list)

            add_food_type(
                            session_token,
                            k,
                            food_type_display_name,
                            avg_price,
                            avg_rating,
                            img_url,
                            len(restaurant_list),
                            most_popular_restaurant,
                            best_restaurant,
                            best_location
                            )

