#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].

list1 = [-1,3,5,-5]
def make_it_big(list1):
  for i, value in enumerate(list1):
    if value >0:
      list1[i] = "big"
  return list1
make_it_big(list1)
print(list1)

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

list1= [-1,1,1,1]
def count_positives(list1):
  result = 0
  for index, value in enumerate(list1):
    if value > 0:
      result+=value
  list1[-1]=result
count_positives(list1)
print(list1) 

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10

list1 = [1,2,3,4]
def sum_total(list1):
  total = 0
  for i in list1:
    total+=i
  return total
sum=sum_total(list1)
print(sum)

#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5

list1 = [1,2,3,4]
def Average(list1):
  total = 0 
  for i in list1:
    total+=i
  avg=total/len(list1)
  return avg
avg=Average(list1)
print(avg)

#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

list1 = [1,2,3,4]
def length(list1):
  l = len(list1)
  return l
l=length(list1)
print(l)

#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

list1 = [1,2,3,4]
def minimum(list1):
  if list1 ==[]:
    return False
  return min(list1)
min = minimum(list1)
print(min)

#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

list1 = [1,2,3,4]
def maximum(list1):
  if list1 == []:
    return False
  return max(list1)
max = maximum(list1)
print(max)

#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

list1 = [1,2,3,4]
def ultimateaalyze(list1):
  result = {}

  sum = 0
  for i in list1:
    sum= sum+i
  s = sum
  a= sum/len(list1)
  m = min(list1)
  m1= max(list1)
  l= len(list1)
  result["Sum"] = s
  result["Avg"]= a
  result["Min"]= m
  result["Max"]= m1
  result["Len"] = l
  return result
result=ultimateaalyze(list1)
print(result)

#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

list1 = [1,2,3,4]
def reverselist(list1):
  return list1.reverse()
reverselist(list1)
print(list1)

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

str1="radar"
def ispalindrome(str1):
  str2=str1[::-1]
  if str1 == str2:
    print(str1 +" is Palindrome")
  else:
    print(str1+" is Not Palindrome")
ispalindrome(str1)

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def fizzbuzz():
  for number in range(1,101):
    if number % 3 == 0:
      print("Fizz ")
    elif number % 5 == 0:
      print("Buzz ")
    elif number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz ")
    else:
        print(number)
fizzbuzz()

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.


def fibonacci(n):
    n1 = 0
    n2 = 1
    if n == 0:
        print(n1)
    elif n == 1:
        print(n2)
    else:
        print(n1)
        print(n2)
        for i in range(2,n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            print(n3)
fibonacci(10)
