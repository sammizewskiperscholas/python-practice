#! /usr/bin.env python3
from functools import reduce
# Generator exercises
#1
def primes_gen():
	n = 2
	while True:
		for i in range(2,n):
			if n % i ==0:
				break
		else:
			yield n
		n += 1 
		
gen = primes_gen()
for _ in range(10):
	print(next(gen), end=' ')

#2
def unique_letters(word):
	unique = []
	for i in word:
		if i not in unique:
			unique.append(i)
	return unique
for letter in unique_letters('hello'):
	print(letter, end = ' ')

# lambda Exercise
prog_lang = [('Python',3.8),('Java',13),('JavaScript',2019),('Scala', 2.13)]

#1
sort_lambda = sorted(prog_lang, key=lambda x: x[1], reverse=False)
print(sort_lambda)

#2
sort_length = sorted(prog_lang, key=lambda x:len(x[0]), reverse=True)
print(sort_length)

#3
filter_a = list(filter(lambda x: 'a' in x[0],prog_lang))
print(filter_a)

#4
filter_int = list(filter(lambda x: isinstance(x[1],int), prog_lang))
print(filter_int)

#5
map_pro = tuple(map(lambda x: (x[0].lower(),len(x[0])), prog_lang))
print(map_pro)

#6
separated = tuple(reduce(lambda x,y: ((str(x[0])+',' +str(y[0])),(str(x[1])+','+str(y[1]))), prog_lang))
print(separated)
