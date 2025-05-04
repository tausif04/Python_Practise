#How to post data to server

import requests

url='http://164.68.107.70:6060/api/v1/CreateProduct'

payload={
    "ProductName":"Demo",
    "ProductCode":"2113131",
    "Img":"abc",
    "UnitPrice":"12",
    "Qty":"1",
    "TotalPrice":"12"
}

header={
    "Content-Type": "application/json"
}

response=requests.post(url=url,json=payload,headers=header)

code=response.status_code


json_data=response.json()

header=response.headers


print(code)

print(json_data)

print(header)

