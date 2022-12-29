# import random
# a=random.randint(1,20)
# print(a)

# b = random.random()
# print(b)

import random
a = random.random()
print(a)
a = random.uniform(1, 10)
print(a)
a = random.randint(1, 10) # This will include the upper bound
print(a)
a = random.randrange(1, 10) #upper range not included
print(a)
a = random.normalvariate(0, 1)# return a random with a mean of zero and std. deviation of 1
print(a)
mylist = list("ABCDEFGH")
print(mylist)
a = random.choice(mylist) # Pick a random element
print(a)
a = random.sample(mylist, 3)
print(a)
a = random.choices(mylist, k=3) # to pick elements multiple times
print(a)
a = random.shuffle(mylist) #it will shuffle the order pf elements in the list
print(mylist)
random.seed(1) # Can reproduce the data and print the exact same results with the seed number
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
# Since the seed can reproduce the random numbers it is advisable to use
# the secret module for security purposes
import secrets
a = secrets.randbelow(10) # upper bound not included
print(a)
a  =secrets.randbits(4)
# 4 bits means it can have 4 different random binary values
# the highest possible numbe rin this case is 1111
# which is 15. It will generate a number from 0-15
print(a)
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)
# import numpy as np
# # numpy random generator uses a different random number generator
# a = np,random.rand(3)
# print(a)
# a = np,random.rand(3, 3)
# print(a)
# a = np,random.randint(0, 10, 3)
# print(a)
# a = np,random.randint(0, 10, (3, 4))
# print(a)
# arr = np.array([1,2,3], [4,5,6], [7,8,9])
# print(arr)
# np.random.shuffle(arr)
# print(arr)
# np.random.seed(1)
# print(np.random.rand(3,3))
# np.random.seed(1)
# print(np.random.rand(3,3))

