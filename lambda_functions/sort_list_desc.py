#Sort the list by the length of the name of each language in descending
#order.

prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]

prog_lang.sort(key = lambda x: x[1],reverse=True)
print(prog_lang)