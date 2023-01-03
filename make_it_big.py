#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def make_it_big(array):
   for i in range(len(array)):
        if array[i]>0:
            array[i]= "big"
   return array   
print(make_it_big([-1, 3, 5, -5]))    
   


