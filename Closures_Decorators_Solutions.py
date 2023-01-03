from datetime import datetime
#1.Using a closure, create a function, multiples_of(n) which we can use to
# create generators that generate multiples of n less than a given
# number.


def multiples_of(n):  
    def inner(n1):
        count = 1
        for _ in range(n1):
            table1 = count * n
            if table1 < n1:
                yield table1
                count += 1
    return inner

m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(type(m3_under30))
print(*m3_under30)
print(*m7_under30)

print(50 * "#")
#1. make_upper – make every letter of a string returned from the decorated
# function uppercase.


def make_upper(func):
    def wrapper():
        str1 = func()
        return str1.upper()
    return wrapper


@make_upper
def hello_world():
    return "hello young, good day!!"

print(hello_world())

print(50 * "#")

#2. print_func_name – print the name of the decorated function before
# executing the function.

def print_func_name(func):
    def wrapper():
        print("my_func is running...")
        str1 = func()
        return str1
    return wrapper

@print_func_name
def my_func():
    print('Python is fun!!')

my_func()
print(50 * "#")


#3. give_name(name) – concatenate the given name at the end of a string
# returned from the decorated function.

def give_name(val):
    def innerfunc(func):
        def wrapper():
            return func() + " " + val
        return wrapper
    return innerfunc

@give_name('Therasa')
def greeting():
    return 'Hello'

print(greeting())
print(50 * "#")


#4. print_input_type – print a data type of the input argument before
# executing the decorated function.


def print_input_type(func):
    def wrapper(n):
        str1 = func(n)
        str2 = type(str1)
        return f"The input data type is {str2} \n{str1}"
    return wrapper

@print_input_type
def square(n):
    return n ** 2 

print(square(3.5))
print(50 * "#")

#5. check_return_type(return_type) – check if the return type of the
# decorated function is return_type and print the result before executing
# the function.

def check_return_type(val):
    def innerfunc(func):
        def wrapper(n):
            value = func(n)
            type_value = type(value)
            if type_value == val:
                return f"The return type is {type_value} \n{value}"
            return f"Error!! \nThe return type is NOT {type_value} \n{value}"
        return wrapper
    return innerfunc



@check_return_type(str)
def square(n):
    return n**2

print(square(6))
print(50 * "#")

@check_return_type(float)
def square(n):
    return n**2

print(square(2.9))
print(50 * "#")

#6. execute_log – write a function execution log on the log file.

def execute_log(func):
    def wrapper(*args):
        time_value = datetime.now()
        function_name = func.__name__
        function_output = func(*args)
        return function_output,f"{time_value} {function_name}"
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

print(multiply(6,2,3))
print(hello_world())
print(multiply(2.2,4))
print(hello_world())
