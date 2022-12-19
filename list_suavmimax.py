
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






   