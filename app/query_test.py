

#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

import pprint
import json
from flask import Flask, jsonify
from app.models import Restaurants, Locations, Food_Types, Reviews
from app.db_manager import *

#db_name = 'sqlite:///food_close_to.db'
#db_engine = create_engine(db_name)
#session_token = init_session(db_engine)

def query_all_restaurants(session_obj):
    result = session_obj.query(Restaurants).order_by(Restaurants.name).all()
    ret = []
    for restaurant in result :
        conv = {"id": restaurant.id,
                "name": restaurant.name,
                "location": restaurant.location,
                "price": restaurant.price,
                "rating": restaurant.rating,
                "food_type": restaurant.food_type,
                "food_type2": restaurant.food_type2,
                "food_type3": restaurant.food_type3,
                "Review": restaurant.Review,
                "Review_Date": restaurant.Review_Date
                }
        ret.append(conv)
    return ret

#l = query_all_restaurants(session_token)
#
#print (type(l))
#pprint.pprint(l, indent=4)
