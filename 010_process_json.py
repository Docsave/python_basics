import json
with open("009_data.json","r") as my_json:
    car = json.load(my_json)
    
print(car["brand"])

print(car.get("year"))

print(car["features"])

print(car["engine"]["horsepower"])

car["year"]=2025

car.update({"speed":"180 km/h"}),

car.update({"country":"Japan"})

del car["color"]

car.pop("model")
