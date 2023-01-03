

count = 0
todos_by_user ={}
for item in todos:
    print(item)
    if item["completed"] == True:
        count += 1
        todos_by_user[item["userId"] ]= count
print(count)
print(todos_by_user)
