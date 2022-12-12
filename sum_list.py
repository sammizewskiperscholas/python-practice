
#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10
def sumlist(lista):
    sumtotal = 0
    for i in lista:
        sumtotal = sumtotal + i
    return sumtotal
a = print(sumlist([1, 2, 3,4]))