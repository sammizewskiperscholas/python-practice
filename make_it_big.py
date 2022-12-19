#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def make_it_big(array):
   for i in range(len(array)):
        if array[i]>0:
            array[i]= "big"
   return array   

print(make_it_big([-1, 3, 5, -5]))    
   
def count_positives(array):
   count = 0
   for val in array:
        if val > 0:
            count += 1
   array[len(array)-1] = count
   return array


print(count_positives([-1,1,1,1]))