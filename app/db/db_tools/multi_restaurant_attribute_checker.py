import json

with open("db/restaurants.json", "r") as f:
    d = json.load(f)

for e in d.keys():
    # Test for not having price in restaurants
    #try:
    #    i = d[e]["price"]
    #except KeyError:
    #    print("key ", e, "doesnt have price")

    # Test for not having zip - replaced with 78704
    #if d[e]["location"]["zip_code"] == "":
    #    print(e, "doesn't have a zip")

    # Test for categories - replaced with pizza
    if d[e]["categories"] == []:
        print(e, "doesn't have a category")
