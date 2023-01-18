def dec(func):
    def wrapper(n):
        for _ in range(n):
            func()
    return wrapper
    
@dec
def say_hello():
    print('hello')

say_hello(5)

# print(dec(say_hello))

# run_w = dec(say_hello)
# print(run_w(5))

# print(globals())
