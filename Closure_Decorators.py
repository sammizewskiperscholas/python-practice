#************************************************************Closure-Exercise*******************************************************************

# Using a closure, create a function, multiples_of(n) which we can use to create generators that generate multiples of n less than a given
# number.

def multiples_of(n):
    def multiply(k):
        for i in range(1,(k//n)+1):
            if i*n<k:
                yield i * n
        
    return multiply

m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(type(m3_under30))
# output: <class 'generator'>

print(*m3_under30)
# output: 3 6 9 12 15 18 21 24 27

print(*m7_under30)

#*************************************************Decorators-Exercises*************************************************************************************

# 1. make_upper – make every letter of a string returned from the decorated function uppercase.

def make_upper(func):
    def sam(*args):
        return func(*args).upper()
    return sam

@make_upper
def hello_world():
    return 'hello young, good day!!'

print(hello_world())

# 2. print_func_name – print the name of the decorated function before executing the function.

def print_func_name(func):
    def wrapper():
        print(func.__name__, "is Running")
        func()
    return wrapper 

@print_func_name
def my_func():
    print('Python is fun!!')

my_func()# output: my_func is running...


# 3. give_name(name) – concatenate the given name at the end of a string returned from the decorated function.

def give_name(n):
   def inner(func):
        def wrapper():
         return (func() + ' ' + n)
        return wrapper
   return inner

@give_name('Theresa')
def greeting():
    return 'Hello'

print(greeting())

# 4. print_input_type – print a data type of the input argument before executing the decorated function.

def print_input_type(func):
    def wrapper(a):
        print("The output data type is ",type(func(a)))
        return func(a)
    return wrapper


@print_input_type
def square(n):
    return n ** 2

print(square(3.5))


#5. check_return_type(return_type) – check if the return type of the decorated function is return_type and print 
#the result before executing the function.

def check_return_type(dtype):
    def inner(func):
        def wrapper(n):
          if type(n) != dtype:
               print("================Error!!\n==============The return type is NOT {}".format(dtype)) 
               
          elif type(n) == dtype:
               return ("The return type is {}".format(dtype)) # + type(n))
          return func(n)        
        return wrapper
    return inner
@check_return_type(str)
def square(n):
    return n ** 2
print(square(6)) # output: =========Error!!
                 #=========The return type is NOT <class 'str'>
                 #36
@check_return_type(float)
def square(n):
    return n ** 2
print(square(2.9))

#6. execute_log – write a function execution log on the log file.

from datetime import datetime, timezone

def execute_log(func):
    
    def inner(*args, **kwargs):
        called_at = datetime.now()
        to_execute = func(*args, **kwargs)
        return ('{0} {1} {2}'.format(called_at,func.__name__,to_execute))
    return inner


@execute_log
def multiply(*nums):
    mult = 1
    for n in nums:
        mult *= n
    return mult
# return multiply

@execute_log
def hello_world():
    return 'hello world!!'

print(multiply(6, 2, 3)) # 36
print(hello_world()) # hello world!!
print(multiply(2.2, 4)) # 8.8
print(hello_world())


