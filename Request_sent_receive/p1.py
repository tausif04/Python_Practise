# How to make Get requests and Fetch Data

import requests

url='http://164.68.107.70:6060/api/v1/ReadProduct'

response=requests.get(url)

code=response.status_code


json_data=response.json()

header=response.headers


print(code)

print(json_data)

print(header)

