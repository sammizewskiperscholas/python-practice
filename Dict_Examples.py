x = {}
print(type(x))
file_counts = {"jpig":10,"txt":14,"csv":2,"py":23}
print(len(file_counts))
print(file_counts)
print(file_counts["txt"])
print("jpig" in file_counts)
file_counts["cfg"] = 8
file_counts["csv"]=17
print(file_counts)
del file_counts["cfg"]
print(file_counts)

#***************************************************************************
file_counts = {"jpig":10,"txt":14,"csv":2,"py":23}
for extension in file_counts:
    print(extension)
for ext,amount in file_counts.items():
    print("There are {} files with .{} extension".format(amount,ext))
print(file_counts.keys())
print(file_counts.values())

#***************************************************************

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key, value in cool_beasts.items():
    print("{} have {}".format(key,value))

#*********************************************************************

dict = {1:'one',2:'two',2:'twoooo'}
dict[2] = "three"
dict[4]='four'
print(dict[2])
print(dict.keys())
print(dict.values())


#********************************************************************
def count_letters(text):
    result={}
    for letter in text:
        if letter not in result:
            result[letter]=0
        result[letter]+=1
    return result
print(count_letters("sssss gg"))

#***********************************Dictionary are mutable **********************************

