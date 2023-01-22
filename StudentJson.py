import json


with open("studentfile.json","r") as file:
    student_data = json.load(file)
print(student_data)

print(type(student_data))

print(student_data[0])

student_dict = {}
student_list=[]

for item in student_data:
    tamil=item['course']['marks']['tamil']
    english=item['course']['marks']['english']
    computer=item['course']['marks']['computer']
    total = tamil+english+computer
    item['course']["total"]=total
    item['course']["average"]=total/3
    item["total"]=total
    item["average"]=total/3
    student_list.append(item)
    if item['course']['average'] > 75 and item['course']['average'] < 100:
        item['course']['grade']="A"
    elif item['course']['average'] >65 and item['course']['average'] < 75:
        item['course']['grade']="B"
    elif item['course']['average'] >45 and item['course']['average'] < 65:
        item['course']['grade']="C"
    else:
        item['course']['grade']="Fail"

    student_list.append(item)

print(student_list)

sorted_student_list=sorted(student_list, key= lambda x: x['course']['grade'])
print(sorted_student_list)

with open("student_result.json","w") as student_file:
    json.dump(sorted_student_list,student_file,indent=4)
   