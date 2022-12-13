#**************************************************Generators Exercise*******************************************************

#1. Create a generator, primes_gen that generates prime numbers starting from 2.

def primes_gen():
    
    for i in range(2,30):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i

gen = primes_gen()

for _ in range(10):
    print(next(gen), end=' ')



# 2. Create a generator, unique_letters that generates unique letters from the input string. It should generate the letters in the same order as
# from the input string.

def unique_letters(name):
    uniqueLetter=set()
    for i in name:
        if i not in uniqueLetter:
            yield i
        uniqueLetter.add(i)
for letter in unique_letters('hello'):
    print(letter, end=' ')

#********************************************************Lambda Function Excersices********************************************************

#1. Sort the list by each language's version in ascending order.

prog_lang = [('Python', 3.8),
            ('Java', 13),
            ('JavaScript', 2019),
            ('Scala', 2.13)]

prog_lang.sort(key=lambda x: x[1])
print(prog_lang)

#2. Sort the list by the length of the name of each language in descending order.

prog_lang = [('Python', 3.8),
            ('Java', 13),
            ('JavaScript', 2019),
            ('Scala', 2.13)]

prog_lang.sort(reverse = True,key=lambda x: x[1])
print(prog_lang)

# 3. Filter the list so that it only contains languages with 'a' in it.

prog_lang = [('Python', 3.8),
            ('Java', 13),
            ('JavaScript', 2019),
            ('Scala', 2.13)]

a_word = list(filter(lambda x: 'a' in x[0], prog_lang))
print(a_word)



# 4. Filter the list so that it only contains languages whose version is in integer form.

prog_lang = [('Python', 3.8),
            ('Java', 13),
            ('JavaScript', 2019),
            ('Scala', 2.13)]

print(list(filter(lambda x: type(x[1])==int,prog_lang)))



#  5. Transform the list so that it contains the tuples in the form("language in all lower case", length of the language string)

prog_lang = [('Python', 3.8),
            ('Java', 13),
            ('JavaScript', 2019),
            ('Scala', 2.13)]
print(list(map(lambda x: (x[0].lower(),len(x[0])),prog_lang)))



# 6. Generate a tuple in the form,("All languages separated by commas","All versions separated by commas")

prog_lang = [('Python', 3.8),
            ('Java', 13),
            ('JavaScript', 2019),
            ('Scala', 2.13)]

a = tuple(map(lambda x: (x[0]), prog_lang))
b = tuple(map(lambda x : (str(x[1])),prog_lang))
print((' '.join(a),''.join(b)))