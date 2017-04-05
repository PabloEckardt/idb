from db_manager import init_session, setupdb
from sqlalchemy import create_engine
from insert_records import add_restaurant
import json
import os

db_name = 'sqlite:///food_close_to.db'
db_engine = create_engine(db_name)
setupdb(db_engine)
session_token = init_session(db_engine)



# TODO populate all restaurants
with open("reviews.json", "r") as rj:
    r = json.load(rj)
    with open("one2oneMega.json", "r") as me:
        m = json.load(me)
        for key in m:

            cat_len = len(m[key]["categories"])
            l = [None] * 3
            for i in range(cat_len):
                l[i] = (m[key]["categories"][i]["alias"] + "/" + m[key]["categories"][i]["title"])
            price = None
            if "price" in m[key].keys():
                price = m[key]["price"]

            add_restaurant (
                            session_token,
                            m[key]["name"],
                            int(m[key]["location"]["zip_code"]),
                            price,
                            float(m[key]["rating"]),
                            r[key][0]["text"],
                            r[key][0]["time_created"],
                            *l
                            )



# TODO populate all reviews

# TODO populate all Locations (tedious)

# TODO populate all food types
