#practice on Generator,lamda
from functools import reduce
#1. Use list comprehension to create a list containing a solution for the
#famous FizzBuzz problem. For integers 1 to 100, inclusively, the value
#should be:
# 'Fizz' if divisible by 3
# 'Buzz' if divisible by 5
# 'FizzBuzz' if divisible by both 3 and 5
# The integer itself if not divisible by both 3 and 5
list2=['FizzBuzz'  if (num%3==0 and num%5==0) else "Fizz" if (num%3==0)else  "Buzz"if (num%5==0) else num  for num in range(1,101)]
print(list2)

#1. Create a generator, primes_gen that generates prime numbers
#starting from 2.
def primes_gen():
    i = 2
    while i < 100 :
        prime = True # reset the `prime` variable before the inner loop
        for a in range(2, i):
            if i%a == 0:
                prime = False
                break
        if prime:    
            yield i
        i += 1 # don't forget to advance `i`

gen = primes_gen()
for _ in range(10):
   print(next(gen), end=' ')
print(end='\n')
#2. Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.
def unique_letters(str1):
    unique=""
    for i in str1:
        if i not in unique:
            unique=unique+' '+i
    yield unique
for letter in unique_letters('hello'):
    print(letter, end=' ')
print(end='\n')

#Consider the list:

#1. Sort the list by each language's version in ascending order.
prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]
list1=prog_lang
list1.sort(key=lambda x: x[1])
print(list1)
#2. Sort the list by the length of the name of each language in descending
##order.
list2=prog_lang
list2.sort(key=lambda x: len(x[0]),reverse=True)
print(list2)
#3. Filter the list so that it only contains languages with 'a' in it.
prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]
list3=list(filter(lambda x: 'a' in x[0], prog_lang))
print(list3)
#4. Filter the list so that it only contains languages whose version is in int
list4=list(filter(lambda x: type(x[1])== int, prog_lang))
print(list4)
#5. Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)
list5=list(map(lambda x  : (x[0].lower(),len(x[0])), prog_lang))
print(list5)
#6. Generate a tuple in theform,
#("All languages separated by commas",
#"All versions separated by commas")
print(reduce(lambda x,y :(f'{x[0]},{y[0]}',f'{x[1]},{y[1]}'),prog_lang))




