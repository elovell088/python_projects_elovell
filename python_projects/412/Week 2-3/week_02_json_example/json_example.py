#IT 412 - Eric Lovell - JSON Practice Lecture Assignment

import json

#How to open and load a JSON file, then print its contents
with open("text_files/config.json") as json_obj:
    config_data = json.load(json_obj)

print(config_data)

#How to print out one element of the json file
print(config_data["memory"])
print(config_data["appfolder"])

#How to modify the contents of a json file
config_data["memory"] = "100mb"
print(config_data)

#How to modify the contents and write it to the original json file
with open("text_files/config.json", "w") as json_obj:
    json.dump(config_data, json_obj)