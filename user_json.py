# Fetching the required details from the user JSON data file

import json
import requests

# Getting the requests from the URL
response = requests.get("https://jsonplaceholder.typicode.com/users")

# Loading the JSON data
users = json.loads(response.text)
user3=[]
users_phonenumbers = {"id":None,"name":None,"phone":None}

# Iterating for all the users in the file
for item in users:
        users_phonenumbers={}
        users_phonenumbers["id"]=item["id"]
        users_phonenumbers["name"]=item["name"]
        users_phonenumbers["phone"]=item["phone"]

        # Appending the list with the required information
        user3.append(users_phonenumbers)

# Sorting the list by name ascending
users_sorted = sorted(user3, key=lambda x: x['name'] )
print(users_sorted)

# Writing the result with the required information to the JSON file
with open("filtered_user_file.json", "w") as data_file:
    json.dump(users_sorted, data_file, indent = 2)
