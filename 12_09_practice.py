#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def positive_to_big(numbers):
    return ["big" if number > 0 else number for number in numbers]


#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def last_num_positives(numbers):
    num_positives = sum(1 for number in numbers if number > 0)
    return numbers[:-1] + [num_positives]


#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10
def sum_numbers(numbers):
    return sum(numbers)


#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5
def avg_num(numbers):
  return sum(numbers) / len(numbers)


#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4
def length_num(numbers):
  return len(numbers)


#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def min_num(numbers):
  return min(numbers)


#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def max_num(numbers):
  return max(numbers)


#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.
def Ulti(numbers):
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "length": len(numbers),
    }

#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverse_list(numbers):
    for i in range(len(numbers) // 2):
        numbers[i], numbers[-i - 1] = numbers[-i - 1], numbers[i]
    return numbers


#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
def is_palindrome(input_word: str) -> bool:
    clean_word = input_word.upper()
    return clean_word == clean_word[::-1]

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

def fibonacci(n: int) -> List[int]:
    fib_seq = [0, 1]

    for i in range(2, n):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    
    return fib_seq
