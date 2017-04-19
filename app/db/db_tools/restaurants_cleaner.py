# The purpose of this file is to clean out elements in a restaurants json
# that are not strictly restaurants using a list of manually selected
# categories that don't fit our criteria, e.g bookstores

from __future__ import print_function
import json
import codecs

rejects_ids = []
m = {}
new_mega = {}
rejects_list = []

with open("mega.json", "r") as mega:
    m = json.load(mega)
    with open("rejects.txt", "r") as r:
        rejects_list = list(r.read().splitlines())

    for key in m:
        flag = True
        for cat in m[key]["categories"]:
            alias_title = cat["alias"] + "/" + cat["title"]
            if alias_title in rejects_list:
                rejects_ids.append(key)
                flag = False
                break
        if flag:
            new_mega[key] = m[key]


with open("deleted_from_mega.txt", "w") as dfm:
    print("len mega", len(m))
    print("len new mega", len(new_mega))
    print("deleted", len(rejects_ids), "restaurants")
    for e in rejects_ids:
        s = e + "," + m[e]["name"] + ","
        print(s, end="")
        dfm.write(s.encode('utf-8'))
        for cat in m[e]["categories"]:
            s = cat["title"] + ","
            print(s, end="")
            dfm.write(s.encode('utf-8'))
        print("")
        dfm.write("\n")

with open("new_mega.json", "w") as n_m:
    json.dump(new_mega, n_m, indent=4)
