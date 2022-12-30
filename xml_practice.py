import xml.etree.ElementTree as ET

tree= ET.parse('movies.xml')
root= tree.getroot()

#print(tree)
#print(ET.tostring(root, encoding = 'utf8').decode('utf8'))
#print(root.tag) #giving us the name of the element tag
#print(root.attrib) #giving us the element attributes in a dictionary
################blank dicitonary means no attributes
#print(len(root)) ##how many children the element has
#print([elem.tag for elem in root.iter()]) #gives me a list of all the elements

for rating in root.iter('rating'):
   # print(rating.text)
   pass
   

for rating_pg in root.findall("./genre/decade/movie/[rating='PG']"):
    #print(rating_pg.attrib)
    pass

kkid= root.find("./genre/decade/movie[@title= 'THE KARATE KID']")
kkid.attrib['title']= "The Karate Kid"
#print(kkid.attrib)


# Creating a new genre <genre category = "Anime"> under the root <collections>
anime_genre = ET.SubElement(root, 'genre')
#print(ET.tostring(root, encoding = 'utf8').decode('utf8'))
anime_genre.attrib['category']= 'Anime'
#print(ET.tostring(anime_genre, encoding = 'utf8').decode('utf8'))


# Adding the decade <decade years = "2000"> under the genre <genre category = "Anime">
add_decade = root.find("./genre[@category= 'Anime']") # We are saving the location of Action 
                                                 # and passing it to the add variable
         
new_dec= ET.SubElement(add_decade, 'decade')
new_dec.attrib['years']= '2000s'



# Adding the movie <movie favorite= "True" title= "Gladiator"> under the decade <decade years = "2000">
add_movie = root.find("./genre[@category='Anime']/decade[@years = '2000s']")
new_movie = ET.SubElement(add_movie, 'movie')
new_movie.attrib['favorite'] = 'True'
new_movie.attrib['title'] = 'Gladiator'


# Adding the sub-tag format <format multiple="No">DVD</format> under the <movie favorite= "True" title= "Gladiator">
movie_path = root.find("./genre[@category='Anime']/decade[@years = '2000s']/movie[@title = 'Gladiator']")
new_format = ET.SubElement(movie_path, 'format')
new_format.attrib['multiple'] = 'No'
new_format.text = 'DVD'


# Adding the sub-tag year <year>2000s</year> under the movie <movie favorite= "True" title= "Gladiator">
new_year = ET.SubElement(movie_path, 'year')
new_year.text = '2000s'


# Adding the sub-tag rating <rating>R</rating> under the movie <movie favorite= "True" title= "Gladiator">
new_rating = ET.SubElement(movie_path, 'rating')
new_rating.text = 'R'


# Adding the sub-tag description <description> under the movie <movie favorite= "True" title= "Gladiator">
new_description = ET.SubElement(movie_path, 'description')
new_description.text = 'A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.'


# Writing the changes to the file
# A new genre category 'Anime', decade year '2000s', movie title 'Gladiator' and it's corresponding child would be updated to the file
tree.write('movies.xml')


# Appending the movie title 'Batman Returns' to the Genre category 'Anime'
batman = root.find("./genre/decade/movie[@title= 'Batman Returns']")
decade_path = root.find("./genre[@category='Anime']/decade[@years= '2000s']")
decade_path.append(batman)


# Deleting the movie title 'Batman Returns' from the genre category 'Action' with the year '1990s'
dec1990= root.find("./genre[@category='Action']/decade[@years= '1990s']")
dec1990.remove(batman)
action_path = root.find("./genre[@category= 'Action']") # We are saving the location of Action 
                                                # and passing it to the add variable


# Viewing the changes in the element tree from the root
print(ET.tostring(root, encoding='utf8').decode('utf8'))


# Writing the changes to the file 
# A new movie title 'Batman Returns' would be appended to the genre category 'Anime' and
# the movie title 'Batman Returns' would be deleted from the genre category 'Action' with the year '1990s'
tree.write('movies.xml')




