# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def big_size(L):

    for i in range(len(L)):
        if (L[i] >= 0):
            L[i] = 'big'
    return L


print(big_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).


def positive(L):
    counter = 0
    last = len(L)
    for i in range(len(L)):
        if (L[i] > 0):
            counter += 1

    L[last-1] = counter
    return L


print(positive([-1, 1, 1, 1]))

print(positive([-1, 1, 1, 3]))


# SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10
def sumTotal(list1):
    sum = 0
    for val in list1:
        sum = sum+val
    return sum
    # for i in range(len(list1))
    #    sum=sum+list[i]
    # return sum


print(sumTotal([1, 2, 3, 4]))


# Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5
def avg(list1):
    sum = 0
    for val in list1:
        sum += val
    return (sum/len(list1))


print(avg([1, 2, 3, 4]))


# Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

def len_list(list1):
    result_length = (len(list1))
    return result_length


print(len_list([1, 2, 3, -4]))
print(len_list([]))

# Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.


def min_value(list1):
    min = list1[0]
    for val in list1:
        if (val < min):
            min = val
    return min


print(min_value([1, 2, -3, 4]))
# Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.


def max_value(list1):
    if len(list1) < 0:
        return False
    maxval = list1[0]
    for val in list1:
        if (val > maxval):
            maxval = val
    return maxval


print(max_value([1, 2, 3, 4, -4]))

# Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.


def ultimateanalyze(list1):
    list2 = {'sumTotal': 0, 'average': 0,
             'minimum': list1[0],  'maximum': list1[0], 'length': len(list1)}
    sum = 0
    for val in list1:

        sum = sum+val
        if val < list2['minimum']:
            list2['minimum'] = val
        if val > list2['maximum']:
            list2['maximum'] = val

    list2['sumTotal'] = sum
    list2['average'] = sum/len(list1)

    return list2


print(ultimateanalyze([1, 2, 3, 4]))


# ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverselist(list):
    length = len(list)
    for i in range(length//2):
        print(i)
        tmp = list[i]
        list[i] = list[length-i-1]
        list[length-i-1] = tmp
    return list


print(reverselist([1, 2, 3, 4, 5]))


# Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

def palindrome(str1):
    reversestr = str1[::-1]
    if (reversestr == str1):
        return "palindrome"
    else:
        return 'not palindrome'


print(palindrome('saas'))
print(palindrome('sbas'))


# Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
# If the number is a multiple of 3, print “Fizz” instead of the number.
# If the number is a multiple of 5, print “Buzz” instead of the number.
# If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif (i % 5 == 0):
            print("buzz")
        elif (i % 3 == 0):
            print("fizz")
        else:
            print(i)


print(fizzbuzz())


# Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Create a function that accepts any number and will create a sequence based on the fibonacci sequence.
def fibonacci(num):
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)


num = int(input("enter number: "))
for i in range(num):
    print(fibonacci(i))
