# print total number of detaails
# print languages of ukrane
# print currency of china
# print population of india
# print neighbouring countries of australia
import json

with open("countries.json",encoding="utf-8") as f:
    data = json.load(f)
print(len(data))

def get_country_data(country_name):

    return [country for country in data if country["name"].lower().startswith(country_name)]

# countrylang=[country["languages"] for country in data if country["name"]=="Ukraine"]
# print(countrylang)


currency_det=[country["currencies"]for country in data if country["name"].startswith("Palestine")]
print(currency_det)

curr_name=[details.get("name")for details in currency_det[0]]
print(curr_name)


india_data=get_country_data("india")
print(india_data[0].get("borders"))

country_borders=india_data[0].get("borders")

neighbouring=[country["name"] for country in data if country["alpha3Code"] in country_borders ]
print(neighbouring)

print(max(data,key=lambda p:p["population"])["name"])

print(min(data,key=lambda p:p["population"])["name"])