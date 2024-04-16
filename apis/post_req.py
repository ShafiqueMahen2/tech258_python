import requests
import json

json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]}) # Turn dict into string
headers = {"Content-Type": "application/json"} # Tells the API what format the data will be in

# post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, json={"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
print(post_multi_req.json())

# data= -> Accepts a string (so we had to use json.dumps first)
# json= -> Accepts a Python Dictionary





