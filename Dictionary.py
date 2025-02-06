student={
    "name": "Alice",
    "age":"23",
    "major":"cs"
}

print(student)
print(student["name"])
print(student.get("age"))
print(student.get("name"))
# Returns a view object containing the dictionary's keys
print(student.keys())
#Returns a view object containing the dictionary's values
print(student.values())
#Returns a view object containing the dictionary's key-value pairs.
print(student.items())
#Uddate the dictionary with the specified key-value pairs
student.update({"age":24,"graduated": True})
print("After Upadating", student)