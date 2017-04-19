# This script will remove the retaurants from restaurants.json
# that don't have a review in reviews.json

import json

with open("restaurants.json", "w") as new_mega:
    new = {}
    with open("new_mega.json", "r") as old_mega:
        old = json.load(old_mega)
        with open("reviews.json", "r") as reviews:
            r = json.load(reviews)

            print("len old", len(old))
            l1 = len(old)
            count = 0
            for key in r:
                if key in old:
                    count += 1
                    new[key] = old[key]

            l2 = len(new)
            print("len new", len(new))
            print("count is:", count, "diff", l1 - l2)
        json.dump(old, new_mega, indent=4)
