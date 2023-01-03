import json
import requests
from pprint import pp

#serialize a json, encoding data into json format
#deserialize a json, decoding into another format

### !!!! They are NOT perfect inverses !!!!! #####
#
#
#Serialize 
#dump() write data to a file like object in json format
#open() in a try and except block
#with open() as

#dumps() write the data to string in json format

data= {
    "user": {
        "name": "William Williams",
        "age": 93
    }
}

# print(data["user"]["age"])

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent= 4)


json_str=json.dumps(data, indent=4)
print(json_str)

#lets check and se

blkjk_hand= (8, "Q")
encoded = json.dumps(blkjk_hand)
decoded= json.loads(encoded)

print(type(blkjk_hand))
print(type(decoded))
print(blkjk_hand ==tuple(decoded))

##deserializatation example
response = requests.get("http://jsonplaceholder.typicode.com/todos")
todos= json.loads(response.text)

#print(type(todos))
pp(todos[:10])


#see who has the most completed items 
#we are going to need to loop through list to check all the todos
#we need to count all the items
#have a place to track and store the number of completed todos, by thu user
todos_by_user={}
for item in todos:
    if item["completed"] == True and item["userId"] not in todos_by_user:
        if item["userID"] not in todos_by_user.keys():
            todos_by_user[item["userId"]] = 1
        else: 
            todos_by_user[item["userId"]] += 1

print(todos_by_user)

#with the code above, we have created a new dictionary that has all of the users with completed
#and the total number of tasks they created

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users)
max_complete= top_users[0][1]

#with the code above we are sorting by the values due to the lambda function sorting at x[1] from high to low

### Final Goal is to tell s in a string who are the users that have the highest number of todos completed with thei user ids 4
stars = [x for x, y in top_users if y == max_complete]

stars2 = []
for users, value in top_users: 
    if value == max_complete:
        stars2.append(users)
print(stars)
print(stars2)


#"Users {} completed {this many} TODOS"

print("User(s) {} completed TODOs".format(user))



