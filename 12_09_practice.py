#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].

def make_it_big(lst):
    """Function to change all positive numbers in the list to word "big." """
    
    for index,number in enumerate(lst):
        if number >= 1:                       # check if number is positive
            lst[index]="big"                  #assigning "big" to positinve number in the list   
    return lst

print(make_it_big([-1,3,5,-5]))    

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def count_positives(lst):
  """ Function to replace last value in the list with number of positive values in the list"""
  count=0                     # counter to count number of positive values
  for number in lst:
    if number >= 1:           # cheking if number is positive
      count+=1
  if count > 1:
    lst[-1]=count             # replacing last value in the list with total number of positive values in the list
  return lst

print(count_positives([-1,1,1,1]))    

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10

def sum_total(lst):
  """Function to calculate sum of all values in the list"""
  total = 0
  for number in lst:
    total += number           # calculating sum 
  return total                # returning sum of all values in the list
 
print(sum_total([1,2,3,4]))   #calling sum_total function to get the sum of all the values in the list


#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5

def average(lst):
  """Function to calculate average of all the values in the list"""
  result = 0                
  count = 0                    #counter to count number of values
  for num in lst:
    result += num              # calculating sum
    count += 1
  return result/count          #average = sum of all the values /number of values

print(average([1,2,3,4]))    #calling multiples function to get the average of the list

#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

def length(lst):
  """Function returns length of the list"""
  count = 0                   # counter to count number of element in the list
  for num in lst:
    count+=1
  return count                # returning lenght of the list

print(length([1,2,3,4]))      # calling length function to get length of the list


#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(lst):
  """Function to calculate minimun valuse in the list"""
  min = 0
  n=0                    # n = list element counter
  for num in lst:        #for loop to iterate over list
    if n == 0:     
      min = lst[0]       # assigning first value to min
    if min > num:
      min = num
    n+=1
  
  if n != 0:                   # if the list is not empty, return minimum value
    return min
  return False                 # else return false

print(minimum([1,2,3,4]))      #calling minimumfunction to ckeck minimum value from the list
print(minimum([-1,-2,-3]))
print(minimum([]))             #calling minimum function to ckeck minimum value in empty list


#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(lst):
  """Function to calculate maximum valuse in the list. if list is empty, returns False"""
  max = 0
  n=0                    # n = list element counter
  for value in lst:        #for loop to iterate over list
    if n == 0:     
      max = lst[0]       # assining firlst value in the list to max
    if max < value:      
      max = value              # assinging list value max if max is less than list value
    n+=1
  
  if n != 0:                   # if the list is not empty, return maximum value
    return max
  return False                 # else return false

print(maximum([1,2,3,4]))      # calling maximum function to get maximum value from the list 
print(maximum([-1,-2,-3]))
print(maximum([]))             #calling maximum function to the maximum value from the empty list


#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

def ultimateaalyze(lst):
  """ Function oto create dictinoary that has sumtotal,average,minimum,maximum & length of the list"""
  ultimate_dict = {}
  ultimate_dict["sumtotal"] = sum_total(lst)      #sum of the list values
  ultimate_dict["average"] = average(lst)        #avg of the list values
  ultimate_dict["minimum"] = minimum(lst)        #minimum value from the list
  ultimate_dict["maximum"] = maximum(lst)        #maximum value from the list
  ultimate_dict["length"] = length(lst)          #lenght of the list
  return ultimate_dict                           #returning dictinoary that has sumtotal,average,minimum,maximum & length of the list

print(ultimateaalyze([1,2,5,6]))                 #calling function ultimateaalyze


#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverse_list(lst):
  """Function to reverse original list"""
  last= len(lst)
  temp=0
  first=0
  
  while(first < last):
    temp = lst[first]
    lst[first] = lst[last-1]                  #swaping elements in the list
    lst[last-1]= temp
    first+=1
    last-=1
    
  return lst                           #returning  reversed list

print(reverse_list([1,2,3,4]))         # calling revere_list function


#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

def is_palindrome(str):
  """Function to check if string is palindrome"""
  reverse_str=""
  original_str=""
  for char in str:
    if char.isalpha():
      reverse_str= char + reverse_str
      original_str = original_str + char
  if reverse_str != original_str:                   #if reverse string is not equal to original string returns False
    return False
  else:
    return True                                 #else True It is palindrome string

print(is_palindrome("radar"))                   
print(is_palindrome("radix"))


#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def fizz_buzz():
  """function prints numbers from 1 to 100, with certain exceptions:
#   #If the number is a multiple of 3, prints “Fizz” instead of the number.
#   #If the number is a multiple of 5, prints “Buzz” instead of the number.
#   #If the number is a multiple of 3 and 5, prints “FizzBuzz” instead of the number."""
  
  for number in range (1,101):         
    if number % 3 == 0 and number % 5 == 0:   # chek if number is multipler of 3 and 5
      print("FizzBuzz", end =", ")
    elif number % 3 == 0:                      #check if number iis multiplier of 3
      print("Fizz",end = ", ")
    elif number % 5 == 0:                      #check if number is multiplier of 5
      print("Buzz", end= ", ")
    else:
      print(number, end= ", ")

fizz_buzz()                                   #calling function fizz_buzz

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

def fibonacci(number):
  """Function to create fibonacci series"""
  count = 0
  n1 = 0
  n2 = 1
  temp = 0

  while count <= number:
    print(n1)
    temp = n1+n2
    n1=n2
    n2 = temp
    count = count + 1

print()
fibonacci(8)                              #calling fibinacci series function 
