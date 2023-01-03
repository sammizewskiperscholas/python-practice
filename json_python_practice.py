import json
import requests
from pprint import pp

response = requests.get("http://jsonplaceholder.typicode.com/todos")

todos = json.loads(response.text)
print(type(todos))
print(todos)

for item in todos:
    print(item)

