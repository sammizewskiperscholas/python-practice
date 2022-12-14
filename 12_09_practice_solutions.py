#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def make_it_big(list):

    for x in list:
        if x > 0:
            list.append("big")
    return list

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def count_positives(list):
  count = 0
  for x in list:
    if x > 0:
      count += 1
  list[len(list-1)] = count
  return list


#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10
def sumtotal(list):
  sum = 0
  for x in list:
    sum += x
  return sum


#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5

def average(list):
  sum = 0
  for x in list:
    sum +=1
  return (sum/len(list))


#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

def length(list):
  return len(list)  
    
#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(list):
  if len(list)<0:
    return False
  minint = list[0]
  for x in list:
    if x<minint:
      minint = x
  return minint

#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(list):
  if len(list)<0:
    return False
  maxint = list[0]
  for x in list:
    if x<maxint:
      maxint = x
  return maxint



#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

def ultimateanalyze(list):
  dict={}


#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverselist(list):
  return list[::-1]


#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
def ispalindrome(string):
    new_string = string[::-1]
    if string  == new_string:
        return True
    return False
 
print(ispalindrome(string))

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.
def fizzbuzz(list):
  list = []
for x in range(1,101):
    if x % 3 == 0:
        list.append("Fizz")
    elif x % 5 == 0:
        list.append("Buzz")
    elif x%3==0 and x %5==0:
        list.append("FizzBuzz")

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.