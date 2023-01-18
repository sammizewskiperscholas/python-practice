import requests
import json
from pprint import pprint

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
r=response.json()

print(response.json())
print(r)
pprint(r)
print(response.status_code)
print(response.headers)
pprint(response.headers["Content-Type"])


#POST requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.status_code)
print(response.json())

#alternate method
headers = {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
response.json()


todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
response.json()
print(response.status_code)

#some extra response requests posted by sammi on the zoom chat
response = requests.get("https://api.open-notify.org/astros.json")
response = requests.get("http://api.open-notify.org/astros.json")
response = requests.get("http://api.open-notify.org/astros.json")

#{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}