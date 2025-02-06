#Convert JSON String to Pyhton Object
import json

# JSON string
person_json = '{"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}'

# Parse JSON string into a Python dictionary
person_dict = json.loads(person_json)

# Accessing data
print(person_dict)
print("Name:", person_dict["name"])
print("Age:", person_dict["age"])
print("City:", person_dict["city"])
print("Has Children:", person_dict["hasChildren"])
print("Titles:", person_dict["titles"])
