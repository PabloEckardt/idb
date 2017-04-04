#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

import json
from insert_records import init_session
from models import Restaurants, Locations, Food_Types, Reviews, Base

def query_restaurants(session_obj, **kwargs):
	restaurant_1 = session_obj.query(Restaurants)
	return jsonify(json_list = qryresult.all())
	

