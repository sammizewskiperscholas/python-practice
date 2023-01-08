#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list. 
# If the passed list is empty, have the function return false. 
# For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(num_list):
    if(len(num_list) == 0):
        return False
    else:
        min_value = min(num_list)
    return min_value
        

print(minimum([-1,-2,-3]))

