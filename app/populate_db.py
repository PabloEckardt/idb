from insert_records import add_restaurant
import app
import json


def add_restaurants(flask_app):
    session_token = app.Session()
    with open(flask_app.config["REVIEWS"], "r") as rj:
        r = json.load(rj)
        with open(flask_app.config["RESTAURANTS"], "r") as me:
            m = json.load(me)
            for key in m:

                rest_dict=m[key]

                cat_len = len(rest_dict["categories"])
                l = [None] * 3
                for i in range(cat_len):
                    l[i] = (rest_dict["categories"][i]["alias"] + "-" + rest_dict["categories"][i]["title"])

                price = None if not "price" in rest_dict.keys() else rest_dict["price"]
                addr = rest_dict["location"]["address1"] if not rest_dict["location"]["address1"] == "" else "No Entry"
                phone = rest_dict["display_phone"] if not rest_dict["display_phone"] == "" else "No Entry"
                img_url = "No Entry" if rest_dict["image_url"] == "" else rest_dict["image_url"]

                add_restaurant (
                                session_token,
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
                                key,
                                *l
                                )

# TODO populate all reviews

#def add_reviews(app,session_token):



# TODO populate all Locations (tedious)

# TODO populate all food types
