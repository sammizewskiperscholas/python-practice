import xml.etree.ElementTree as ET #alias
import re #regex

#fix data within movies.xml file

tree = ET.parse('movies.xml') #assign to variable (set to )
root = tree.getroot() #get root of tree (set root variable to move along tree)

print(tree)
print(root)

print(root.tag) #tag - gets values inside element
print(root.attrib) #attrib - see if tag has any attributes

for child in root:    #create for loop to iterate over each child in root (childern in root collection are all genre)
    print(child.tag,child.attrib) #gets value inside element : see if tage has any attributes (returns as dictionary)

#print([elem.tag for elem in root.iter()]) # example of list comperhension
#print(ET.tostring(root, encoding='utf8').decode('utf8'))
#use iter () to iterate

for movie in root.iter('movie'): #getting attributes for all movie tags that are passed
    #print(movie.attrib)
    pass
#access text
for description in root.iter('description'):
    #print(description.text) #use text becuase it does not have attributes
    pass
#movie is parent of description

#for movie in root.findall("./genre/decade/movie/[year='1992']"): #pass in path of what we are trying to find
    #print(movie.attrib) #print movies only in 1992

#for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']"): #multiple an attribute of format (only returns dictionary with multiple as key and yes as value)
    #print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."): #@ when using attrubutes
    #print(movie.attrib)
    pass
#(...) use to return parent element of current element, gives more useable information

#fix back 2 the future to back to the future

#back= root.find("./genre/decade/movie[@title= 'Back to the Future']") #use find to find a specific 
#print(back)
#back.attrib["title"] = "Back To the Future" #access attribute title and set it to correct spelling
#print(back.attrib) 

#file is not changed^

#tree.write('movies.xml') #send back to movies.xml file so the changes can be seen there
#tree= ET.parse('movies.xml')
#root=tree.getroot()
#for movie in root.iter('movie'):
    #print(movie.attrib)

for form in root.findall("./genre/decade/movie/format"): #larger check of what we have in format
    #print(form.attrib, form.text)
    #search for the commas in the format text
    match= re.search(',', form.text) #regex in python
    if match:
        form.set('multiple', 'Yes') #set()- set elements attribute
    else:
        form.set('multiple', "No")
    print(form.attrib, form.text)

#check to see if decades match up with years text
for decade in root.findall("./genre/decade"): #getting decade (.) starts at root
    print(decade.attrib) #getting decase attribute
    for year in decade.findall("./movie/year"): # (.) at decade
        print(year.text, '\n') #print text inside year (/n - creates new line)

#fix decade beace year should be correct
#create decade
#need to know what the movie is

for movie in root.findall("./genre/decade/movie[year='2000']"): #shows what movies where release in 2000s
    print(movie.attrib)

#add decade to action genre because X-Men in action genre
add= root.find("./genre[@category='Action']") #go into action genre
#print(add)
new_decade= ET.SubElement(add, 'decade') #add to action tag and create new decade
#print(new_decade)
new_decade.attrib['years']='2000s' #add 2000s to the decade we just created

for genre in root.findall("./genre"): #getting decade (.) starts at root
    #print(genre.attrib) #getting decase attribute
    pass

#+print(ET.tostring(add, encoding='utf8').decode('utf8')) #see if decade was added

#movie X-men from 1990s to 2000s in action genre
#first make a copy and add xmen to 2000s
xmen= root.find("./genre/decade/movie[@title='X-men']")
decade2000= root.find("./genre[@category='Action']/decade[@years='2000s']")
decade2000.append(xmen)
print(ET.tostring(add, encoding='utf8').decode('utf8'))

#delete x-men from old category
#decade1990=root.find("./genre[@category='Action']/decade[@years='1990s']")
#decade1990.remove(xmen)
#print(ET.tostring(add, encoding='utf8').decode('utf8'))

#tree.write('movies.xml')
