import json
import sys
import io

if __name__ == "__main__":
    name = "food_type.json"
    with open(name, 'r') as data_file:
        data = json.load(data_file)
    resultFile = open("keys.txt", 'w')
    for k in data.keys():
        resultFile.write(k)
        resultFile.write("\n")
