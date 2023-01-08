#Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)

from functools import reduce

prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]

generate_tuple = reduce(lambda x, y:(x[0]+','+y[0], str(x[1]) +',' + str(y[1])),prog_lang)
print(generate_tuple)