# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def change_positive():
    user_input_list = [int(item) for item in input("Enter the list items for Biggie Size (positive or negative integers) : ").split()]
    print(user_input_list)
    for count, item in enumerate(user_input_list):
        if item > 0:
            user_input_list[count] = "big"
    return user_input_list

# Count Positives - Given a list of numbers,
# create a function to replace last value with number of positive values.
# Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.
# (Note that zero is not considered to be a positive number).
def count_positive():
    count = 0
    user_input_list = [int(item) for item in input("Enter the list items for count positives (positive or negative integers) : ").split()]
    for item in user_input_list:
        if item > 0:
            count += 1
    user_input_list.pop()
    user_input_list.append(count)
    return user_input_list

# SumTotal - Create a function that takes a list as an argument and returns the
# sum of all the values in the list.
# For example sum_total([1,2,3,4]) should return 10
def sum_total():
    user_input_list = [int(item) for item in input("Enter the list items for sumtotal (positive or negative integers) : ").split()]
    sum = 0
    for item in user_input_list:
        sum += item
    return sum


# Average - Create a function that takes a list as an argument and returns the average
# of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5
def average():
    user_input_list = [int(item) for item in input("Enter the list items to find average (positive or negative integers) : ").split()]
    sum1 = 0
    counter = 0
    for item in user_input_list:
        sum1 += item
        counter += 1
    avg = sum1 / counter
    return avg

# Length - Create a function that takes a list as an argument and returns the length of the list.
# For example length([1,2,3,4]) should return 4
def length():
    user_input_list = [int(item) for item in input("Enter the list items to find it's length (positive or negative integers) : ").split()]
    count = 0
    for item in user_input_list:
        count += 1
    return count


# Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.
# If the passed list is empty, have the function return false.
# #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum():
    user_input_list = [int(item) for item in input("Enter the list items to find minimum value (positive or negative integers) : ").split()]
    if not user_input_list:
        return False
    temp = user_input_list[0]
    for item in user_input_list:
        if item < temp:
            temp = item
    return temp


# Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.
# If the passed list is empty, have the function return false.
# #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def maximum():
    user_input_list = [int(item) for item in input("Enter the list items to find maximum value (positive or negative integers) : ").split()]
    if not user_input_list:
        return False
    temp = user_input_list[0]
    for item in user_input_list:
        if item > temp:
            temp = item
    return temp


# Ultimateaalyze - Create a function that takes a list as an argument and returns a
# dictionary that has the sumTotal, average, minimum, maximum ad length of the list.
def ultimate_dict():
    user_input_list = [int(item) for item in input("Enter the list items for Ultimateaalyze dict(positive or negative integers) : ").split()]
    result = {}
    result["sumtotal"] = sum(user_input_list)
    result["average"] = sum(user_input_list)/len(user_input_list)
    result["minimum"] = min(user_input_list)
    result["maximum"] = max(user_input_list)
    result["length"] = len(user_input_list)
    return result


# ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.
# Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1].
# This challenge is known to appear during basic technical interviews.
def list_reverse():
    user_input_list = [int(item) for item in input("Enter the list items to reverse(positive or negative integers) : ").split()]
    return user_input_list[::-1]


# Ispalindrome- Given a string, write a python function to check if it is palindrome or not.
# A string is said to be palindrome if the reverse of the string is the same as string.
# For example, “radar” is a palindrome, but “radix” is not a palindrome.
def is_palindrome():
    input_sentence=input("Enter string to check for palindrome: ")
    input_sentence = input_sentence.lower()
    input_sentence = input_sentence.split()
    input_sentence = ",".join(input_sentence)
    input_sentence = input_sentence.replace(",", "")
    # print(word1)
    if input_sentence == input_sentence[::-1]:
        return True
    return False

# Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
# If the number is a multiple of 3, print “Fizz” instead of the number.
# If the number is a multiple of 5, print “Buzz” instead of the number.
# If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.
def fizzbuzz():
    #print("print FizzBuzz for numbers in range of 1 to 100")
    start = int(input(" Enter the starting range for FizzBuzz: "))
    end = int(input(" Enter the ending range for FizzBuzz: "))
    fb = ["FizzBuzz" if (num % 3 == 0 and num % 5 == 0) else "Fizz" if (num % 3 == 0) else "Buzz" if (
                num % 5 == 0) else num for num in range(start, end+1)]
    return fb


# Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Create a function that accepts any number and will create a sequence based on the fibonacci sequence.
def fibonacci_recur(n):
    if (n >= 0):
        if n <= 1:
            return n
        else:
            return (fibonacci_recur(n - 1) + fibonacci_recur(n - 2))


# get input from user

print('''Enter choice from below:
         1.Change postitve numbers to \"big\"
         2.Count positive values and replace last value to count
         3.Sum of all list items
         4.Average of all list items
         5.Length of thr list
         6.Minimum value in the list
         7.Maximum value in the list
         8.Dictionary with sum, average, max, min and length of input list
         9.Reverse the given list
         10.Check for palindrome
         11.FizzBuzz
         12.Fibonacci sequence
         13.Exit''')
user_choice = 100  # initializing with random int value
while int(user_choice) != 13:
    user_choice = input("Please enter your choice: ")
    if user_choice.isspace():
        print(" Invalid user choice")
        user_choice = 0
    elif user_choice not in ['1','2','3','4','5','6','7','8','9','10','11','12','13']:
        print("Invalid user choice ")
        user_choice=0
    elif int(user_choice) == 1:
        # function call
        print("change positive numbers to \"big\" in list:", change_positive())
    elif int(user_choice) == 2:
        # function call
        print("count positive values in the list and replace last value with positive item count :", count_positive())
    elif int(user_choice) == 3:
        # function call
        print("sum of all list items in :", sum_total())
    elif int(user_choice) == 4:
        # function call
        print("average of list items in :", average())
    elif int(user_choice) == 5:
        # function call
        print("length of list items:", length())
    elif int(user_choice) == 6:
        # function call
        print("minimum value in the list : ", minimum())
    elif int(user_choice) == 7:
        print("maximum value in the list: ", maximum())
    elif int(user_choice) == 8:
        # function call
        print("Dict with aggregate functions of list: ", ultimate_dict())
    elif int(user_choice) == 9:
        # function call
        print("reverse of the list :", list_reverse())
    elif int(user_choice) == 10:
        print("palindrome : ", is_palindrome())
    elif int(user_choice) == 11:
        # function call
        print("Callin FuzzBuzz: ", fizzbuzz())
    elif int(user_choice) == 12:
        # function call
        n = int(input("Enter input value for fibonacci sequence: "))
        print("Fibonacci sequence : ", fibonacci_recur(n))
    elif int(user_choice) == 13:
        print("Exiting")
        exit