
#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def min_list(list1):
     if list1 == []:
        return False
     else:   
        return min(list1)

min1 = print(min_list([1,2,3,4]))
min2 = print(min_list([-1,-2,-3]))
min3 = print(min_list([]))
