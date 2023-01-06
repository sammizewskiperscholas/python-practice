# JSON : Java Script Object Notation
#python package for encoding decoding json

#The process of encoding JSON is called serialization. this means transformation of data into series of bytes
#Deserialization is the reciprocal process of decodind data that has been stored or deliverd in JSON standard

import json
import requests
from pprint import pp

#serialization
data = {
        "precident" : {
                "name:" : "Zaphord Beeblebrox",
                "spicies:" : "Betelgqusian"
                    }
        }

json_string = json.dumps(data,indent=4)

# print(json_string)

#deserialize
black_jack=(8,"Q")
encoded_jack=json.dumps(black_jack)          #tuple stored as array in json
decoded_jack=json.loads(encoded_jack)        #array returned as list in python
# print(type(black_jack))
# print(type(encoded_jack))
# print(type(decoded_jack))                     #array returned as list in python


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
todos=response.json()
# print(type(todos))
# pp(todos[:10])


#which users has copleted most task

#map of userid to number of complete todos for that user
todos_by_user={}
for todo in todos:
    if todo['completed']:
        todos_by_user[todo['userId']] = todos_by_user.get(todo['userId'],0)+1

print(todos_by_user)
top_users= sorted(todos_by_user.items(), key=lambda x: x[1],reverse=True)
print(top_users)

max_complete=top_users[0][1]

#create a list of users who have completed max number of todos
users=[]
for user,num_completed in top_users:
    if num_completed < max_complete:
        break
    users.append(str(user))
max_users=" and ".join(users)              #users who completed max TODOS
s='s' if len(users) > 1 else ""
print("user{} {} completed {} TODOS".format(s,max_users,max_complete))

#create json file that contains the completed todos for each user who completed the max number of TODOS

#define function to filter out completed todos of user with max completed TODOS
def keep(todos):
    is_complete=todos['completed']
    hax_max_count= str(todos["userId"]) in users
    return is_complete and hax_max_count

#Write filtered TODOS to file
filtered_todos=list(filter(keep,todos))
# pp(filtered_todos)
with open("jsonph_filterd_data_file.json","w") as file:
     json.dump(filtered_todos,file,indent=4)





       





