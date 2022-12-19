
#Python Practice Problems Assignment
#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def make_it_big(array):
   for i in range(len(array)):
        if array[i]>0:
            array[i]= "big"
   return array   
print(make_it_big([-1, 3, 5, -5]))    

#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def count_positives(array):
    count = 0
    for val in array:
        if val > 0:
            count += 1
    array[len(array)-1] = count
    return array
print(count_positives([-1,1,1,1]))

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10
def sumlist(lista):
    sumtotal = 0
    for i in lista:
        sumtotal = sumtotal + i
    return sumtotal
a = print(sumlist([1, 2, 3,4]))

#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5
def avglist(lista):
    sumvalue = 0
    avgvalue = 0
    for i in lista:
       sumvalue = sumvalue + i
    avgvalue = sumvalue/len(lista) 
    return avgvalue

avg1 = print(avglist([1,2,3,4]))       

#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4
def lenlist(list1):
    return len(list1)
len1 = print(lenlist([1,2,3,4]))

#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def min_list(list1):
     if list1 == []:
        return False
     else:   
        return min(list1)

min1 = print(min_list([1,2,3,4]))
min2 = print(min_list([-1,-2,-3]))
min3 = print(min_list([]))

#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def max_list(list1):
     if list1 == []:
        return False
     else:   
        return max(list1)

max1 = print(max_list([1,2,3,4]))
max2 = print(max_list([-1,-2,-3]))
max3 = print(max_list([]))

#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.
def d_suavmima(list1):
    sumlist = sum(list1)
    avglist = sum(list1)/len(list1)
    minlist = min(list1)
    maxlist = max(list1)
    lenlist = len(list1)
    list2  = ['sumlist', 'avglist', 'minlist', 'maxlist', 'lenlist']
    list3  = [sum(list1), sum(list1)/len(list1), min(list1), max(list1), len(list1)]
    i = iter(list2)
    j = iter(list3)
    dic1  = dict(zip(i, j))
    return dic1

dict1 = print(d_suavmima([1,2,3,4]))

#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverse_list(list1):
    left = 0
    right = len(list1) - 1
    while (left < right):
        temp = list1[left]
        list1[left] = list1[right]
        list1[right] = temp
        left+=1
        right-=1
    return list1

revlist1 = print(reverse_list([1,2,3,4,5]))

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
def palindromchk(str1):
    revstr1 = ""
    for i in str1:
        revstr1 = i + revstr1
    if (str1 == revstr1):
        return 'Yes'
    else:
        return 'No' 

chk1 = print(palindromchk('12321'))      

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


