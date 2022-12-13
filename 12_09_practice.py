#!/usr/bin/env python
# coding: utf-8

#    # Python Practice  
#    
#    ### Ndugba

# ## Problem # 1
#  Biggie Size - Given a list, write a function that changes all 
#  positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) 
#  returns that same list, #changed to [-1, "big", "big", -5].

# In[1]:


def positive_numbers(list):
    for number in range(len(list)):
        if list[number] >0:
            list[number] ="big"
        else:
            return list
        return list


# In[2]:


example1= [-1,3,5,-5]


# In[3]:


print(positive_numbers(example1))


# In[ ]:





# ## Problem # 2
# 
# Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

# unsure what question is asking- shouldnt the above response be (-1,1,1,2) ? or (-1, 0, 1, 2)?

# In[ ]:





# In[ ]:





# ## Problem # 3
# #SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10

# In[4]:


##why doesnt this work?? but works below?
def sumtotal(list):
    return sum(list)


# In[5]:


def sum(list):
    counter = 0
    for number in range(len(list)):
        counter = counter + list[number]
    return counter


# In[6]:


example1= [1,2,3,4]


# In[7]:


print(sumtotal(example1))


# In[8]:


print(sum(example1))


# In[ ]:





# ## Problem # 4
# #Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5

# In[9]:


def average(list):
    return sum(list)/len(list)

  


# In[10]:


example1 = [1,2,3,4]


# In[11]:


print(average(example1))


# In[ ]:





# ## Problem # 5
# #Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4

# In[12]:


def length(list):
    return len(list)


# In[13]:


example1 = [1,2,3,4]


# In[14]:


print(length(example1))


# In[ ]:





# ## Problem # 6
# #Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
# 

# In[15]:


def min(list):
    return min(list)


# In[16]:


example1 = [1,2,3,4]
example2 = [-1,-2,-3]
example3 = [ , ]


# In[18]:


print(min(example1))
print(min(example2))
#print(min(example3))


# ## Problem # 7
# #Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

# In[19]:


def max(list):
    return max(list)


# In[21]:


example1 = [1,2,3,4]
example2 = [-1,-2,-3]
#example3 = [ , ]


# In[22]:


print(max(example1))
print(max(example2))
#print(max(example3))


# ## Problem # 8
# Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

# In[32]:


def stats(list):
    return max(list), min(list), (sum(list)/len(list)), sum(list)


# In[33]:


def stats1(list):
    return sum(list)


# In[34]:


example1 = [1,2,3,4]


# In[35]:


print(stats(example1))


# In[30]:


print(stats1(example1))


# In[31]:


print(average(example1))


# ## Problem # 9
# #ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

# In[27]:


def reverse(list):
    return(list[::-1])


# In[28]:


example1 = [1,2,3,4]


# In[29]:


print(reverse(example1))


# ## Problem # 10
# #Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

# In[36]:


def palindrome(string):
    string = string
    new_string = string[::-1]
    if new_string == string:
        return True
    else:
        return False


# In[37]:


string = 'radar'


# In[38]:


string2 = 'radarl'


# In[39]:


print(palindrome(string))


# In[40]:


print(palindrome(string2))


# ## Problem # 11
# #Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
#   #If the number is a multiple of 3, print “Fizz” instead of the number.
#   #If the number is a multiple of 5, print “Buzz” instead of the number.
#   #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

# In[41]:


def fizzbuzz(number):
    while number >=1 and number <=100:
        if number %3 ==0 and number %5 ==0:
            number = "FizzBuzz"
        elif number %3 ==0:
            number= "Fizz"
        elif number %5 ==0:
            number= "Buzz"
        else:
            number = number
        return number
    
    


# In[42]:


# if I wanted to return 

def fizzbuzz2(list):
    for number in range(len(list)):
        if list[number] %3 ==0 and list[number] %5 ==0:
            list[number] = "FizzBuzz"
        elif list[number] %3 ==0:
            list[number]= "Fizz"
        elif list[number] %5 ==0:
            list[number]= "Buzz"
        else:
            list[number] = list[number]
    return list[number]
    


# In[43]:


number1 = (33)
number2 = (15)
number3 = (13)
number4 = (25)


# In[44]:


number5 = [33, 15, 13, 25, 26, 72]


# In[45]:


print(fizzbuzz(number1))
print(fizzbuzz(number2))
print(fizzbuzz(number3))
print(fizzbuzz(number4))


# In[46]:


print(fizzbuzz2(number5))


# ## Problem # 12
# #Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
#   #F(0) = 0, F(1) = 1
#   #F(n) = F(n - 1) + F(n - 2), for n > 1.
#   #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

# In[47]:


#assuming postive numbers
def Fibonacci(number):
    if number < 0:
        return False
    elif number ==0:
        number =0
    elif number ==1:
        number= 1
    else:
        number = (number - 1) + (number - 2)
    return number


# In[48]:


number1 = (-5)
number2 = (0)
number3 = (1)
number4 = (5)
number5 = (30)


# In[49]:


print(Fibonacci(-5))
print(Fibonacci(0))
print(Fibonacci(1))
print(Fibonacci(5))
print(Fibonacci(30))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




