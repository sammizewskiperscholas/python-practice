prime=[]

for i in range(1,51):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime.append(i)
print(prime)

prime=[i]

prime=[]
for i in range(2, 51):
    if i == 2 or i == 3 or i == 5 or i == 7:
        prime.append(i)
    if i%2==0 or i%3==0 or i%5==0 or i%7==0:
        pass
    else:
        prime.append(i)
print(prime)

letters=["a", "b", "c", "d"]
dict={}
count=1
for i in letters:
    dict[count]=i

add_num={}
for num in range(1,11):
    add_num[num]= num+num

print(add_num)

# {key: value for loop }
add_num2={num: num+num for num in range(1,11)}
print(add_num2)




list=["FizzBuzz" if num % 15 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else num for num in range(1,101)] 
print(list)
