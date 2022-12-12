
#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverse_list(list1):
    left = 0
    right = len(list1) - 1
    while (left < right):
        temp = list1[left]
        list1[left] = list1[right]
        list1[right] = temp
        left+=1
        right-=1
    return list1

revlist1 = print(reverse_list([1,2,3,4,5]))
