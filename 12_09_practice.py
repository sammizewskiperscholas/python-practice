
#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". 
# Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].

def make_it_big(mylist):
  return [each if each < 0 else "big"  for each in mylist ]

print(make_it_big([-1, 3, 5, -5]))

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. 
# Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  
# (Note that zero is not considered to be a positive number).

def count_positives(mylist):
  c = 0
  for each in mylist:
    if each > 0:
      c+=1
  mylist[-1] = c
  return mylist

print(count_positives([-1,1,1,1]))

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list. 
#For example sum_total([1,2,3,4]) should return 10

def sum_total(mylist):
  return sum(mylist)

print(sum_total([1,2,3,4]))

#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  
# For example multiples([1,2,3,4]) should return #2.5
def multiples(mylist):
  return (sum(mylist)/len(mylist))
   
print(multiples([1,2,3,4]))

#Length - Create a function that takes a list as an argument and returns the length of the list.  
# For example length([1,2,3,4]) should return 4
def length(mylist):
  return len(mylist)

print(length([1,2,3,4]))

# Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  
# If the passed list is empty, have the function return false.  
# For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(mylist):
  if len(mylist) == 0:
    return False
  else:
    return min(mylist)

print(minimum([1,2,3,4]))


# Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  
# If the passed list is empty, have the function return false.  
# For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def minimum(mylist):
  if len(mylist) == 0:
    return False
  else:
    return max(mylist)

print(minimum([1,2,3,4]))


# Ultimateaalyze - Create a function that takes a list as an argument and 
# returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

def create_dict(mylist):
  mydict = {}
  mydict["sumtotal"] = sum(mylist)
  mydict["average"] = sum(mylist)/len(mylist)
  mydict["minimum"] = min(mylist)
  mydict["maximum"] = max(mylist)
  mydict["length"] = len(mylist)
  return mydict

print(create_dict([1,2,3,4]))

# ReverseList - Create a function that takes a list as a argument and return a list in a reversed order. 
# Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. 
# This challenge is known to appear during basic technical interviews.

def reverse(mylist):
  return list(reversed(mylist))

print(reverse([1,2,3,4]))

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. 
# A string is said to be palindrome if the reverse of the string is the same as string. 
# For example, “radar” is a palindrome, but “radix” is not a palindrome.

def palindrome(mystr):
  r=""
  l = len(mystr)
  for i in range(l-1, -1, -1):
    r += mystr[i]
  if mystr == r:
    return True
  else:
    return False

print(palindrome("soon"))


#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def myfunc(n):
  if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
  elif n % 5 == 0:
    print("Buzz")
  elif n % 3 == 0:
    print("Fizz")
  else:
    print(n)
  return

myfunc(30)

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
#F(0) = 0, F(1) = 1
#F(n) = F(n - 1) + F(n - 2), for n > 1.
#Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

def fibonacci(n):
  fib_list = [0,1]
  for i in range(2,n):
    fib_list.append(fib_list[i-2] + fib_list[i-1])
  return fib_list

print(fibonacci(10))

#########################################################################################################
############# 12-11-python-practice #####################################################################

####### slide 14 #######
#Create a generator, primes_gen that generates prime numbers starting from 2
def primes_gen():
  return [i for i in range(1,101) if all(i%j != 0 for j in range(2,i))]
  
gen = primes_gen()
for _ in range(10):
  print(next(gen), end=' ')

############ slide 19 and 20 ##################
#Consider the list:
prog_lang = [('Python', 3.8), ('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]

#1. Sort the list by each language's version in ascending order.
def version_sort(pl):
  pl_sort = sorted(pl, key=lambda t : t[1])
  return pl_sort

print(version_sort(prog_lang))

#2. Sort the list by the length of the name of each language in descending order.

def lname_len_sort(pl):
  lname_len_sort = sorted(pl, key=lambda t : len(t[0]), reverse = True)
  return lname_len_sort

print(lname_len_sort(prog_lang))

#3. Filter the list so that it only contains languages with 'a' in it.

def filter_alang_pl(pl):
  pl_fil = list(filter(lambda t : "a" in t[0].lower(), pl))
  return pl_fil

print(filter_alang_pl(prog_lang))


#4. Filter the list so that it only contains languages whose version is in integer form

def filter_intver_pl(pl):
  pl_fil = list(filter(lambda t : type(t[1]) == int, pl))
  return pl_fil

print(filter_intver_pl(prog_lang))

#5. Transform the list so that it contains the tuples in the form, ("language in all lower case", length of the language string)

def tuple_lang_len(pl):
  pl_tup = (*map(lambda t : t[0].lower()+", "+ str(len(t[0])), pl),)
  return pl_tup

print(tuple_lang_len(prog_lang))

#6. Generate a tuple in the form, ("All languages separated by commas", "All versions separated by commas")

def tuple_lang_ver(pl):
    pl_tup = (*map(lambda t : t[0], pl),)
    return pl_tup

print(tuple_lang_ver(prog_lang))
