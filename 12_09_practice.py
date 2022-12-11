#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].

def make_big(lst):
  return ["big" if el > 0 else el for el in lst ]

print(make_big([-1, 3, 5, -5]))

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def add_number_positives(lst):
  lst[len(lst)-1] = len([i for i in lst if i>0])
  return lst

print(add_number_positives([-1,1,1,1]))

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10

def sum_total(lst):
  return sum(lst)

print(sum_total([1,2,3,4]))

#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5

def get_avg(lst):
  return sum(lst)/len(lst)

print(get_avg([1,2,3,4]))

#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

def get_length(lst):
  return len(lst)

print(get_length([1,2,3,4]))

#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def get_minimum(lst):
  return False if len(lst) == 0 else min(lst)

  
print(get_minimum([1,2,3,4]), get_minimum([-1,-2,-3]))
#
#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def get_maximum(lst):
  return False if len(lst) == 0 else max(lst)
  
print(get_maximum([1,2,3,4]), get_maximum([-1,-2,-3]))

#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

def ultimateanalyze(lst):
  dct = {}
  dct['sumTotal'] = sum(lst)
  dct['average'] = sum(lst)/len(lst)
  dct['minimum'] = min(lst)
  dct['maximum'] = max(lst)
  dct['length'] = len(lst)
  return dct

print(ultimateanalyze([1,2,3,4]))
  
#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverselist(lst):
  return lst[::-1]

print(reverselist([1,2,3]))
#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

def ispalindrome(lst):
  return lst == lst[::-1]
        
print(ispalindrome('abba'))
#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
#If the number is a multiple of 3, print “Fizz” instead of the number.
#If the number is a multiple of 5, print “Buzz” instead of the number.
#If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def fizzbuzz():
  p = lambda x: print(x)

  [p('FizzBuzz') if (i%3==0 and i%5==0) 
  else (p('Fizz') if i%3==0 
  else ( p('Buzz') if i%5==0 else p(i)))
  for i in range(1,101)]
 
fizzbuzz()
   
#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

def fibonacci(n):
  if n == 0: return 0
  dct_fibo = {}
  dct_fibo[0] = 0
  dct_fibo[1] = 1
  for i in range(2,n+1):
    dct_fibo[i] = dct_fibo[i-1] + dct_fibo[i-2]
  return [values for _, values in dct_fibo.items()]

print(fibonacci(10))