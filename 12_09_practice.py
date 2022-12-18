#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def biggie(list):
  for i in range(len(list)):
    if list[i]>0:
      list[i]='big'
  return list

print(biggie([-1,3,5,-5]))
#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def positives(list): 
  count = 0
  for i in list:
    if i > 0:
      count += 1 
  list[len(list) - 1] = count
  return list

print(positives([-1,1,1,1]))
  

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10

def sumtotal(list):
  sum = 0
  for i in list:
    sum += i
  return sum 

print(sumtotal([1,2,3,4]))
#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5

def average(list):
  sum = 0
  for i in list:
    sum += i
  return sum/len(list)

print(average([1,2,3,4]))

#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

def length(list):
  return len(list)

print(length([1,2,3,4]))

#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(list): 
  return min(list)

print(minimum([1,2,3,4]))

#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(list): 
  return max(list)

print(maximum([1,2,3,4]))

#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

def ultimateanalyze(list):
  dict = {'sumtotal':0, 'average':0, 'minimum': list[0], 'maximum': list[0], 'length': len(list)}
  for i in list: 
    dict['sumtotal'] += i
    dict['average'] = dict['sumtotal']/len(list)
    if dict['minimum'] > i:
      dict['minimum'] = i
    if dict['maximum'] < i:
      dict['maximum'] = i
  return(dict)

print(ultimateanalyze([-2,4,-5,6,10,1,0]))

#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverse_list(list):
  for i in range(len(list) // 2):
    list[i], list[-1-i] = list[-1-i], list[i]
  return list
print(reverse_list([11,12,13]))
print(reverse_list([11,12,13,14,15,16]))

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

def isPalindrome(str):
 
    for i in range(0, (len(str)/2) ):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

print(isPalindrome('radar'))
print(isPalindrome('radix'))

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def fizzbuzz(): 
  for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0: 
      print("FizzBuzz")
    elif i % 3 == 0: 
      print("Fizz")
    elif i % 5 ==0:
      print("buzz")
    else:
      print(i)

fizzbuzz()

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.
def fibonacci(n): 
  if n == 0:
    return 0  
  elif n == 1:
    return 1  
  else:
    return ((n-1) + (n-2))

print(fibonacci(5))



