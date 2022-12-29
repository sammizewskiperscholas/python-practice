# Calculating the total, average and grade for the students in the student file and 
# writing the result to the JSON file

import json

# Read the JSON data from the JSON file
with open('studentfile.json', "r") as file:
    student = json.load(file)

student_list = []

for item in student:
    total = 0
    item1 = 0
    item1 = item["course"]["marks"]

    # Calculating the total marks
    for mark, value in item1.items():
       total += value
       
    item["course"]["total"] = total

    # Calculating the average 
    item["course"]["average"] = total/len(item1)
    
    # Assigning the grade based on the range of the marks
    if item["course"]["average"] > 75 and item["course"]["average"] < 100:
        item["course"]["grade"] = "A"
    elif item["course"]["average"] > 65 and item["course"]["average"] < 75:
        item["course"]["grade"] = "B"    
    elif item["course"]["average"] > 45 and item["course"]["average"] < 65:
        item["course"]["grade"] = "C"  
    else:
        item["course"]["grade"] = "F" 

    student_list.append(item)   

# Sorting the student list by the grade ascending
student_sorted = sorted(student_list, key = lambda x: x["course"]["grade"])   
print(student_sorted)

# Writing the result to the studentresult.json file 
with open("studentresult.json", "w") as file:
    json.dump(student_sorted, file, indent = 4) 
