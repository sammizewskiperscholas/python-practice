x = ['Now', 'We', 'are', 'cooking']
print(type(x))
print(x)
print(len(x))
print('are' in x)
print('am' in x)
print('Now' in x)
print(x[2],x[3])
print(x[1:3])
print(x[1:])
#****************************Using Split() and indexing ***************************************
def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

#********************************List's are Mutable & List Methods********************************************************

fruits = ['pineapple','banana','orange','apple','melon']
fruits.append("kiwi")
print(fruits)
fruits.insert(1,"mango")
print(fruits)
fruits.insert(25,"peach")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.remove(fruits[2])
print(fruits)
fruits.pop(0)
print(fruits)
fruits[2]='Strawbury'
print(fruits)

#*****************************Tuple is Immutable********************************

fullname = [('Samundeeswari',"Velusamy")]
print(fullname)

#*********************************************************

def convert_seconds(seconds):
    hours = seconds//3600
    minitues = (seconds - hours *3600)//60
    remaining_seconds = seconds-hours * 3600 -minitues*60
    return hours,minitues,remaining_seconds
result = convert_seconds(5000)
print(result)
print(type(result))


#********************************************************************

def file_size(file_info):
	name, type, size = file_info
	return("{:.2f}".format(size/ 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

#**************************************************************************

animals= ['lion','zebra','dolphin','monkey','tiger','cow']
chars = 0
for animal in animals:
    chars+=len(animal)
print("Total Characters: {}, Average Length: {}".format(chars,chars/len(animals)))

#********************************enumerate function**************************************************

winners = ['samundeeswari velusamy','deepesh maniyan','ritisha maniyan','maniyan mariappan']
for index,person in enumerate(winners):
    print("{}-{}".format(index+1,person))

#****************************************************************************
def full_emails(people):
    result = []
    for email,name in people:
        result.append("{}<{}>".format(name,email))
    return result
print(full_emails([("chamu.grm@gmail.com", "sam eshwari"),("shay@example.com","shay brandt")]))
    
#***************************************************************
def skip_elements(elements):
	# code goes here
	element = []
	for i,name in enumerate(elements):
		if i %2 ==0:
			element.append(name)
	return element

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

#*******************************List Comprehension********************************************************
multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

#*****************************Just one line using list comprehension ***************
multiples = [x*7 for x in range(1,11)]
print(multiples)
#************************************************
languages = ['python','java','c++','ruby']
lengths = [len(language) for language in languages]
print(lengths)
#**********************************************
def odd_numbers(n):
	return [x for x in range(0,n+1) if x %2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

#************************************************************
