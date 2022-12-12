#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].

def make_it_big(number_list = []):
  for i in range(len(number_list)):
    if(number_list[i]) > 0:
      number_list[i] = "big"
  return number_list

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def count_positives(number_list = []):
  pos_count = 0
  for number in number_list:
    if number > 0:
      pos_count += 1
  number_list[-1] = pos_count
  return number_list

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10

def sum_total(number_list = []):
  sum = 0
  for i in number_list:
    sum += i
  return sum

#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5

def multiples(number_list = []):
  average = sum_total(number_list)/len(number_list)
  return average

#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

def length(list = []):
  return len(list)

#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
#
def minimum(number_list = []):
  if len(number_list) == 0:
    return False
  min = number_list[0]
  for i in number_list:
    if i < min:
      min = i
  return min

#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def maximum(number_list = []):
  if len(number_list) == 0:
    return False
  max = number_list[0]
  for i in number_list:
    if i > max:
      max = i
  return max

#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

def ultimateanalyze(list = []):
  dictionary = {
    "sumTotal":sum_total(list), 
    "average":multiples(list), 
    "minimum": minimum(list), 
    "maximum":maximum(list), 
    "length":length(list)
  }
  return dictionary

#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverse(number_list = []):
  for i in range(len(number_list)):
    if i < len(number_list)/2:
      temp = number_list[i]
      number_list[i] = number_list[len(number_list)-1-i]
      number_list[len(number_list)-1-i] = temp
  
#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

def ispalindrome(word = []):
  for i in range(len(word)):
    if i < len(word)/2:
      if word[i] != word[len(word)-1-i]:
        return False
  return True


#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def fizzbuzz():
  for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
      print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
      print("Buzz")
    elif i % 3 == 0 and i % 5 ==0:
      print("FizzBuzz")
    else:
      print(i)

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

def fibonacci(n):
  if n < 0:
    print("incorrect")
  elif n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)