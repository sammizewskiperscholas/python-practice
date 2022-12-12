#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". 
# Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def change_posi_big(list):
    for index in range(len(list)):
        if list[index] >= 0:
            list[index] = "big"
    print(list)
 
change_posi_big([-1, 2, 3, -5, 10])


#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. 
# Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def count_posi_list(list):
    count = 0
    for index in range(len(list)):
        if list[index] > 0:
            count += 1
    print(count) 
    list[len(list)-1] = count
    print(list)

count_posi_list([-1, 1, 2 , 3, -2, 3, 2])         

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  
# For example sum_total([1,2,3,4]) should return 10

def sum_of_list(list):
    total = sum(list)
    print(total)
  
sum_of_list([1, 1, -1, 1, 1])


#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  
# For example multiples([1,2,3,4]) should return #2.5
def avg_of_list(list):
    avg = sum(list)/len(list)
    print(avg)
  
avg_of_list([1, 2, 3 , 4])


#Length - Create a function that takes a list as an argument and returns the length of the list.  
# For example length([1,2,3,4]) should return 4

def len_of_list(list):
    length = len(list)
    print(length)
  
len_of_list([1, 2, 3 , 4])


#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  
# If the passed list is empty, have the function return false. 
#  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def min_of_list(list):
    if len(list) == 0:
        print("false")
    else:
        minimum = min(list)
        print(minimum)

min_of_list([])
min_of_list([1, 2, 3, 4, -5])
#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  
# If the passed list is empty, have the function return false. 
#  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def max_of_list(list):
    if len(list) == 0:
        print("False")
    else:
        maxi = max(list)
        print(maxi)
    
max_of_list([])
max_of_list([1, 2, 3, 50])

#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

def list_to_dict(list):
    
    sumTotal = sum(list)
    average = sum(list)/len(list)
    minimum = min(list)
    maximum = max(list)
    length = len(list)
    dictionary = {"sumTotal":sum(list), "average":sum(list)/len(list), "minimum":min(list), "maximum":max(list), "length":len(list)}
    print(dictionary)

list_to_dict([1, 2, 3, 4, 5, 6])
print(list_to_dict)

#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  
# Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. 
# This challenge is known to appear during basic technical interviews.

def rev_of_list(list):
    list.reverse()
    print(list)

rev_of_list([1, 2, 3, 4])

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. 
# A string is said to be palindrome if the reverse of the string is the same as string.
#  For example, “radar” is a palindrome, but “radix” is not a palindrome.

def palindrome(word):
    word_reverse = word[::-1] 
    if word == word_reverse:
        print(word + " is palindrome")
    else:
        print(word + " is non palindrome")
   
palindrome("mom")
palindrome("moon")

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “” instead of the number.
def fizzbuzz(number):
    for number in range(1, 101):
        if number%3 == 0:
            print("Fizz")
        elif number%5 == 0:
            print("Buzz")
        else:
            number%3 == 0 and number%5 == 0
            print("FizzBuzz")
    print(number)

fizzbuzz(150)


#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, 
#starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

def fibonacci(num):
    if num < 2:
        return (num)
        print(num)
    else:
        return (fibonacci(num -1) + fibonacci(num -2))
        print(num)
fibonacci(5)