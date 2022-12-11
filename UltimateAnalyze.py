#Ultimate_analyze - Create a function that takes a list as an argument and returns a dictionary
# that has the sumTotal, average, minimum, maximum and length of the list.






def sumTotal(num_list):
    sum = 0
    for n in num_list:
        sum = sum + n
    return sum

def average(num_list):
    sum = 0
    count = 0
    for n in num_list:
        sum = sum + n
        count +=1
    average = sum/count
    return average

def minimum(num_list):
    if(len(num_list) == 0):
        return False
    else:
        min_value = min(num_list)
    return min_value

def maximum(num_list):
    if(len(num_list) == 0):
        return False
    else:
        max_value = max(num_list) 
    return max_value

def length(num_list):
     return(len(num_list))

   

def ultimate_analyze(num_list):
    dict = {}
    
    dict['sumTotal'] = sumTotal(num_list)
    dict['average'] = average(num_list)
    dict['minimum'] = minimum(num_list)
    dict['maximum'] = maximum(num_list)
    dict['length'] = length(num_list)
    return dict


print(ultimate_analyze([1,2,3,4,5,6]))
