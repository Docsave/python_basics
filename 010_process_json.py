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

with open("011_new_data.json","w") as new_data:
    json.dump(car,new_data)
print(len(car))

print(car.keys())

print(car.values())

print(car.items())

for a in car:
    print(a)

for a in car.items():
    print(a)
