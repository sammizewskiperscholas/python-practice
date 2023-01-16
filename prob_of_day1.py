#Problem1
def sortfirstnames(list1):
     sortedlist = []
 
     for i in list1:
        sortedlist.append(i.split())
     list1 = []
 
 
     for i in sorted(sortedlist, key=lambda x: x[0]):
        list1.append(' '.join(i))
 
 
     return list1
    
list2 = ["Benjamin Witter", "Sammi Grego", "Valerie Boss"]
print("Ascending by the first name formatted with first name first")
print(sortfirstnames(list2))

#Problem2
def sortlastnames(list3):
     sortedlast = []
 
 
     for i in list3:
        sortedlast.append(i.split())
     list3 = []
 
     for i in sorted(sortedlast, key=lambda x: x[-1]):
        list3.append(' '.join(i))
 
  
     return list3
    
teachers = ["Benjamin Witter", "Sammi Grego", "Valerie Boss"]
print("Ascending by the last name formatted with first name first")
print(sortlastnames(teachers))


#Problem3
def sortlastnames(list4):
     sortedlastdesc = []
     swaplist = []
 
  
     for i in list4:
        swaplist.append(i.split()[::-1])
     print(swaplist)
     list4 = []

     
     for i in sorted(swaplist, key=lambda x: x[0]):
         list4.append(' '.join(i))
        
    
     return list4


teachers3 = ["Benjamin Witter", "Sammi Grego", "Valerie Boss"]
print("Descending by the last name formatted with last name first")
print(sortlastnames(teachers3))

