#Generator Exercises
#Create a generator, primes_gen that generates prime numbers starting from 2.

def is_prime(n):
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
def primes_gen():
    n=2
    while True:
        if is_prime(n):
            yield n
        n+=1
        
gen=primes_gen()
for _ in range(10):
    print(next(gen),end=' ')

#Create a generator, unique_letters that generates unique letters from the input string. It should generate the letters in the same order as from the input string.
def unique_letters(string):
    seen = set()
    for letter in string:
        if letter not in seen:
            yield letter
            seen.add(letter)
for letter in unique_letters('hello'):
    print(letter, end=' ')





#Lambda Exercises
prog_lang = [('Python', 3.8), ('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]

#Sort the list by each language's version in ascending order
prog_lang.sort(key=lambda x: x[1])
print(prog_lang)

#Sort the list by the length of the name of each language in descending order.
prog_lang.sort(key=lambda x: len(x[0]), reverse=True)
print(prog_lang)

#Filter the list so that it only contains languages with 'a' in it.
prog_lang = list(filter(lambda x: 'a' in x[0], prog_lang))
print(prog_lang)

#Filter the list so that it only contains languages whose version is in integer form.
prog_lang = list(filter(lambda x: isinstance(x[1], int), prog_lang))
print(prog_lang)

prog_lang1 = [('Python', 3.8), ('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]
#Transform the list so that it contains the tuples in the form "language in all lower case", length of the language string
prog_lang1 = list(map(lambda x: (x[0].lower(), len(x[0])), prog_lang1))
print(prog_lang1)

#Generate a tuple in the form, ("All languages separated by commas", "All versions separated by commas")
prog_lang2 = [('Python', 3.8), ('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]
prog_lang2 = (", ".join(map(lambda x: x[0], prog_lang2)), ", ".join(map(lambda x: str(x[1]), prog_lang2)))
print(prog_lang2)

