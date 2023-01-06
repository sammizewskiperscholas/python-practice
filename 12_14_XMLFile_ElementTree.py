import xml.etree.ElementTree as ET      #import ElementTree library which has functions to read and manupulate XML files
import re

tree = ET.parse("movies1.xml")
root = tree.getroot()

#create new genre  'Anime' to the root
aneme_genre = ET.SubElement(root,'genre')
aneme_genre.attrib['category']="Anime"
print(ET.tostring(root,encoding='utf8').decode('utf8'))


#create new decade 2000s under <genre category "Anime">
aneme_decade = ET.SubElement(aneme_genre,'decade')  
aneme_decade.attrib['years'] = "2000s"                     #adding new dacade 2000s under 'Aneme' genre

#add new movie under decade 2000s
aneme_new_movie = ET.SubElement(aneme_decade,'movie')     # adding new movie tag under decade - 2000s             
aneme_new_movie.attrib['favorite'] = "True"                #  setting the movie attributes         
aneme_new_movie.attrib['title'] = "Shrek"
new_movie_format = ET.SubElement(aneme_new_movie,'format')  #adding sub-tag format under movie 
new_movie_format.attrib['multiple']="True"                  #setting format attribute
new_movie_format.text = "DVD,online"                        #aading format text
new_movie_year = ET.SubElement(aneme_new_movie,'year')      #adding sub-tag year under movie
new_movie_year.text = "2001"                                #stting year text
new_movie_rating = ET.SubElement(aneme_new_movie,'rating')  #adding sub-tag rating under movie
new_movie_rating.text = "PG"
new_movie_decription = ET.SubElement(aneme_new_movie,'description') #adding sub-tag description under movie
new_movie_decription.text = "A mean lord exiles fairytale creatures to the swamp of a grumpy ogre,\n who must go on a quest and resucue a princess for lord \n in order to get his land back"

tree.write('movies1.xml')                                #writing to changes to file



tree = ET.parse("movies1.xml")                            #parsing tree again after changes
root = tree.getroot()

aneme_genre=root.find("./genre[@category='Anime']")      #find the 'Aneme' genre in the tree

#add new Decade to 'Anime' genre
aneme_genre_new_dacade=ET.SubElement(aneme_genre,'decade')
aneme_genre_new_dacade.attrib['years']="1990s"

#move batman movie from 'Action' genre to 'Aneme' genre
batman = root.find("./genre/decade/movie[@title='Batman Returns']")                #find batman movie 
anme_dec1990s = root.find("./genre[@category='Anime']/decade[@years='1990s']")
anme_dec1990s.append(batman)                                                       #append batman movie to 'Anme' genre decade 1990s

action_dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
action_dec1990s.remove(batman)                                                     #remove movie from 'Action' genre

action = root.find("./genre[@category='Action']")
print(ET.tostring(action, encoding='utf8').decode('utf8'))
print(ET.tostring(aneme_genre,encoding='utf8').decode('utf8'))

tree.write('movies1.xml')
tree=ET.parse('movies1.xml')
root = tree.getroot
print(ET.tostring(root,encoding='utf8').decode('utf8'))




# ==================================================Class Practice=============================================
# tree = ET.parse('movies1.xml')           #Parse the xml File
# root = tree.getroot()

# print(tree)
# print(root)

#print root Tag (which collection in Movies file)
# print(root.tag)

#printed root attributes (which is empty {}- means no attribute on root tag in movies.xml )
# print(root.attrib)

#itrate over subelements of tree
# for child in root:
    # print(child.tag, child.attrib)

#to get all the elements of the entire Tree
# print([elem.tag for elem in root.iter()])

#tostring method of Element tree to display document from root 
# print(ET.tostring(root,encoding='utf8').decode('utf8'))


#use  root.iter() function to list all subelements under the root that match the element specified

# for movies in root.iter('movie'):
    # print(movies.attrib)

#print text content (Print out all the descriptions of the movies )
# for description in root.iter('description'):
    # print(description.text)

# for movie in root.findall("./genre/decade/movie/[year='1992']"):
    # print(movie.attrib)

#use @ when search using attribute. Now, print out only the movies that are available in multiple formats (an attribute).
# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    # print(movie.attrib)

#Tip: use '...' inside of XPath to return the parent element of the current element.
# for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
    # print(movie.attrib)

# =====================================  Modifying XML =============================================================

# Accesing attribute of the element
# backtof=root.find("./genre/decade/movie[@title='Back 2 the Future']")
# print(backtof)

#assigning value to the attribute
# backtof.attrib['title']='Back To The Future'
# print(backtof.attrib)

#Write change back to movies1.xml file.
# tree.write("movies1.xml")

# tree = ET.parse("movies1.xml")                   #parse the tree again to see saved changes
# root = tree.getroot()

# for movie in root.iter('movie'):                 #diplay movies
    # print(movie.attrib)

# =======================================================Fixing Attributes==========================================

# The multiple attribute is incorrect in some places. Use ElementTree to fix the designator based on how many
#  formats the movie comes in. First, print the format attribute and text to see which parts need to be fixed.

# for form in root.findall("./genre/decade/movie/format"):
    # print(form.attrib, form.text)

# # import re use regex to find pattern
# for form in root.findall("./genre/decade/movie/format"):
# # search for comma seperated text
#     match = re.search(',',form.text)
#     if match:
#         form.set('multiple','Yes')
#     else:
#         form.set('multiple','No')


# # for form in root.findall("./genre/decade/movie/format"):
#     # print(form.attrib, form.text)

# tree.write("movies1.xml")

# tree = ET.parse('movies1.xml')
# root = tree.getroot()

# for form in root.findall("./genre/decade/movie/format"):
    # print(form.attrib,form.text)


# =================================================Moving Element===================================
# for decade in root.findall("./genre/decade"):
#     print(decade.attrib)
#     for year in decade.findall("./movie/year"):
#         print(year.text,'\n')

# #create new decade in action category
# action = root.find("./genre[@category='Action']")
# new_dec = ET.SubElement(action, 'decade')
# new_dec.attrib["years"] = '2000s'

# # print(ET.tostring(action, encoding='utf8').decode('utf8'))

# # Append the X-Men movie to the 2000s and remove it from the 1990s, using .append() 
# # and .remove(), respectively.

# xmen = root.find("./genre/decade/movie[@title='X-Men']")
# dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
# dec2000s.append(xmen)
# dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
# dec1990s.remove(xmen)
# print(ET.tostring(action, encoding='utf8').decode('utf8'))

# tree.write("movies1.xml")

# tree = ET.parse('movies1.xml')
# root = tree.getroot()

# print(ET.tostring(root, encoding='utf8').decode('utf8'))