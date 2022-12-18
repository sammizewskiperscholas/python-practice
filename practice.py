#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def fizzbuzz(): 
  for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0: 
      print("FizzBuzz")
    elif i % 3 == 0: 
      print("Fizz")
    elif i % 5 ==0:
      print("buzz")
    else:
      print(i)

#fizzbuzz

#Use list comprehension for fizzbuzz problem 

fizzbuzzlist = ['Fizzbuzz' if i % 3 == 0 and i % 5 == 0 else 'fizz' if i % 3 == 0 else 'buzz' if i % 5 == 0 else i for i in range(1,51)]

# print(fizzbuzzlist)

# def dec(func, n):
#     def wrapper():
#         for _ in range(n):
#             func()
#     return wrapper
    
# @dec('say_hello', 5)
# def say_hello():
#     print('hello')

# #say_hello = dec(say_hello, 5)
# say_hello()

def dec(*args): 
    #print(type(args))
    #print(args)
    n = args[0]
    #print(n)
    def wrapper(func): 
        for _ in range(n):
            func()
    return dec
