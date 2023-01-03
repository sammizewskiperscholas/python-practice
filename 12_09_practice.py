#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#  Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].

def make_it_big(list1):
  for index,element in enumerate(list1):
    if element >= 0:
      list1[index] = "big"

  return list1


change_result = make_it_big([-1,3,5,-5])
print(change_result)

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. 
# Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def count_positives(list1):
  count = 0
  for i in list1:   
    if i > 0:
      count += 1
  list1[-1] = count
  return list1

result = count_positives([-1,1,1,1])
print(result)


#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  
# For example sum_total([1,2,3,4]) should return 10

def sum_total(list1):
  sum = 0
  for i in list1:
    sum += i
  return sum

sum_result = sum_total([1,2,3,4])    
print(sum_result)

#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  
# For example multiples([1,2,3,4]) should return #2.5

def avg_value(list1):
  sum = 0
  for i in list1:
    sum += i
  return sum/len(list1)

sum_result = avg_value([1,2,3,4])    
print(sum_result)


#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

def length_of_list(list1):
  return len(list1)

result = length_of_list([1,2,3,4])
print(result)

#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list. 
#  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1;
#  minimum([-1,-2,-3]) should return -3.

def minimum(list1):
  if len(list1) == 0:
    return False
  else:
    min_value = list1[0]
    for i in range(1,len(list1)):
      if min_value > list1[i]:
        min_value = list1[i]
    return min_value    

a =minimum([1,2,3,4])    
print(a)


#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  
# If the passed list is empty, have the function return false.  
# #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(list1):
  if len(list1) == 0:
    return False
  else:
    max_value = list1[0]
    for i in range(1,len(list1)):
      if max_value < list1[i]:
        max_value = list1[i]
    return max_value    

a =maximum([1,2,3,4])    
print(a)



#Ultimateaalyze - Create a function that takes a list as an argument 
# and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

def list_content(list1):
  if len(list1) == 0:
    return False
  else:
    d = {}
    d["sum"] = sum_total(list1)
    d["average"] = avg_value(list1)
    d["minimum"] = minimum(list1)
    d["maxmimum"] = maximum(list1)
    d["length"] = length_of_list(list1)
    return d

a = list_content([-1,2,0,-8,0,6])
print(a)



#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  
# Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. 
# This challenge is known to appear during basic technical interviews.

def reverse_list(list1):
   list1 = list1[::-1]
   return list1
  

a = reverse_list([1,2,3,4])
print(a)



#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. 
# A string is said to be palindrome if the reverse of the string is the same as string. 
# For example, “radar” is a palindrome, but “radix” is not a palindrome.

def palindrome(string1):
  if(string1 == string1[::-1]):
    print("The given string is Palindrome")
  else:
    print("The given string is not a Palindrome")  

palindrome("radax")    

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def fizzbizz():
  for i in range(1,101):
    if (i%3 == 0) and (i%5 == 0):
      print(i , "FizzBuzz")
    elif i%3 == 0:
      print(i, "Fizz")
    elif i%5 == 0:
      print(i, "Buzz")
    else: 
      print(i)
fizzbizz()


#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
#  such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

def fibonacci(n):
  first = 0
  second = 1

  for i in range(n):
    print(first)
    third = first + second
    first = second
    second = third

number_for_fibo = int(input("Enter Number : "))
fibonacci(number_for_fibo)




