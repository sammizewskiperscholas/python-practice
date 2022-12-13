from functools import reduce
from fractions import Fraction
# QUESTIONS

# Slide 19 Question

prog_lang = [
    ('Python', 3.8), 
    ('Java', 13), 
    ('JavaScript', 2019), 
    ('Scala', 2.13)]

# 1
# Sort the list by each languages version in ascending order

prog_lang_version = sorted(prog_lang, key=lambda x: x[1])  
# returns new list sorted by defined iterable
# sorted(iterable, key)
# ascending by default 
print(prog_lang_version) 

# 2
# Sort the list by the length of the name of each language 
# in descending order. 

prog_lang_length = sorted(prog_lang, key=lambda x: len(x[0]), reverse=True)
print(prog_lang_length)
# reverse=True == Descending

# 3
# Filter the list so that it only contains languages with 'a' in it.
prog_lang_a_only_filter = list(
    filter(lambda language: "a" in language[0], prog_lang))  #func, arg
print(prog_lang_a_only_filter)

# 4
# Filter the list so that it only contains languages whos version is
# in integer form

prog_lang_version_int = list(
    filter(lambda language : type(language[1]) == int, prog_lang))
print(prog_lang_version_int)

# 5
# transform list, tuples w/
# lowercase, len of lang string
# can't mutate tuples, need to make new list

prog_lang_lower_len = map(
    lambda language : (language[0].lower(),len(language[0])), prog_lang)

print(list(prog_lang_lower_len))

# the trick here is not to get caught up with trying to use multiple variables,
# all you need to do is have a variable for the given tuple, and assign
# multiple operations for given values in the tuple
# the given values being tuple of index 0

# 6
# generate a tuple in the form 
# (all languages, all versions)

# DEBUG LIST COMP 
#names = [language[0] for language in prog_lang]
#print(names)

#lang = [language[1] for language in prog_lang]
#print(lang)


#prog_concat = lambda language: tuple(([language[0] for language in language], [language[1] for language in language]))
#print(prog_concat(prog_lang))
# DEBUG LIST COMP 


#EXPLINATION FOR LAMBDA FUNCTION BELOW:
# for all tuples:
# extracting all index 0 vals and concatenating
# extracting all index 1 vals and concatenating
# need to concat as str for both
# wrapped in parenthesis, implicitly defined tuple
# pro tip I learned 💪🏻 you can re-use the same container over and over in different ways if you wrap the function in parenthesis 
# container : (operation(s) for container object [0], operation(s) for container object [1])

prog_concat_str = lambda language : (", ".join(str(language[0]) for language in language) , ", ".join(str(language[1]) for language in language)) # 🔥 spicy
print(prog_concat_str(prog_lang))


# HACKER-RANK Q'S

# Map function
# Cubes of fibbonaci numbers

cube = lambda x : x ** 3

def fibbonacci(n):
    if n == 0:
        return [] # return empty set b/c its asking for an amount of nums, not sequence in range(nums)
    start = [0, 1]
    for _ in range(n - 1):  # same func I wrote before but this one doesn't want to include end range
        start.append(sum(start[-2:]))
    start.pop()
    return start  # returns list

print(fibbonacci(5))

print(list(map(cube, fibbonacci(0))))


# reduce
#n rep how many
# num / denom
# product
# LCM 

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)  # input from above func
    # stored as t
    return t.numerator, t.denominator

# have to read on this module




# validate email address w/ a filter
# n for n emails
# print only valid emails
# name@name.extension
# max len of extension is 3


def fun(s):
    digest = '' + s
    if "@" in digest and "." in digest:
        at_finder = digest.find("@")
        dot_finder = digest.find(".")
        #print(digest[at_finder + 1:dot_finder])
        if digest[at_finder + 1 :dot_finder].isalnum() and digest.find("@")!= 0:
            #print(digest[at_finder - 1])
            if len(digest[dot_finder + 1:]) <= 3 and digest[dot_finder + 1:].isalpha(): 
                digest = digest.replace("@", '')
                digest = digest.replace(".", '')
                #print(digest)
                if "-" in digest:
                    digest = digest.replace("-", '')
                if "_" in digest:
                    digest = digest.replace("_", '')
                    #print(digest)
                if digest.isalnum():
                    return s
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

list_emails = ["daniyal@gmail.coma", 
    "its@gmail.com1", 
    "rase23@ha_ch.com", 
    "hotdog@hotdog.com", # 🌭
    "sone.com",
    "@something.co1",  # check extension - done
    "@something.com"]  # check front - done
list_comp_e = [fun(email) for email in list_emails]
print(list_comp_e)

# this is super hacky. Regex would come in clutch but this works for now. 