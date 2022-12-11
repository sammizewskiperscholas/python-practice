#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  
# For example sum_total([1,2,3,4]) should return 10

def sum_total(num_list):
    sum = 0
    for n in num_list:
        sum = sum + n
    return sum

print(sum_total([1,2,5,4]))