#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def fizz_buzz(start,end):
    numbers = []
    for n in range(start,end+1):
        if n % 3 == 0 and n % 5 == 0:
            numbers.append("FizzBuzz")
        elif n % 3 == 0:
            numbers.append("Fizz")
        elif n % 5 == 0:
            numbers.append("Buzz")
        else:
            numbers.append(n)
    return numbers

print(fizz_buzz(1, 100))