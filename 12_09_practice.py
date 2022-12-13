# these lists come into play a lot below
numbers = [4, 0, 5, 10, 99, -4]
more_numbers = [0, -2, -5, 5, -99]

#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". 
# Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def make_it_big(assortment):
    new_assortment = []
    for item in assortment:
        if item <= 0:
            new_assortment.append(item)
        else: 
            new_assortment.append("big")
    return new_assortment
print(make_it_big(numbers))

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. 
# Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def end_count(assortment):
    new_assortment = []
    count = 0
    for item in assortment:
        if item <= 0:
            pass
        else: 
            count += 1
    assortment[-1] = count
    return assortment
print(end_count(numbers))

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  
# For example sum_total([1,2,3,4]) should return 10
def sumTotal(assortment):
    total = 0
    for item in assortment:
        total += item
    return total
print(sumTotal(numbers))

#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  
# For example multiples([1,2,3,4]) should return #2.5
def average(assortment):
    result = (sum(assortment))/(len(assortment))
    return result
print(average(numbers))

#Length - Create a function that takes a list as an argument and returns the length of the list.  
# For example length([1,2,3,4]) should return 4
def length(assortment):
    result = len(assortment)
    return result
print(length(numbers))

#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  
# If the passed list is empty, have the function return false.  
# #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum(assortment):
    if len(assortment) < 1:
        return False
    else:
        assortment.sort()
        minimum = assortment[0]
        return minimum
print(minimum(more_numbers))

#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  
# If the passed list is empty, have the function return false.  
# #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def maximum(assortment):
    if len(assortment) < 1:
        return False
    else:
        assortment.sort(reverse=True)
        maximum = assortment[0]
        return maximum
print(maximum(more_numbers))

#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the 
# sumTotal, average, minimum, maximum and length of the list.
def ultAn(assortment):
    ultAn={}
    if len(assortment) < 1:
        return False
    else:
        assortment.sort()
        ultAn["minimum"] = assortment[0]
        assortment.sort(reverse=True)
        ultAn["maximum"] = assortment[0]
        ultAn["length"] = len(assortment)
        ultAn["sumTotal"] = 0
        for item in assortment:
            ultAn["sumTotal"] += item
        ultAn["average"] = (sum(assortment))/(len(assortment))
    return ultAn
print(ultAn(numbers))

#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  
# Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. 
# This challenge is known to appear during basic technical interviews.
def ReverseList(assortment):
    assortment2 = assortment[::-1]
    return assortment2
print(ReverseList([1,2,4,6,5]))

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. 
# A string is said to be palindrome if the reverse of the string is the same as string. 
# For example, “radar” is a palindrome, but “radix” is not a palindrome.
def Ispalindrome(assortment):
    if assortment[::-1] == assortment[::1]:
        return True
    else:
        return False
print(Ispalindrome("radar"))
print(Ispalindrome("radix"))

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.
def fizzBuzz():
    numbers = []
    for i in range (1,101):
        if i % 3 == 0:
            if i % 5 == 0:
                numbers.append("FizzBuzz")
            else:
                numbers.append("Fizz")
        elif i % 5 == 0:
            numbers.append("Buzz")
        else:
            numbers.append(i)
    return numbers
print(fizzBuzz())

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.
def F(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return F(n - 1) + F(n - 2)
    else: 
        return "That's not a positive number. Give me a positive number."
print(F(10))
