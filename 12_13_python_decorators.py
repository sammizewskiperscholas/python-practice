#Using a closure, create a function, multiples_of(n) which we can use to
#create generators that generate multiples of n less than a given
#number.

def multiples_of(n):
    def multiply(k):
        print([i for i in range(n, k, n)])
    return multiply

m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(type(m3_under30))
print(m3(60))
print(m3_under30)
print(m7_under30)

#Create following decorators:
#1. make_upper – make every letter of a string returned from the decorated
#function uppercase.

def make_upper(f):
    def wrapper():
        str1=f()
        return str1.upper()
        
    return wrapper
@make_upper
def hello_world():
     return 'hello young, good day!!'
print(hello_world()) # output: HELLO YOUNG, GOOD DAY!!
#2. print_func_name: Anynt the name of the decorated function before
#executing the function.
def print_func_name(f):
    def wrapper():
        print(f.__name__,"is running...")
        f()
    return wrapper

@print_func_name
def my_func():
    print('Python is fun!!')
my_func() # output: my_func is running...

#3. give_name(name) – concatenate the given name at the end of a string
#returned from the decorated function.

def give_name(str1):
    def wrapper(f):
        return f()+" "+str1
    return wrapper
@give_name('Theresa')
def greeting():
  return 'Hello'

print(greeting) # output: Hello Theresa

print("---------------------------------------------------------------------------------------------------------")



#4. print_input_type – print a data type of the input argument before executing the decorated function.
def print_input_type(func):
  def typer(n):
    return f'The input data type is {type(func)}\nThe {func.__name__} of {n} is {func(n)}'
  return typer
  
@print_input_type
def square(n):
  return n**2

print(square(3.5)) # output: The input data type is <class 'float'>


#5. check_return_type(return_type) – check if the return type of the decorated function is return_type and print the result before executing the function.

def check_return_type(return_type):
  def wrapper(func):
    def inner(*args):
      print(func(*args))
      if type(func(*args)) == return_type:
        return f'The return type is {type(func(*args))}'
      else:
        return f'=========Error!!=========The return type is NOT {return_type}'  
    return inner
  return wrapper
  
@check_return_type(float)
def square(n):
  return n ** 2

print(square(6)) # output: =========Error!!=========The return type is NOT <class 'str'>


print(square(2.9)) # output: The return type is <class 'float'>


#6. execute_log – write a function execution log on the log file.
from datetime import datetime

def execute_log(func):
  def wrapper(*args):
    return f'{datetime.now()} {func.__name__}'
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