# This script builds food_types.json from restaurants.json
import json

food_types = {}
with open("restaurants.json", "r") as restaurants_f:
    restaurants = json.load(restaurants_f)
    for key in restaurants.keys():
        l = restaurants[key]["categories"]
        for dicts in l:
            t = dicts["alias"] + "/" + dicts["title"]
            if not t in food_types:
                food_types[t] = []
            r = restaurants[key]
            r["key"] = key
            food_types[t].append(r)

with open("food_types.json", "w") as f:
    json.dump(food_types, f, indent=4)

cats = None
with open("food_types.json", "r") as f:
    cats = json.load(f)
    catNums = []
    for key in cats.keys():
        catNums.append((len(cats[key]), key))
    catNums = sorted(catNums)

    print("total cats", len(catNums))
    for t in catNums:
        print(t[0], t[1])
