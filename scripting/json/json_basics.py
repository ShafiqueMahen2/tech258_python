import json

car_data = {
    "name": "tesla",
    "engine": "electric"
}

print(type(car_data))

# json.dumps() --> serialises JSON to a formatted string

car_data_json_string = json.dumps(car_data)
print(car_data_json_string)

# json.dump() --> Creates a stream object and expects a file object to write to

with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)

