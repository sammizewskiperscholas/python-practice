import sys
mytuple = ("tim","john","jenny","jack")
print(type(mytuple))

print(mytuple[0])

# mylist=list(mytuple)
# print(mylist)
# mytuple=tuple(mylist)
# print(mytuple)

ct=mytuple.count("sam")
print(ct)

print(mytuple[::-1])

a=("john",26,"Boston")
print(type(a))
name,age,place=a

print(type(name))
print(type(age))
print(place)
print(type(a))

number_list=[1,2,3,4,5,6,7,8,9]
number = (1,2,3,4,5,6,7,8,9)
*i1,i2=number
print(i2)
print(sys.getsizeof(number_list),bytes)
print(sys.getsizeof(number),bytes)

import timeit

print(timeit.timeit(stmt="[1,2,3,4,5]",number=100))#7.499994...
print(timeit.timeit(stmt="(1,2,3,4,5)",number=100)) # tuple is more efficient than list- 2.00092
print(timeit.timeit(stmt='{"a":1,"b":2,"c":3,"d":4,"e":5}',number=100))#1.22
print(timeit.timeit(stmt='"12345"',number=100))#2.20001675..












