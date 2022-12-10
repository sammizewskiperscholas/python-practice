#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". 
#Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].

def make_positive_big(numbers):
    for integer in numbers:
        if integer > 0:
            position=numbers.index(integer)
            numbers[position]="big"
    return(numbers)

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values.
# Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def replace_last_pos_count(numbers):
    positive_count = 0
    for integers in numbers:
        if integers > 0:
            positive_count+=1
    numbers[-1] = positive_count
    return(numbers)

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.
#For example sum_total([1,2,3,4]) should return 10

def sum_values(numbers):
    return(sum(numbers))

def sum_values_2(numbers):
    count=0
    for i in numbers:
        count+=i
    return count        

#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  
#For example multiples([1,2,3,4]) should return #2.5

def avg_values(numbers):
    average=sum(numbers)/len(numbers)
    return average

def avg_values_2(numbers):
    count=0
    for i in numbers:
        count+=i
    average = count/len(numbers)
    return average 

#Length - Create a function that takes a list as an argument and returns the length of the list.  
#For example length([1,2,3,4]) should return 4

def length(numbers):
    return len(numbers)

def length_2(numbers):
    count=0
    for i in numbers:
        count+=1
    return count

#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  
#If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum_1(numbers):
    empty_list= []
    if len(numbers) == len(empty_list):
        return False
    else:
        return min(numbers)

def minimum_2(numbers):
    empty_list= []
    if len(numbers) == len(empty_list):
        return False
    else:
        small=numbers[0]
        for i in numbers:
            if i < small:
                small=i
        return small
            
'''
# I was curious to see if I could make a function that accounts for an edge case, of a list is provided with numbers that are in strings
def minimum_3(numbers):
    empty_list= []
    if len(numbers) == len(empty_list):
        return False
    else: 
        for i in numbers:
            new_list = []
            if type(i) == str and i.isalpha() is not True:
                new_list.append(float(i))
            else:
                new_list.append(i)
        return min(new_list)
    return min(numbers)
'''           

#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  
#If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maxium_1(numbers):
    empty_list= []
    if len(numbers) == len(empty_list):
        return False
    else:
        return max(numbers)

def maximum_2(numbers):
    empty_list= []
    if len(numbers) == len(empty_list):
        return False
    else:
        big=numbers[0]
        for i in numbers:
            if i > big:
                big=i
        return big

#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.



#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order. Do this without creating a empty temporary list. 
# For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
'''
# Why doesn't this work?
def reversal_2(numbers):
    count=0
    for i in range(0,len(numbers)):
        backwards=numbers[(-1+count)]
        count-=1
        numbers[i]=backwards
    return numbers
'''
def reversal(numbers):
    return numbers[::-1]

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. 
#A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
def Is_palindrome_1(word):
    if word == word[::-1]:
        return "Is a Palindrome"
    else:
        return "Is not a Palindrome"

def Is_palindrome_2(word):
    new_word=""
    for i in range(1, len(word)+1):
        new_word+=word[-i]
    if word == new_word:
        return "Is a Palindrome"
    else:
        return "Is not a Palindrome"

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def Fizzbuzz():
	for i in range(1,101):
		if i % 15 == 0:
			print("FizzBuzz")
		else:
			if i % 3 ==0:
				print("Fizz")
			elif i % 5 ==0:
				print("Buzz")
			else:
				print(i)
Fizzbuzz()

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
#such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.