import json
import requests
from pprint import pp

#serialize a json
#deserialize a json
#They are not perfect inverses

#Serialize
#dump() writes data to a file like object in json format
#open() in a try and except block with open() as
#dumps() write the data to string in join format

data =  {
        "user": 
        {
            "name": "Williams Williams",
            "age": 93
        }
    }

print(data["user"]["age"])

with open("data_file.json","w") as write_file:
    json.dump(data, write_file, indent=4)

json_str=json.dumps(data,indent=1)
print(json_str)

black_jack=(8,"Q")
encoded=json.dumps(black_jack)
decoded=json.loads(encoded)

print(type(black_jack))
print(type(decoded))

print(black_jack)
print(decoded)
print(tuple(decoded))


#deserislize example

response = requests.get("http://jsonplaceholder.typicode.com/todos")
todos=json.loads(response.text)
print(type(todos))
pp(todos[:10])

dict_new = {}

for item in todos:
  if item["completed"] == True:
    if item["userId"] not in dict_new.keys():     
        dict_new[item["userId"]] = 1 
    else:
        dict_new[item["userId"]] += 1 
     
print(dict_new)
