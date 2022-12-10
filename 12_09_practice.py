#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].

# Function that changes all positive numbers to the string "big"
def make_it_big(output_list):
  
  for position, number in enumerate(output_list):
    # Checking if the number is positive
    if number > 0:
      # Assigning the value "big" to the positive number
      output_list[position] = "big"
  return output_list    
  
biggie_size = [-1, 3, 5, -5]
# Calling the function to change all positive numbers to the string "big"
make_it_big(biggie_size)
print(biggie_size)
   
#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

# Function to replace last value with the count of positive values
def count_positives(output_list):
  total = 0
  for number in output_list:
    # Checking if the number is positive
    if number > 0:
      # Adding the positive numbers
       total += number
  # Assigning the sum of all positive values to the last value of the list
  output_list[-1] = total   
  return output_list    
  
input_list = [-1, 1, 1, 1]
# Calling the function to count the positive numbers
count_positives(input_list) 
print(input_list)

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10

# Function to return the sum of all values
def sumtotal(output_list):
    return sum(output_list)
  
input_list = [1, 2, 3, 4]
print(sumtotal(input_list)) 

#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5

# Function to return the average of all the values in the list
def average(output_list):
 # Returns the average of the values in the list
  return sum(output_list)/len(output_list)
  
input_list = [1, 2, 3, 4]
avg = 0
avg = average(input_list)
print(avg)

#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

# Function to get the length of the list
def length(output_list):
  # Returning the length og the list
   return len(output_list)

input_list = [1, 2, 3, 4]
lgth = 0
# Calling the function to find the length of the list
lgth = length(input_list)
print(lgth)

#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

# Function to get the minimum value from the list
def minimum(output_list):
  # Cheking if the list is empty and if so returning false
  if len(output_list) == 0:
     return False
  else:   
     return min(output_list)

input_list = [1, 2, 3, 4]
#input_list = [-1, -2, -3]
#input_list = []
minmum = 0
# Calling the function minimum to get the minimum  value from the list
minmum = minimum(input_list)
print(minmum)


#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

# Function to get the maximum value from the list
def maximum(output_list):
  # Checking if the list is empty and if so returning false
  if len(output_list) == 0:
    return False
  else:
    return max(output_list)  

input_list = [1, 2, 3, 4]
#input_list = [-1, -2, -3]
#input_list = []
maxmum = 0
# Calling the function to get the maximum value from the list
maxmum = maximum(input_list)
print(maxmum)


#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

# Function to get the sumtotal, average, minimum, maximum and length of the list
def ultimateanalyze(output_list):
  output_dictionary = {}
  # Adding entries to the dictionary
  output_dictionary['sumtotal'] = sum(output_list)
  output_dictionary['average'] = sum(output_list)/len(output_list)
  output_dictionary['minimum'] = min(output_list)
  output_dictionary['maximum'] = max(output_list)
  output_dictionary['length'] = len(output_list)
  return output_dictionary

input_list = {1, 2, 3, 4}
# Calling the function to get the sumtoatl, average, minimum, maximum and length of the list
output_dictionary = ultimateanalyze(input_list)
print(output_dictionary)

#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

# Function to reverse the list
def reverselist(output_list):
    return output_list.reverse()

input_list = [1, 2, 3, 4]
# Calling the function to reverse the list
reverselist(input_list)
print(input_list)

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

# Function to check whether the given string is a palindrome or not
def ispalindrome(output_string):
  # Checking if the reverse of the string matches the string
  if output_string == output_string[::-1]:
     return True
  else:
     return False
input_string = "radar"
# Calling the function to check whether the given string is a palindrome or not
print(ispalindrome(input_string))

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

# Function to check the multiples of 3, 5 or both and print accordingly print Fizz, Buzz or FizzBuzz
def fizzbuzz():
  for number in range(1, 101):
    # Checking if the number is both multiple of 3 and 5
    if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
    # Checking if the number is a multiple of 3  
    elif number % 3 == 0:
      print("Fizz")  
    # Checking if the number is a multiple of 5  
    elif number % 5 == 0:
      print("Buzz")  
    else:
      print(number)

# Calling the function to print the numbers from 1 to 100 checking the multiples 
fizzbuzz()


#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

# Function to get the fibonacci sequence for the given number
def fibonacci(n):
   # Initializing the first two number in the fibonacci sequence to zero and one
   first_number = 0
   second_number = 1

   # Assigning 0 if the number is zero
   if n == 0:
      print(first_number, end = " ")

   # Assigning 1 if the number is 1   
   elif n == 1:
      print(second_number, end = " ")
   else:
     number = 0
     # Looping till the length of the given number 
     while number < n:
        print(first_number, end = " ")
        temp = first_number + second_number
        first_number = second_number
        second_number = temp
        number += 1

# Calling the fibonacci function to print the fibonacci sequence
fibonacci(10)    
