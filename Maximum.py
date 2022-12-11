#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list. 
# If the passed list is empty, have the function return false. 
# For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(num_list):
    if(len(num_list) == 0):
        return False
    else:
        max_value = max(num_list) 
    return max_value

print(maximum([-1,2,3]))
