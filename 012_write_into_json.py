import json
student = {
        "id": 10,
        "name": "Idara",
        "gender": "male",
        "department": "pharmacology",
        "school": "uniport"
        }

with open("013_data.json","w") as my_file:
    json.dump(student, my_file)

print(student)

