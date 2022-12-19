
#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.
def fizzbuzz(x):
    i =1
    for i in range(x+1):
        if i%3 == 0 and i%5 != 0:
             i = 'Fizz'
             print(i)
        elif (i%5 == 0 and i%3 != 0):
             i = 'Buzz'
             print(i)
        elif i%3 == 0 and i%5 == 0:
             i = 'FizzBuzz'
             print(i)
        else: 
             i = i
             print(i)

fizzbuzz(100)
            