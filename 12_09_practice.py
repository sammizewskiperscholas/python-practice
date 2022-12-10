# TODO  Question 1
#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def make_it_big(list_input) -> list:
    for index, num in enumerate(list_input):  # enumerate to keep track
        if num > 0:
          list_input.insert(index, "big")  # insert at index big  
          list_input.pop(index + 1)  # old num shifts up, delete that one
    return list_input   # return list

print(make_it_big([12, -7, 0, 2]))

# main takeaway, list methods to not need to be assigned back to list, they directly mutate the list
    
# ------------------------------------------ #

# TODO Question 2
#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
# 1, 1, 1 becomes 1, 1, 3

def count_positive(list_input) -> list:
  count = 0
  for num in list_input:
    if num > 0: 
      count += 1
  list_input.pop(-1)
  list_input.append(count)
  return list_input


print(count_positive([-1, 1, 1, 1]))  # 3 positive

# -------------------------------- #

# TODO Question 3
#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10

def sum_list(list_input) -> list:
   return sum(list_input)
  
print(sum_list([0, -1, 1]))
print(sum_list([12, -2, 10]))

# ----------------------------- #

# TODO Question 4
#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5
def ave_list(list_input) -> list:
   return sum(list_input)/len(list_input)

print(ave_list([1, 2, 3, 4]))

# --------- #
# TODO Question 5
#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

def len_list(list_input) -> list:
   return len(list_input)

print(len_list([1, 2, 3, 4]))


# TODO Question 6
# Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  
# If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def min_list(list_input) -> list:  # I thought if I specify I wouldn't need to use try: except:, still keeping it in tho
   try: return min(list_input)     # Fancy
   except: ValueError
   return 1

print(min_list([-1, -2, -3]))
print(min_list([]))

# ----------------------------- #

# TODO Question 7
# Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  
# If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def max_list(list_input) -> list: 
   try: return max(list_input)     
   except: ValueError
   return -1

print(max_list([1, 2, 3, 4]))
print(max_list([]))

# ----------------------------------------------- # 

# TODO Question 8 
#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.
# dictionary
  # keys:
    # sum 
    # avg
    # min
    # len of list

def ultimate_analyze(list_input) -> list:  
   dictionary = {"sum":0, "avg":0, "min":0, "max":0, "len":0}
   list_input.sort()
   dictionary["sum"] = sum(list_input)
   dictionary["len"] = len(list_input)
   dictionary["avg"] = dictionary["sum"] / dictionary["len"]  # effeciency 🔥👄🔥  # this question was fun. 
   dictionary["max"] = list_input[-1]
   dictionary["min"] = list_input[0]
   return dictionary

print(ultimate_analyze([1, 2, 3, 4]))  # sum: 10, avg: 2.5, min: 1, max: 4, len: 4
print(ultimate_analyze([2, 4, 3, 1]))  # testing sort


# ------------------------------------- #

# TODO Question 9 
# ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. 
# This challenge is known to appear during basic technical interviews.

def reverse_list(list_input) -> list:
   list_input.sort(reverse=True)
   return list_input

print(reverse_list([1, 2, 3, 4]))

# ----------------------------- #

# TODO Question 10
# Ispalindrome- Given a string, write a python function to check if it is palindrome or not. 
# A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
def is_palindrome(string) -> str: # ❕ Good question. 
   list_comp = [char for char in string]  # list comp [a, b, c]  # easier than attempting to use .split() for chars with no spaces or a traditional for loop
   list_comp_backwards = list_comp.copy()  # copy, reverse [c, b, a]
   list_comp_backwards.reverse()
   for index in range(len(list_comp) - 1):  # index will be same, but will chars? need to compare l_normal[0] = a; l_reversed[0] = c
      return list_comp[index] == list_comp_backwards[index]  # return false immediately if not true
   return  # otherwise return true
      

print(is_palindrome("radar"))
print(is_palindrome("radix"))


# ------------------------------------- #

# TODO question 11
#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def FizzBuzz():
   for num in range(101):
      if num % 3 == 0:
        if num % 5 == 0:
         print("FizzBuzz")  # 3 and 5
        else:
           print("Fizz")  # just 3
      elif num % 5 == 0:
         print("Buzz")  # only 5
      else:
         print(num)
         
FizzBuzz() 

# --------------------------------------------- #

# TODO Question 12

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.


def Fibbonacci(target):  # this took me  hella long to figure out lol. But I did it just off of what I learned 🥳
  start_list = [0, 1]  # 0 and 1 kickstart
  while start_list[-1] <= target:  # while the last number in the list is less than or equal to the target we want to climb to
    summation = sum(start_list[-2:])  # sum the list from the second to last, to last number 👀(list always reads from right to left)
    start_list.append(summation)  # append the list with the new sum
  start_list.pop()  # pop last num after exiting the loop b/c it will always be greater than target
  num_string = ", ".join(str(num) for num in start_list) # join method just populates an otherwise empty string with iterables and some other flavor like whitespace and/or char

  print(f"Fibbonacci Sequence: {num_string}")  # f string w/ num string embedded

Fibbonacci(100)  # will print 0, 1, 1, etc. It's the real deal

# Main takeaway - the target here is the delimiter, it has nothing to do with any calculations. 


# test_list = [0, 1]
# print(sum(test_list[-2:]))
