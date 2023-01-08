#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, 
#called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

def Fibonacci(n):
   
    if  n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
       return Fibonacci(n -1) + Fibonacci(n - 2)

print(Fibonacci(9))