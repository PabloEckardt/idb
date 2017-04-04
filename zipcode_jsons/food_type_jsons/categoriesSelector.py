import json


food_types = {}
l = []
with open ("food_type.json", "r") as ft:
    food_types = json.load(ft)
    for key in food_types:
        print (key + "?")
        i = raw_input()
        if i == 'n':
            l.append(key)
        elif i == "y":
            pass

for e in l:
    print (e)

with open("rejects.txt", "w") as f2:
    for e in l:
        f2.write(e+"\n")
