from functools import reduce
#====================comprehension Exercises============================== 
# Use list comprehension to create a list containing a solution for the
# famous FizzBuzz problem. For integers 1 to 100, inclusively, the value
# should be:
# ➢ 'Fizz' if divisible by 3
# ➢ 'Buzz' if divisible by 5
# ➢ 'FizzBuzz' if divisible by both 3 and 5
# ➢ The integer itself if not divisible by both 3 and 5


fizz_buzz=["fizzbuzz" if n%3==0 and n%5== 0 else "Fizz" if n%3== 0 else "Buzz" if n%5 == 0 else n for n in range(1,101)]

print(fizz_buzz)


#=====================================Generator Exercises============================
# 1 > Create a generator, primes_gen that generates prime numbers starting from 2.


def isprime(num):
    """Function to check if number is the prime number"""
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def primes_gen():
    """ Generator function to generate prime numbers"""                        #generator to generate prime numbers
    num = 2                                                                    #starting from 2   
    while True:
        if isprime(num):                 # calling function to check if number is prime number
            yield num
        num+=1
     
    return

gen = primes_gen()
for _ in range (10):                        # loop to generate first 15 prime numbers
    print(next(gen), end=" ")


#  2  > Create a generator, unique_letters that generates unique letters from
#       the input string. It should generate the letters in the same order as
#       from the input string.

def unique_letter(str1):
    """Generator to generate unique letters from the input string"""
    list1=[]                                 
    for char in str1:
        if char not in list1:                    
            list1.append(char)
            yield char
        
for letter in unique_letter('hello'):
    print(letter, end = " ")



# ================================================Lambda Function=====================
print()
# Consider the list:prog_lang = [('Python', 3.8),
                                #  ('Java', 13),
                                #  ('JavaScript', 2019),
                                #  ('Scala', 2.13)]



prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]

#   1  > Sort the list by each language's version in ascending order.

print(sorted(prog_lang,key=lambda x: x[1]))   

#   2  > Sort the list by the length of the name of each language in descending order.

print(sorted(prog_lang,key=lambda x: len(x[0]),reverse=True))


#   3  > Filter the list so that it only contains languages with 'a' in it.


print(list(filter(lambda x: x[0].count('a')> 1,prog_lang)))


#   4  >  Filter the list so that it only contains languages whose version is in integer
        #  form.


print(list(filter(lambda x: isinstance(x[1],int),prog_lang)))



#    5   > Transform the list so that it contains the tuples in the form,
#         ("language in all lower case", length of the language string)


print(list(map(lambda x :(x[0].lower(),len(x[0])),prog_lang)))           


#     6   > Generate a tuple in the form,
#           ("All languages separated by commas",
#           "All versions separated by commas")
