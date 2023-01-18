from functools import reduce
print([i for i in range(1,101) if all(i%j != 0 for j in range(2,i))])

#prime = [i for i in range(1,51) if (i%2 != 0 and i%3!=0 and i%5!=0 and i%7!=0) or (i==1 or i==2 or i==3 or i==5 or i==7)]
#print(prime)

#print(["FizzBuzz" if n%3==0 and n%5==0 else "Buzz" if n%5==0 else "Fizz" if n%3==0 else n  for n in range(1,16)])


numbers =[1,2,3,4]
#print(list(filter(lambda x : x**2, numbers)))
#print(map(lambda x : x**2, numbers))
print("Fibbonacci Numbers")
print([reduce(lambda x, y : x+y, numbers)] )

my_list = ['python', 'java', 'scala', 'javascript']

#Consider the list:
prog_lang = [('Python', 3.8), ('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]

#1. Sort the list by each language's version in ascending order.
def version_sort(pl):
  pl_sort = sorted(pl, key=lambda t : t[1])
  return pl_sort

print(version_sort(prog_lang))

#2. Sort the list by the length of the name of each language in descending order.

def lname_len_sort(pl):
  lname_len_sort = sorted(pl, key=lambda t : len(t[0]), reverse = True)
  return lname_len_sort

print(lname_len_sort(prog_lang))

#3. Filter the list so that it only contains languages with 'a' in it.

def filter_alang_pl(pl):
  pl_fil = list(filter(lambda t : "a" in t[0].lower(), pl))
  return pl_fil

print(filter_alang_pl(prog_lang))


#4. Filter the list so that it only contains languages whose version is in integer form

def filter_intver_pl(pl):
  pl_fil = list(filter(lambda t : type(t[1]) == int, pl))
  return pl_fil

print(filter_intver_pl(prog_lang))

#5. Transform the list so that it contains the tuples in the form, ("language in all lower case", length of the language string)

def tuple_lang_len(pl):
  pl_tup = (*map(lambda t : t[0].lower()+", "+ str(len(t[0])), pl),)
  return pl_tup

print(tuple_lang_len(prog_lang))

#6. Generate a tuple in the form, ("All languages separated by commas", "All versions separated by commas")

def tuple_lang_ver(pl):
    pl_tup = (*map(lambda t : t[0], pl),)
    return pl_tup

print(tuple_lang_ver(prog_lang))

def fun(s):
    print(split(s))

print(reduce(lambda x,y :(f'{x[0]},{y[0]}',f'{x[1]},{y[1]}'),prog_lang))


print(fun("sushama.cardozo@gmail.com"))

def outer(msg):
    lang = 'Python'
    def inner():
        print(lang, msg)
    return inner

my_func = outer('is fun!!!')
my_func() # output: 'Python is fun!!!'

##############################################################################
############### create a closure #############################################
def multiples_of(n):
    def multiply(k):
        print([i for i in range(n, k, n)])
    return multiply

m3 = multiples_of(3)
m5 = multiples_of(5)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(m3(60))
print(type(m3))

print(m5(50))
print(type(m5))

print(m3_under30)
print(type(m3_under30))


