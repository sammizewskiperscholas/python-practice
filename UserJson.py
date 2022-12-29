# Fetching only the specified field(id,name and phone) from JSON Data  

import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = json.loads(response.text)

print(type(users))

print(users[:1])

user3=[]
users_phonenumbers = {"id":None,"name":None,"phone":None}

for item in users:
        users_phonenumbers={}
  
        users_phonenumbers["id"]=item["id"]
        users_phonenumbers["name"]=item["name"]
        users_phonenumbers["phone"]=item["phone"]
 
        user3.append(users_phonenumbers)
print(user3)


orderby_users = sorted(user3, key=lambda x: x['name'])
print(orderby_users)
with open("users.json","w") as file:
    
    json.dump(orderby_users,file,indent=4)
