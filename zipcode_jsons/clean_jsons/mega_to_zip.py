import json

mega = {}
with open("one2oneMega.json", "r") as f:
    mega = json.load(f)

zips = {}

for r in mega.keys():
    curr_zip = mega[r]["location"]["zip_code"]
    #print(curr_zip)
    if curr_zip != "":
        if not curr_zip in zips.keys():
            zips[curr_zip] = {r: mega[r]}
        else:
            zips[curr_zip][r] = mega[r]

with open("locations.json", "w") as f:
    json.dump(zips, f, indent=4)
