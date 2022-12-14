def multiples_of(n):
    def limit(k): 
        for i in range(n,k):
            if i % n == 0:
                yield i
    return limit

m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)
print(type(m3_under30))
print(*m3_under30)
print(*m7_under30)

#1. make_upper – make every letter of a string returned from the decorated function uppercase.
def make_upper(up):
    def wrapper():
        return up().upper()
    return wrapper

@make_upper
def hello_world():
    return 'hello young, good day!!'

uppity = make_upper(hello_world) # output: HELLO YOUNG, GOOD DAY!!
print(uppity())

#2. print_func_name – print the name of the decorated function before executing the function.
def print_func_name(machine):
    def wrapper():
        func_name = machine.__name__
        print(f"{func_name} is running...")
        print(machine())
    return wrapper

@print_func_name
def my_func():
    return('Python is fun!!')

my_func() # output: my_func is running...
                    #Python is fun

#3. give_name(name) – concatenate the given name at the end of a string 
# returned from the decorated function.
def give_name(name):
    def wrapper(yar):
        print(yar(), name)
    return wrapper
@give_name('Theresa')
def greeting():
    return 'Hello'

#print(greeting()) # output: Hello Theresa

#4. print_input_type – print a data type of the input argument before executing the 
# decorated function.
def print_input_type(q):
    def wrapper(p):
        x = type(p)
        print(f"The input data type is {x}")
        activate = q(p)
        return activate
    return wrapper
@print_input_type
def square(n):
    return n ** 2

print(square(3.5)) # output: The input data type is <class 'float'> 
                             #12.25

#5. check_return_type(return_type) – check if the return type of the 
# decorated function is return_type and print the result before executing
# the function.
def check_return_type(return_type):
    def wrapper(p):
        x = type(p)
        activate = return_type()
        returned = type(activate)
        if returned == x:
            print("bingo")
        else:
            print("=========Error!!")
            print(f"=========The return type is not {return_type}")
            print(type(activate), p, return_type, returned)
            
        return p
    return wrapper
@check_return_type(str)
def square(n):
    return n ** 2

print(square(6)) # output: =========Error!!
                           #=========The return type is NOT <class 'str'>
                           #36

@check_return_type(float)
def square(n):
    return n ** 2

print(square(2.9)) # output: The return type is <class 'float'> 
                             #8.41