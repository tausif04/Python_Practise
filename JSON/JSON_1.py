#Convert Python Object into a JSON String

import json
# Python dictionary
person={
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}
# Convert Python dictionary to JSON string
person_json=json.dumps(person,indent=4)
print(person_json)
