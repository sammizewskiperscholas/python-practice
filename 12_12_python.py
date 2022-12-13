#Create a generator, primes_gen that generates prime numbers starting from 2.
#############################################################################
# Generator Excercises
#############################################################################

# Generator function to generate prime numbers till 30
def primes_gen():
       # Looping through numbers from 2 to 30
       for prime in range(2,30):
        for number in range(2,prime):
            # Checking if the number is prime
            if prime%number==0:
                break
        else:
            yield prime

gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')


# Create a generator, unique_letters that generates unique letters from
# the input string. It should generate the letters in the same order as
# from the input string.
#Function to generate unique letters from a given string
def unique_letters(text):
    str = ""
    #Looping through the string
    for i in text:
        #Checking if the letter is not in the result string
        if i not in str:
            #Concatenating to the result string if it is the first occurence of the letter in the input string
           str += i
    yield str 
   
for letter in unique_letters('hello'):
    print(letter, end=' ')

#############################################################################
# Lambda Excercises
#############################################################################

# # Sort the list by each language's version in ascending order.
prog_lang = [('Python', 3.8), ('Java', 13), ('Javascript', 2019), ('Scala', 2.13)]
prog_lang.sort(key=lambda x: x[1])
print(prog_lang)

# Sort the list by the length of the name of each language in descending order.
#prog_lang = [('Python', 3.8), ('Java', 13), ('Javascript', 2019), ('Scala', 2.13)]
prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]
prog_lang.sort(key=lambda x: len(x[0]), reverse = True)
print(prog_lang)

# Filter the list so that it only contains languages with 'a' in it.
#filter_list = list(filter(lambda x: 'a' in x[0]), prog_lang)
prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]
print(list(filter(lambda x: 'a' in x[0], prog_lang)))


#Filter the list so that it only contains languages whose version is in integer
#form.
prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]
# Filtering the version with only integers
print(list(filter(lambda x: type(x[1])==int,prog_lang)))

# Transform the list so that it contains the tuples in the form,
# ("language in all lower case", length of the language string)
prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]
print(list(map(lambda x: (x[0].lower(),len(x[0])),prog_lang)))

#Generate a tuple in the form,
#("All languages separated by commas",
#"All versions separated by commas")
prog_lang = [('Python', 3.8),
            ('Java', 13),
            ('JavaScript', 2019),
            ('Scala', 2.13)]
all_languages = tuple(map(lambda x: (x[0]), prog_lang))
all_versions = tuple(map(lambda x : (str(x[1])),prog_lang))
# Joining all the languages by commas and all the versions by comma
print((','.join(all_languages),','.join(all_versions)))


