#Average - Create a function that takes a list as an argument and returns the average of all the values in the list. 
# For example multiples([1,2,3,4]) should return #2.5

def average(num_list):
    sum = 0
    count = 0
    for n in num_list:
        sum = sum + n
        count +=1
    average = sum/count
    return average

print(average([1,2,3,5]))