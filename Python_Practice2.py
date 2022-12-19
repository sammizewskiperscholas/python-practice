
#Without List Comprehension
my_list = []
for e in range(1, 10, 2):
    my_list.append(e**2)
print(my_list)
#With List Comprehension
my_list = [e**2 for e in range(1, 10, 2)]
print(my_list)

#Without List Comprehension
my_list = []
for e in range(10):
    if e%2 == 1:
        my_list.append(e**2)
print(my_list)
#With comprehension
my_list = [e**2 for e in range(10) if e%2 == 1]
print(my_list)

#multiple conditional statements using ternary operators:
grades = [95, 55, 83, 75, 91]
grades_l = [('A' if g>=90 else ('B' if g>=75 else 'C')) for g in grades]
print(grades_l)
# OR

grades_l = []
for g in grades:
   if g >= 90:
      grades_l.append('A')
   elif g >= 75:
      grades_l.append('B')
   else:
      grades_l.append('C')
print(grades_l)

#nested for loops
pairs = []
for i in range(3):
  for j in range(2):
    pairs.append((i, j))
print(pairs)

#Generator Example1:
def powers_of_two():
   n = 1
   while True:
      n *= 2
      yield n
      
powers = powers_of_two()
for _ in range(20):
      print(next(powers))
      squares = (i**2 for i in range(20))
for s in squares:
      print(s)

#Generator Example2
def even_n(max_n = 1):
    n =1
    while n <= max_n:
        yield n*2
        n +=1

i = even_n(3)
print(next(i))
print(next(i))
print(next(i))

#Prime_number Generator
def primes_gen():
    for n in range(2, 100):     # n starts from 2 to end
        for x in range(2, n):   # check if x can be divided by n
            if n % x == 0:      # if true then n is not prime
                break
        else:                   # if x is found after exhausting all values of x
            yield n             # generate the prime

gen = primes_gen()       
for _ in range(10):
    print(next(gen), end=' ')

#Unique Letters generator
def unique_str(my_str):
    char_seen = []
    for char in my_str:
        if char not in char_seen:
            char_seen.append(char)
    yield (''.join(char_seen))


# For loop to reverse the string
for char in unique_str("Hello"):
    print(char, end = ' ')

#Sort the list by each language's version in ascending order.
prog_lang = [('Python', 3.8), ('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]
new_list = sorted(prog_lang, key = lambda x : x[1], reverse = True)
print(new_list)

#Sort the list by the length of the name of each language in descending order.
prog_lang = [('Python', 3.8), ('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]
new_list2 = sorted(prog_lang, key = lambda x : x[1], reverse = False)
print(new_list2)

new_list4 = list(filter(lambda x: x[1] 'a', prog_lang))
print(new_list4)


