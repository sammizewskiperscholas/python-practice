def outer(msg):
   lang = 'Python'
   print(locals())
   def inner():
     print(lang, msg)
   inner()

outer('is fun!!!')


#Want a closure that take 2 numbers and sum
#def sum(num1):

def make_multiplier_of(n):
    def multiply(k):
        return k * n
    return multiply

multiplier3 = make_multiplier_of(3)
print(multiplier3(5))

#def dec(func, n):
#    def wrapper():
#        for _ in range(n):
#            func()
#    return wrapper
    
#@dec.wraps(func, 5)
#def say_hello():
#    print('hello')

#say_hello = dec(say_hello, 5)
#say_hello()

def make_multiplier_of(n):
    def multiply(k):
        return k * n
    return multiply

m3_under30 = make_multiplier_of(3)
print(type(m3_under30))


def make_multiplier_of(n):
    def multiply(*k):
        for x in range(k):
            return x * n            
    return multiply

multiplier3 = make_multiplier_of(5)
print(*multiplier3)

def multiplier(*x):
    return x * 2

print(multiplier(3,4))



