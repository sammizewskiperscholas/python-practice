myset=set("hello")
print(myset)

myset1=set()#set is mutable
print(type(myset1))

myset1.add(1)
myset1.add(20)
myset1.add(30)

print(myset1)

myset1.remove(1)
print(myset1)
# myset1.remove(40)
# myset1.discard(40)
myset1.pop()

print(myset1)

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes={2,3,5,7}

u=odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i1=odds.intersection(primes)
print(i1)


setA = {1,2,3,4,5,6,7,8,9,13}
setB={1,2,3,10,11,12,13}

diff = setB.difference(setA)
print(diff)

symdiff = setB.symmetric_difference(setA)
print(symdiff)

# setA.update(setB)
# print(setA)

# setA.intersection_update(setB)
# print(setA)

# setB.difference_update(setA)
# print(setB)

# setA.symmetric_difference(setB)
# print(setA)
setA = {1,2,3,4,5,6,7,8,9,13}
setB={1,2,3,13}
setC={45,50}
print(setB.issuperset(setA))
print(setB.issubset(setA))

print(setC.isdisjoint(setA))

# setD=setC
setD=setC.copy()
setC.add(100)
print(setD)
print(setC)

#frozenset is immutable--"we cannot modify or add or delete the element"

a=frozenset([1,2,3,4])
b=frozenset([8,9])

print(a.union(b))

print(a)
