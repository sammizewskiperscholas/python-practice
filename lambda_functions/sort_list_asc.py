# Sort the list by each language's version in ascending order.

prog_lang = [('Python', 3.8),
('Java', 13),
('JavaScript', 2019),
('Scala', 2.13)]

prog_lang.sort(key = lambda x:x[1])
print(prog_lang)




