import json
import zipcodes

mega = {}
latlons = {}
count = 0
for zipcode in zipcodes.zipCodes:
    s = str(zipcode) + ".json"
    print(s)
    with open(s, "r") as f:
        zip_data = json.load(f)
    for key in zip_data.keys():
        latlon = (zip_data[key]["coordinates"]["latitude"], zip_data[key]["coordinates"]["longitude"])
        if not latlon in latlons:
            mega[count] = zip_data[key]
            latlons[latlon] = True
            count += 1

with open("mega.json", "w") as f:
    json.dump(mega, f, indent=4)
