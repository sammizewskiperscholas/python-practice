
#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence. 
def fibchk(n):
    n1 = 0
    n2 = 1
    sum = 0
    for i in range(n):
        sum = n1 + n2
        n1 = n2
        n2 = sum 
        i+=1
        print(sum)
        

fibchk(50)

