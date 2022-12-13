prog_lang = [
    ('Python', 3.8),
    ('Java', 13),
    ('JavaScript', 2019),
    ('Scala', 2.13)
    ]

#1. Sort the list by each language's version in ascending order.

prog_lang.sort(key=lambda item:item[1])
print(prog_lang)

#2. Sort the list by the length of the name of each language in descending order.

prog_lang.sort(key=lambda item:len(item[0]),reverse= True)
print(prog_lang)

#3. Filter the list so that it only contains languages with 'a' in it.
print(list(filter(lambda item : "a" in item[0], prog_lang)))

#4. Filter the list so that it only contains languages whose version is in integer form.
print(list(filter(lambda item : type(item[1]) == int, prog_lang)))


#5. Transform the list so that it contains the tuples in the form, ("language in all lower case", length of the language string)
print(list(map(lambda item :  (item[0].lower(), len(item[0])),prog_lang)))

#6. Generate a tuple in the form, ("All languages separated by commas", "All versions separated by commas")
a = tuple(map(lambda item : (item[0]),prog_lang))
b = tuple(map(lambda item : (str(item[1])),prog_lang))
print((' '.join(a), ' '.join(b)))


# 2. Create a generator, unique_letters that generates unique letters from
# the input string. It should generate the letters in the same order as
# from the input string.

def unique_letter(name):
    a = []
    for i in name:
        if i not in a:
            yield i
        a.append(i)
  
for letter in unique_letter("hello"):
    print(letter, end =" ")
print()

# 1. Create a generator, primes_gen that generates prime numbers
# starting from 2.

def prime_gen():
    end = int(input("Enter Number :"))
    for i in range(2, end):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            yield i

gen = prime_gen()
for _ in range(10):
    print(next(gen), end =" ")
