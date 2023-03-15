from functools import reduce
from datetime import timezone, datetime

#Create a generator, primes_gen that generates prime numbers
#starting from 2.

def primes_gen():
    for i in range(2,100):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i

gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')


################## unique _letter generator
#def unique_let_gen():


def unique_letters(input_word):
    #unique = set()
    #unique=list()
    unique=[]
    for char in input_word:
        if char not in unique:
            yield char
        #unique.add(char)
        unique.append(char)

for letter in unique_letters('hello'):
    print(letter, end=' ')



'''Use list comprehension to create a list containing a solution for the
famous FizzBuzz problem. For integers 1 to 100, inclusively, the value
should be:
➢ 'Fizz' if divisible by 3
➢ 'Buzz' if divisible by 5
➢ 'FizzBuzz' if divisible by both 3 and 5
➢ The integer itself if not divisible by both 3 and 5'''
fb = ["FizzBuzz" if (num % 3 == 0 and num % 5 == 0) else "Fizz" if (num % 3 == 0) else "Buzz" if (
                num % 5 == 0) else num for num in range(1, 100+1)]
    
print(fb)

#Generators Exercise
#Sort the list by each language's version in ascending order.'''
prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]

#1.Lambda function to print asc order on version
prog_lang.sort(key=lambda a: a[1])
print(prog_lang)

#2.Sort the list by the length of the name of each language in descendingorder.

prog_lang.sort(reverse=True, key=lambda item: len(item[0]))
print(prog_lang)

#3.Filter the list so that it only contains languages with 'a' in it.

output_list=list(filter(lambda item: "a" in item[0],prog_lang))
print(output_list)

#4.Filter the list so that it only contains languages whose version is in integer form.

output_list=list(filter(lambda item: type(item[1])==int ,prog_lang))
print(output_list)

#5.Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)

output_list=list(map(lambda item: (item[0].lower(),len(item[0])),prog_lang))
print(output_list)

#6.Generate a tuple in the form,
#("All languages separated by commas",
#"All versions separated by commas")

input_string = tuple(map(lambda item : (item[0]),prog_lang))
input_num_string = tuple(map(lambda item : (str(item[1])),prog_lang))
print((' '.join(input_string), ' '.join(input_num_string)))

print(reduce(lambda x,y:(f'{x[0]},{y[0]}',f'{x[1]},{y[1]}') , prog_lang))

'''Using a closure, create a function, multiples_of(n) which we can use to
create generators that generate multiples of n less than a given
number.'''

def multiples_of(n):
    def multiplier(x):
        for i in range(x):
            multiple=(i+1)*n
            if multiple<30:
                yield multiple
    return multiplier

m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(type(m3_under30))
# output: <class 'generator'>

print(*m3_under30)
# output: 3 6 9 12 15 18 21 24 27

print(*m7_under30)
# output: 7 14 21 28

#1.make_upper – make every letter of a string returned from the decorated
#function uppercase.
def make_upper(func):
    def upper_case():
        str = func()
        return str.upper()
    return upper_case


@make_upper
def hello_world():
    return 'hello young good day!!'
    

print(hello_world()) # output: HELLO YOUNG, GOOD DAY!!

#2.print_func_name – print the name of the decorated function before
#executing the function.

def print_func_name(func):
    def inner():
        print(func.__qualname__ +" is running...")
        print(func.__name__ + " is running...")
        func()
    return inner


@print_func_name
def my_func():
    print('Python is fun!!')

my_func() # output: my_func is running...
          # Python is fun

#3.give_name(name) – concatenate the given name at the end of a string
#returned from the decorated function.

def give_name(name):
    def inner(func):
        def wrapper():
            return func()+" "+name
        return wrapper
    return inner


@give_name('Theresa')
def greeting():
    return 'Hello'

print(greeting()) # output: Hello Theresa

#4.print_input_type – print a data type of the input argument before
#executing the decorated function.
def print_input_type(func):
    def inner(n):
        print("The input data type is ", type(n))
        return func(n)
    return inner

@print_input_type
def square(n):
    return n ** 2

print(square(3.5)) # output: The input data type is <class 'float'>
                   #12.25

#5.check_return_type(return_type) – check if the return type of the
#decorated function is return_type and print the result before executing
#the function.

def check_return_type(rtyp):
    #print(rtyp)
    def inner(func):
        def wrapper(n):
            #ret_type=type(func(n))
            #print(ret_type)
            if (type(func(n))==rtyp):
                print("The return type is",type(func(n),),func(n))
            else:
                print("---------Error!--------- The return type is NOT <class 'str'> ",func(n))
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

print(square(2.9)) # output: The return type is <class 'float' 8.41

#6.execute_log – write a function execution log on the log file.
def execute_log(func):
    def inner(*args):
        return(datetime.now(timezone.max),func(*args,),func.__name__)

    return inner
       

@execute_log
def multiply(*nums):
    mult = 1
    for n in nums:
        mult *= n
    return mult
@execute_log
def hello_world1():
    return 'hello world!!'

print(multiply(6, 2, 3)) # 36
print(hello_world1()) # hello world!!
print(multiply(2.2, 4)) # 8.8
print(hello_world1()) # hello world!!


