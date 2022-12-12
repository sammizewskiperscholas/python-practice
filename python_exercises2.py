#####################################################################
# GENERATORS:
#####################################################################
# Generator exercises: Create a generator, primes_gen that generates prime numbers starting from 2.

import math

# use the principle that if a number have any factor less than the numbers square root, then the number cannot be prime

def isprime(n):
  if n == 2: return True
  nroot = int(math.sqrt(n))+ 1
  for i in range(2,nroot+1):
    if n % i == 0:
      return False
  return True  

def primes_gen():
  n = 2
  while True:
    if isprime(n):
      yield n
    n += 1

gen = primes_gen()
print('primes')
for _ in range(10):
  print(next(gen), end=' ')
#####################################################################  
#Create a generator, unique_letters that generates unique letters from the input string. It should generate the letters in the same order as from the input string.

def unique_letters(str):
  mem = [] # memory list to keep unique letters
  for lt in str:
    if lt not in mem:
      yield lt
      mem.append(lt)
print('\nUnique Letters:')
for letter in unique_letters('hello'):
  print(letter, end=' ')
  
#####################################################################
# LAMBDA FUNCTIONS
#####################################################################
#Consider the list:
prog_lang = [('Python', 3.8),
             ('Java', 13),
             ('JavaScript', 2019),
             ('Scala', 2.13)]

#1. Sort the list by each language's version in ascending order.

print(sorted(prog_lang, key = lambda x : x[1]))

#2. Sort the list by the length of the name of each language in descending order.

print(sorted(prog_lang, key = lambda x : len(x[0]), reverse=True))

#3. Filter the list so that it only contains languages with 'a' in it.

print(list(filter(lambda x : True if 'a' in x[0] else False, prog_lang)))

#4. Filter the list so that it only contains languages whose version is in integer form.
print(list(filter(lambda x : isinstance(x[1],int) , prog_lang)))
