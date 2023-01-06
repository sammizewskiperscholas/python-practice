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



prog_lang = [('Python', 3.8),('Java', 13),('JavaScript', 2019),('Scala', 2.13)]

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


print(reduce(lambda x,y :(f'{x[0]},{y[0]}',f'{x[1]},{y[1]}'),prog_lang)) #using reduce function

#                   using map function
languages=tuple(map (lambda x: x[0], prog_lang))
version=tuple(map(lambda x:str(x[1]),prog_lang))
print((",".join(languages),",".join(version)))


#================================================Clossure Exercise==================

#        Using a closure, create a function, multiples_of(n) which we can use to
#        create generators that generate multiples of n less than a given number
#         number.

def multiples_of(n):
    def multiples(given_number):                        #GEnerator function 
        num=1
        while given_number >= n:
            yield n*num         
            given_number -= n
            num+=1
    return multiples                             #returning function WITHOT parenthesis

m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)
print(type(m3_under30))                       #output <class 'generator'>
print(*m7_under30)
print(*m3_under30)



# =================================================Decorator Excercise====================
# Create following decorators:

#   1.  make_upper – make every letter of a string returned from the decorated
        # function uppercase.


def make_upper(func):                        # func function passed as paramer
    def wrapper():                           #wrapper function created
        val = func()
        return val.upper()                   #returning string converted in to uppercase
    return wrapper                           #return wrapper function

@make_upper                                  #hello_world decorated with modified behavior
def hello_world():
    return "hello young, good day!!"

print(hello_world())                        


#     2. print_func_name – print the name of the decorated function before
#        executing the function.

def print_func_name(func):                                               #function passed as parameter 
    def wrapper():                                                       #wrapper function - innner function
        print("{} is running".format(func.__name__))
        func()                                                           #calling function 
    return wrapper                                                       #return wapper function

@print_func_name                               #my_func decorated with modifier behavior
def my_func():
    print("Python is fun")

print(my_func())


#     3.   give_name(name) – concatenate the given name at the end of a string
#          returned from the decorated function.

def give_name(name):                                             #outer function 
    def decorator(func):                                        #decorated function
        def wrapper():
            greetings = func()
            return "{} {}".format(greetings,name)               #concatenating the name at the end of the sring return from decorated function
        return wrapper                                           #returning wrapper function
    return decorator                                             #returning decorator function

@give_name('Theresa')                                          #passing parameter to the outer function
def greeting():
    return 'Hello'

print(greeting())                                              #calling function decorated by decorator



#    4.  print_input_type – print a data type of the input argument before
#        executing the decorated function.

def print_input_type(func):          
    def wrapper(*arg):             
        print("The input data type is : {}".format(type(*arg)))    #input datatype
        val = func(*arg)                #return value from passed function
        return val
    return wrapper

@print_input_type                        #square function decorated with modifier behavior
def square(n):
    return n*n

print(square(3.5))



#      5. check_return_type(return_type) – check if the return type of the
#         decorated function is return_type and print the result before executing
#         the function.

def check_return_type(type1):
    def check_return(func):
        def wrapper(*arg):

            if type1 != (type(arg[0])):       #if output type not equal to input type Disply ERROR msg
               print("=================Error!!!")
               print("============The return type is NOT  {}".format(type1))
            # print(*arg1)
            else:
                print("The return type is {}",type1)
            val = func(*arg)
            return val
        return wrapper
    return check_return


@check_return_type(str)                    #First input str
def square(n):
    return n*n
print(square(3.2))


@check_return_type(float)                  #second input float
def square(n):
    return n*n

print(square(3.2))


#      6.   problem number 6:execute_log – write a function execution log on the log file.


def execute_log(func):                           #outer function
    def wrapper(*arg):                           #Wrapper Function
        with open ("log.txt",'a') as f:          #opening text file to save log data
            f.write(str(datetime.datetime.now())+func.__name__+"\n")  #writing log data to txt file
            val = func(*arg)
            return val
    return wrapper

@execute_log                       #multiply function decorated with modifier behavior
def multiply(*nums):
    mult = 1
    for n in nums:
        mult *= n
    return mult

@execute_log                        #hello_world function decorated with modifier behavior     
def hello_world():
    return "Hello world"

print(multiply(6, 2, 3)) # 36
print(hello_world()) # hello world!!
print(multiply(2.2, 4)) # 8.8
print(hello_world())


