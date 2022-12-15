# Create a generator, primes_gen that generates prime numbers starting from 2.
def gen_primes(N):
    prime_numbers = set()
    for n in range(2, N):
        if all(n % p > 0 for p in prime_numbers):
            prime_numbers.add(n)
            yield n
print(*gen_primes(10))

# The list 
prog_lang = [('Python', 3.8),
             ('Java', 13),
             ('JavaScript', 2019),
             ('Scala', 2.13)]

# Sort the list by each language's version in ascending order.

print(sorted(prog_lang, key= lambda x: x[1]))

# Sort the list by the length of the name of each language in descending order.

print(sorted(prog_lang, key= lambda x: len(x[0]), reverse= True))

# Filter the list so that it only contains languages with 'a' in it.

print(list(filter(lambda x: True if 'a' in x[0] else False, prog_lang)))

# Transform the list so that it contains the tuples in the form,("language in all lower case", length of the language string)

print(list(map(lambda x: (x[0].lower(), len(x[0])), prog_lang)))

# Filter the list so that it only contains languages whose version is in integer form.

print(list(filter(lambda x: isinstance(x[1],int), prog_lang)))