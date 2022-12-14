#list comprehension
expression for variable in sequence (optional predicate)
my_list=[]
for i in range(1,10,2):
    my_list.append(i**2)

my_list2=[i**2 for i in range(1,10,2)]
print(my_list)
print(my_list2)

odd_square=[]
for x in range(1,11):
    if x % 2==1:
        odd_square.append(x**2)

odd_square2 = [x**2 for x in range(1,11) if x %2 ==1]  
 print(odd_square2)      


def dec(func, n):
    def wrapper():
        for _ in range(n):
            func()
    return wrapper
    
@dec
('say_hello', 5)
def say_hello():
    print('hello')

#say_hello = dec(say_hello, 5)
say_hello()

