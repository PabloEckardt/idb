#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

import json
from insert_records import init_session
from models import Restaurants, Locations, Food_Types, Reviews, Base

def query_restaurants_filter(session_obj, **kwargs):
	restaurants = session_obj.query(Restaurants).filter_by(**kwargs)
	return jsonify(json_list = qryresult.all())
	