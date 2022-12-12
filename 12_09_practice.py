#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].

list1=[-1, 3, 5, -5]

def make_it_big(list1):
    list=[]
    for i,a in enumerate(list1):
        if a < 0:
            list.append("big")
        else:
            list.append(a)
    print(list)
make_it_big(list1)

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

list1=[-1,1,1,1]

def count_positives(list1):
    list=[]
    sum=0
    for i,a in enumerate(list1):
        if a < 0:
            list.append(a)
        else:
            sum+=a
            list.append(a)
    list[-1]=sum       
    print(list)
count_positives(list1)

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10
list1=[1,2,3,4]
def sum_total(list1):
    sum=0
    for i in list1:
      sum+=i
    print (sum) 
    return sum
sum_total(list1)    
#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5
list1=[1,2,3,4]
def average(list1):
    sum=0
    for i in list1:
      sum+=i
    avg1=sum/len(list1)  
    print (avg1) 
    return avg1
average(list1)    
#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4
list1=[1,2,3,4]
def length(list1):
    count=0
    for i in list1:
      count+=1
    print (count) 
    return count
length(list1)  
#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
list1=[0,-3, 5,2]
def minimum(list1):
    if len(list1)==0:
        print("False")
    else:
        return min(list1)    
        print(min(list1)) 
minimum(list1)
#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
list1=[0,-3, 5,2]
def maximum(list1):
    if len(list1)==0:
        print("False")
    else:
        return max(list1)    
        print(max(list1)) 
maximum(list1)  
#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.
lis1=[0,-3, 5,2]
def ultimateaalyze(list1):
  dict={
  "sum_total":sum_total(list1),
  "average":average(list1),
  "minimum":minimum(list1),
  "maximum":maximum(list1),
  "length":length(list1)
  }
  print(dict)
ultimateaalyze(list1)  
  
#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
list1=[1,2,3,4]
def reverse(list1):
    print (list1[::-1]) 
    return list1[::-1]
reverse(list1)  

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
#string1="radar"
def ispalindrome(string1):
  if string1==string1[::-1]:
    print(f"{string1} is palindrome")
  else:
    print(f"{string1} is not palindrome")
string1 = input('Enter any string ')
ispalindrome(string1)


#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def fizzbuzz():
  for num in range(0,101):
    if num%3==0 and num%5==0:
      print("FizzBuzz")
    elif num%3== 0:
      print("Fizz") 
    elif num%5==0:
      print("Buzz")   
    else:
      print(num)  
fizzbuzz()      

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

def fibonacci(num):
    num1 = 0
    num2 = 1
    seq = 0
    if num == 0:
        return 0
    elif num== 1:
        return 1    
    for i in range(num):
        print(seq, end=' ')
        num1 = num2
        num2 = seq
        seq = num1 + num2
 
num = int(input('Enter any number '))
fibonacci(num)


