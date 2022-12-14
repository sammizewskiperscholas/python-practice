#############################################################################
# Closure Exercise
#############################################################################

# Using a closure, create a function, multiples_of(n) which we can use to
# create generators that generate multiples of n less than a given
# number.
# Function to get multiples for a given number
def multiples_of(n):
    # Function to get multiples for a given number until the product 
    # is less than the given number 
    def multiple(k):
      for i in range(1, (k//n) + 1):
        # Checking if the product is less than the given number
        if i*n < k: 
          yield i * n
   
    return multiple

m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(type(m3_under30))
# output: <class 'generator'>

print(*m3_under30)
# output: 3 6 9 12 15 18 21 24 27

print(*m7_under30)
# output: 7 14 21 28

#############################################################################
# Decorator Exercise
#############################################################################

# Create following decorators:
# 1. make_upper – make every letter of a string returned from the decorated
# function uppercase.

def make_upper(func):
    def wrapper():
      return func().upper()
    return wrapper

@make_upper
def hello_world():
  return 'hello young, good day!!'

print(hello_world()) # output: HELLO YOUNG, GOOD DAY!!

# print_func_name – print the name of the decorated function before
# executing the function.

def print_func_name(func):
  def wrapper():
      print(func.__name__ + ' ' + 'is running...')
      return func()
  return wrapper

@print_func_name
def my_func():
  print('Python is fun!!')

my_func() # output: my_func is running...
          # Python is fun


# give_name(name) – concatenate the given name at the end of a string
# returned from the decorated function.

def give_name(n):
   def inner(func):
        def wrapper():
         return (func() + ' ' + n)
        return wrapper
   return inner

@give_name('Theresa')
def greeting():
  return 'Hello'

print(greeting()) # output: Hello Theresa


#print_input_type – print a data type of the input argument before
#executing the decorated function.

def print_input_type(func):
  def wrapper(n):
    print('The input data type is ' + str(type(func(n))))
    return (func(n))
  return wrapper


@print_input_type
def square(n):
  return n ** 2

print(square(3.5)) # output: The input data type is <class 'float'>


# 5. check_return_type(return_type) – check if the return type of the
# decorated function is return_type and print the result before executing
# the function.

def check_return_type(func):
    def wrapper(a):
        if type(func(a)) == float:
            print("The output data type is ",type(func(a)))
        else:
            print("=========Error!!")
     #       print("=========The return type is NOT ",type(func(a)))
            print("=========The return type is NOT str")
        return func(a)
    return wrapper

@check_return_type
def square(n):
  return n ** 2

print(square(6)) # output: =========Error!!
                 #=========The return type is NOT <class 'str'>
                 #36

@check_return_type
def square(n):
  return n ** 2

print(square(2.9)) # output: The return type is <class 'float'>
                   # 8.41



# execute_log – write a function execution log on the log file.
# function_execution.log
from datetime import datetime, timezone

def execute_log(func):
  def wrapper(*args, **kwargs):
    dtime = datetime.now()
    result = func(*args, **kwargs)
    print('{0} {1}'.format(dtime,func.__name__))
    return result
  return wrapper  


@execute_log
def multiply(*nums):
  mult = 1
  for n in nums:
    mult *= n
  return mult

@execute_log
def hello_world():
  return 'hello world!!'

print(multiply(6, 2, 3)) # 36
print(hello_world()) # hello world!!
print(multiply(2.2, 4)) # 8.8
print(hello_world()) # hello world!!