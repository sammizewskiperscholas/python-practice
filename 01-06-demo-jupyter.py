1. Create a function that returns a list of all the names.
2. Create a function that counts the total number of males and females. Return both numbers
3. Create a function that returns a list of all the charachters that appear in more than x number of films. Where 'x' is the number of films you are checking for and is passed into the function.
4. Create function that returns a tuple of the min, max, and avg height for all charachters
5. Create a function that accepts two arguements: eye color and hair color. Return a dictionary with the min, max, and avg height based on the parameters.

Challenge 1: Get all of the response data into a list using a "While Loop" instead of a "For Loop"
Challenge 2: For problem number 4, convert the centimeters to feet
Challenge 3: Create a function that returns a list of all the names that start with a certain letter.





We have an endpoint with 82 people records We have 10 records per page We have 9 total pages

We have a base url: https://swapi.dev/api/people/?page=

import requests
import json 
from pprint import pp
We need to get all of the pages into one Python List.

Psuedo-Code

I want to make a for loop that loops through every page -I need to increase the page number of the URL by 1 every time I move through the loop -pagenum + 1 -pagenum + i
Concept: I need to extract the data I am looking for into a data structure (list) -need to create a list

Make a get request -I need to save the response to the request in a variable

Need to turn our response into a data type we can use later .loads() .json()

.append the converted response into the list

WAIT!

Before we even mess with the loop.....let's make sure we can do it for one page

url= 'https://swapi.dev/api/people/?page=1'

response= requests.get(url)

r= response.json()

pp(r)
=======================================================================================

We are now going to try to get all of the pages.


baseurl= 'https://swapi.dev/api/people/?page='
total_pages= 9

#I need to perform my get request, 9 times. 
#I want to use a for loop to do that. 

#I can hardcode the values in a for loop, by setting the range with integers
#for i in range(1, 10)
data= []

for i in range(1, total_pages+1):
    response= requests.get(baseurl + str(i))
    #'https://swapi.dev/api/people/?page=1'
    #'https://swapi.dev/api/people/?page=2'
    #'https://swapi.dev/api/people/?page=3'
    new_response= response.json()
    data.append(new_response)

pp(data)
============================================================================================


We now have everything in one list!

But there are keys that we do not need for the questions that are being asked.

Let's get the values of the results keys in one list.

We need to loop through the list. Then you call the key for that list index, in this case it is the 'result' key We want to store it in a seperate list so all of have left to work with is our charachter data.

#Checking to see how to get the information that we want.
print(data[0]['results'])

cleaned_data= []

for list_page in data:
    #print(list_page)
    #print(data[i])
    pass
    for values in list_page['results']:
        #print(values)
        pass

#print(cleaned_data)

for num in range(0, 9):
    results= data[num]['results']
    cleaned_data.extend(results)

print(cleaned_data)

============================================================================================





