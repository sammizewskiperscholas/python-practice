#4: Divisors
#num = int(input("Please choose a number to divide: "))

#listRange = list(range(1,num+1))

#divisorList = []

#for number in listRange:
#    if num % number == 0:
#        divisorList.append(number)

#print(divisorList)

#5: List Overlap
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
for y in b:
    if y in a: 
        c.append(y)
#print(c)

#One line solution
#print(list(set(a) & set(b)))

#6: String Lists : Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
# string = input("Input a string to see if it is a palindrome: ")
# reverse = string[::-1]
# print(reverse)
# if string == reverse: 
#     print("This word is a palindrome")
# else: 
#     print("This word is not a palindrome")

#7: Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# a = [1,4,9,16,25,36,49,64,81,100]

# evens = [x for x in a if x % 2 == 0]

# print(evens)

#8: Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
import sys


# user1_answer = input("Player 1:rock, paper or scissors? ")
# user2_answer = input("Player 2: rock, paper or scissors? ")

# def compare(u1, u2):
#     if u1 == u2:
#         return("It's a tie!")
#     elif u1 == 'rock':
#         if u2 == 'scissors':
#             return("Rock wins!")
#         else:
#             return("Paper wins!")
#     elif u1 == 'scissors':
#         if u2 == 'paper':
#             return("Scissors win!")
#         else:
#             return("Rock wins!")
#     elif u1 == 'paper':
#         if u2 == 'rock':
#             return("Paper wins!")
#         else:
#             return("Scissors win!")
#     else:
#         return("Invalid input! You have not entered rock, paper or scissors, try again.")
#         sys.exit()

# print(compare(user1_answer, user2_answer))

#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
# import random 
# number = random.randint(2,10)
# guess = 0
# while guess != number:
#     guess = int(input("Guess the number between 1 and 9: "))
#     if guess < number: 
#         print("Too low, try again")
#     elif guess > number: 
#         print("Too high, try again")
#     else: 
#         print("Yessirrrr!!" )

#10: List Overlap Comprehensions
import random
 
# a = random.sample(range(1,30), 12)
# b = random.sample(range(1,30), 16)
# result = [i for i in a if i in b]
# print(result)

#11: Check Primality: Ask the user for a number and determine whether the number is prime or not.
# import sys
# number = input("Please enter a number" + "\n" + ">>>")
# number = int(number)
# prime = False # initiate boolean for true false, default false 
# if number > 0: 
#     for x in range(2, number - 1): #this range excludes number and 1, both of which the number is divisible by
#         if number % x != 0: 
#             continue
#         elif number % x ==0: 
#             sys.exit("The number is not prime")
#     sys.exit("The number is prime.")
# elif number == 0: 
#     sys.exit("The number is not prime.")
# else: 
#     sys.exit("The number is not prime")

#12 List Ends: Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

# def list_ends(list):
#     return [list[0], list[len(list)-1]]

# print(list_ends([4,8,3,9,1]))

#14 List Remove Duplicates - Write a program(function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates

# def duplicate(x):
#     y= []
#     for i in x: 
#         if i not in y: 
#             y.append(i)
#     return y

# print(duplicate([1,2,3,1,2,4,6,7,8,9]))

#15 Reverse Word Order - Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
# def reverse_v1(x):
#   y = x.split()
#   result = []
#   for word in y:
#     result.insert(0,word)
#   return " ".join(result)

#18 Cows and Bulls 
