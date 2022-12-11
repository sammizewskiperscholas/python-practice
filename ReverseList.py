#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order. 
# Do this without creating a empty temporary list. 
# For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverse(num_list):
    reverse_list = sorted(num_list, reverse=True)
    return reverse_list

print(reverse([1,2,3,4]))