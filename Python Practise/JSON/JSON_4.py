#Read JSON String from a file
import json
with open('person.json','r') as json_file:
    person=json.load(json_file)

print(person)