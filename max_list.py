
#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def max_list(list1):
     if list1 == []:
        return False
     else:   
        return max(list1)

max1 = print(max_list([1,2,3,4]))
max2 = print(max_list([-1,-2,-3]))
max3 = print(max_list([]))
