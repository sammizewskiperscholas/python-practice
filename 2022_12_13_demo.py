#list = []
#for x in range(1,101):
    #if x % 3 == 0:
        #list.append("Fizz")
    #elif x % 5 == 0:
        #list.append("Buzz")
    #elif x%3==0 and x %5==0:
        #list.append("FizzBuzz")
#print(list)

#def decorator1(func):
    #def wrapper():
        #print("I am running before the function call")
        #func()
        #print("I am running after the function call")
    #return wrapper
#@decorator1
#def i_am_func():
    #print("I am the function")

#run_decorator = decorator1(i_am_func)
#run_decorator = wrapper
#run_decorator()


# 1. make_upper- make every letter of a strinf returned from the decorated function uppercase.

def decorator(func):
    def make_upper():
        print('hello young, good day!!'.upper())
    return make_upper

def hello_world():
    return 'hello young, good day!!'

use_decorator = decorator(hello_world)
use_decorator()


# 2. print_func_name - print the name of the decorated function before executing the function.

def decorator1(func):
    def print_func_name():
        print('my_func is running...')
        func()
    return print_func_name

def my_func():
    print('Python is fun!!')

use_decorator1 = decorator1(my_func)
use_decorator1()



# 3. give_name(name) - concatenate the given name at the end of a string returned from the decorated
#def decorator2(func):
    #def greeting():
        #print('Hello' + func())
        #return 'Hello'
    #return greeting

#def give_name(name):
    #print(name)
    
#give_name('Theresa')
#use_decorator2 = decorator2(give_name)
#use_decorator2()
#print(greeting())

#def decorator2(func):
    #def greeting():
        #print(greeting() + give_name('Theresa'))
        #return 'Hello'
    #return greeting


#def give_name():
    #return'Theresa'

#use_decorator2 = decorator2(give_name)
#use_decorator2()



# 4. print_input_type - print a data type of the input argument before executing the decorated function.

def decorator3(func):
    print(type(square(3.5)))
    def print_input_type():
        print(square(3.5))
    return print_input_type

def square(n):
    return n ** 2

use_decorator3 = decorator3(square)
use_decorator3()
# 5. check_return_type(return_type) - check if the return type of the decorated function is return_type and print the result before executing the function.

def decorator4(func):
    def check_return_type(str):
        print(type(check_return_type))
        print()
    return check_return_type

def square(n):
    return n ** 2

use_decorator4 = decorator4(square)
use_decorator4()

# 6. execute_log - write a function execution log on the log file.