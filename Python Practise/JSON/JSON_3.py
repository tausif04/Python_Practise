#Write JSON String to a File

import json
#python dictionary
person={
    "name":"John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer","programmer"]
}

with open('person.json','w') as json_file:
    json.dump(person,json_file)