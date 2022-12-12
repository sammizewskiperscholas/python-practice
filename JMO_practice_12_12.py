#Consider the list:
prog_lang = [('Python', 3.8),
             ('Java', 13),
             ('JavaScript', 2019),
             ('Scala', 2.13)]
#1. Sort the list by each language's version in ascending order.
ascend = sorted(prog_lang, key=lambda x: x[1])
print(ascend)

#2. Sort the list by the length of the name of each language in descending order.
dlname = sorted(prog_lang, key=lambda x: len(x[0]), reverse = True)
print(dlname)

#3. Filter the list so that it only contains languages with 'a' in it.
a = list(filter(lambda x: 'a' in x[0], prog_lang))
print(a)

#4. Filter the list so that it only contains languages whose version is in integer form. 
integers = list(filter(lambda x: isinstance(x[1], int), prog_lang))
print(integers)

#5. Transform the list so that it contains the tuples in the form, 
# ("language in all lower case", length of the language string)
def newlist(old):
    new = []
    new2 = []
    new3 = []
# "new" gets the names, new2 gets the lengths:
    for x in old:
        new.append(x[0].lower())
        new2.append(len(str(x[0])))
# new3 is made of tuples combining new and new2 at the same index
    for i in range (len(new)):
        new3.append((new[i], new2[i]))
    return new3
print(newlist(prog_lang))

#6. Generate a tuple in the form, ("All languages separated by commas",
# "All versions separated by commas")
def newtuple(old):
    new = []
    newstring = ''
    new2 = []
    new2string = ''
    for x in old:
        new.append(x[0])
        new2.append(x[1])
#new holds the names, new2 holds the values
    for y in new:
        newstring += y
        newstring += ','
    newstring = newstring[:-1]
#newstring takes everything in new, followed by a comma, into a string - then the last character is removed
    for z in new2:
        new2string += str(z)
        new2string += ','
#new2string does the same as above, for new2
    new2string = new2string[:-1]
    new3 = newstring, new2string
    return new3
print(newtuple(prog_lang))
