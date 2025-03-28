import json
user = {
        "id": input("Enter ID: "),
        "first_name": input("Enter First Name: "),
        "last_name": input("Enter First Name: "),
        "email": input("Enter Email: "),
        "password": input("Enter Password: "),
        }

with open("015_register.json", "w") as my_file:
    json.dump(user, my_file)

