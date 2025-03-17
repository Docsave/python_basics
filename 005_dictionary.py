student_info = {
        "name":"Saviour",
        "age":30,
        "grade":"c",
        "subject":["maths","physics","chemistry"],
        "address":{"city":"Port-Harcourt","country":"Nigeria"}
        }
        
print(student_info["name"])

print(student_info.get("age"))

print(student_info["subject"])

print(student_info["address"])

student_info["grade"] = "A"
print(student_info)

student_info.update({"GPA":4.5})
print(student_info)

student_info.update({"age":40, "school":"OAU"})
print(student_info)

del student_info["GPA"]
print(student_info)

age = student_info.pop("age")
print(student_info)

print(len(student_info))

print(student_info.keys())

print(student_info.values())

for keys in student_info:
    print(keys)

for keys, values in student_info.items():
    print(keys, values)
