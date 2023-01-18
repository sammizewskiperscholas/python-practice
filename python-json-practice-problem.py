import requests
import json
from pprint import PrettyPrinter
import math


url = 'https://swapi.dev/api/people/?page=1'
response = requests.get(url)
new_response = response.json()
data = []

print(len(new_response["results"]))
total_pages =  math.ceil(new_response["count"] / len(new_response["results"]))
print(total_pages)

url = 'https://swapi.dev/api/people/?page='
for i in range(1, total_pages + 1):
    response = requests.get(url + str(i))
    new_response = response.json()
    data.append(new_response)
#print(data)
   
results_list = []
for pages in range(0, total_pages):
    results_list.extend(data[pages]["results"])


#1. Create a function that returns a list of all the names.
def list_of_names():
    names = []
    for each_name in results_list:
        names.append(each_name["name"])
    return names

#2. Create a function that counts the total number of males and females. Return both numbers
def total_gender():
    male_count = 0
    female_count = 0
    for each_gender in results_list:
        if each_gender["gender"] == "male":
            male_count += 1
        elif each_gender["gender"] == "female":
            female_count += 1
    return (male_count, female_count)

#3. Create a function that returns a list of all the characters that appear in more than x number of films. 
# Where 'x' is the number of films you are checking for and is passed into the function.
def char_films_count():
    char_films_list = []
    for each_char in results_list:
        char_films_list.append((each_char["name"],len(each_char["films"])))
    return char_films_list


#4. Create function that returns a tuple of the min, max, and avg height for all characters   
def char_height():
    char_ht_list = []
    total_ht = 0
    for each_char in results_list:
        char_ht_list.append(int(each_char["height"]))
    
    return (min(char_ht_list), max(char_ht_list), sum(char_ht_list) / len(char_ht_list))

#5. Create a function that accepts two arguements: eye color and hair color. Return a dictionary with the min, max, and avg height based on the parameters.
def eye_hair_dict_mod(eye_color, hair_color):
    eye_hair_dict = {}
    eye_hair_list = []

    for each_record in results_list:
        if each_record["eye_color"].strip() == eye_color and each_record["hair_color"].strip() == hair_color : 
            if each_record["height"].isnumeric(): 
                eye_hair_list.append(int(each_record["height"]))

    if eye_hair_list != []:
        if len(eye_hair_list) == 1:
            eye_hair_dict["eye_color"] = eye_color
            eye_hair_dict["hair_color"] = hair_color
            eye_hair_dict["min"] = eye_hair_list[0] 
            eye_hair_dict["max"] = eye_hair_list[0]
            eye_hair_dict["avg"] = eye_hair_list[0]
        else:
            eye_hair_dict["eye_color"] = eye_color
            eye_hair_dict["hair_color"] = hair_color
            eye_hair_dict["min"] = min(eye_hair_list) 
            eye_hair_dict["max"] = max(eye_hair_list)
            eye_hair_dict["avg"] = math.ceil(sum(eye_hair_list)/len(eye_hair_list))
    return eye_hair_dict
   
#Challenge 1: Get all of the response data into a list using a "While Loop" instead of a "For Loop"
#def response_list_using_while():
   # pass

print(list_of_names())

x, y = total_gender()
print(f"Male count = {x} and Female count = {y}")

print(char_films_count())

min, max, avg = char_height()
print(f"Minimum = {min} : Maximum = {max} : Aveage = {avg}")

print(eye_hair_dict_mod("blue","blond"))




