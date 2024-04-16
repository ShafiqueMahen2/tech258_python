import requests

postcodes_req = requests.get("https://api.postcodes.io/postcodes/SE120NB")
# print(postcodes_req.status_code)
# print(postcodes_req.headers)
# print(type(postcodes_req.content))
# print(postcodes_req.json())

data_dict = postcodes_req.json()["result"] # Widest dictionary removed (status code)
print(data_dict["region"])