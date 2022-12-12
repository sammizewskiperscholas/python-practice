
#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5
def avglist(lista):
    sumvalue = 0
    avgvalue = 0
    for i in lista:
       sumvalue = sumvalue + i
    avgvalue = sumvalue/len(lista) 
    return avgvalue

avg1 = print(avglist([1,2,3,4]))       