import xml.etree.ElementTree as ET

tree= ET.parse('movies1.xml')
root= tree.getroot()

# print(tree)
# print(ET.tostring(root, encoding = 'utf8').decode('utf8'))
# print(root.tag) #giving us the name of the element tag
# print(root.attrib) #giving us the element attributes in a dictionary
# ###############blank dicitonary means no attributes
# print(len(root)) ##how many children the element has
# print([elem.tag for elem in root.iter()]) #gives me a list of all the elements

for rating in root.iter('rating'):
   # print(rating.text)
   pass
   

for rating_pg in root.findall("./genre/decade/movie/[rating='PG']"):
    #print(rating_pg.attrib)
    pass

kkid= root.find("./genre/decade/movie[@title= 'THE KARATE KID']")
kkid.attrib['title']= "The Karate Kid"
#print(kkid.attrib)

#Creating "Anime" category under <collection>
anime_genre = ET.SubElement(root, 'genre')
print(ET.tostring(root, encoding = 'utf8').decode('utf8'))
anime_genre.attrib['category']='Anime'

#Creating "decade" under <genre category='Anime'>
new_decade = root.find("./genre[@category='Anime']")
print(new_decade)
print()
new_decade_add = ET.SubElement(new_decade,'decade')
print(new_decade_add)
print()
new_decade_add.attrib['years']='2017'#Adding the attribute value '2017'
print(ET.tostring(new_decade_add, encoding='utf8').decode('utf8'))


#Creating "movie" under<decade years=2017>
new_movie= root.find("./genre[@category='Anime']/decade/[@years='2017']")

new_movie_add = ET.SubElement(new_movie,'movie')
new_movie_add.attrib['favorite']='True'
new_movie_add.attrib['title']='Gifted'


#Creating sub-tags <format>,<year>,<rating>and<description> under "movie" tag
Movie_path = root.find("./genre[@category='Anime']/decade[@years='2017']/movie[@title='Gifted']")

new_format = ET.SubElement(Movie_path,'format')
new_year=ET.SubElement(Movie_path,'year')
new_rating=ET.SubElement(Movie_path,'rating')
new_description = ET.SubElement(Movie_path,'description')

# Giving the value of attributes 
new_format.attrib['multiple']='yes'
new_format.text ='DVD'
new_year.text='2017'
new_rating.text='R'
new_description.text='an intellectually gifted seven-year-old who becomes the subject of a custody battle between her maternal uncle and maternal grandmother.'

#Writing the changes into the file
tree.write('movies1.xml')

#Changing the movie "Batman Returns" from Action categroy to Anime category
batman=root.find("./genre/decade/movie[@title='Batman Returns']")
decade_2017= root.find("./genre[@category='Anime']/decade[@years='2017']")
decade_2017.append(batman)

#Remove the movie "Batman Returns" from Action category
decade_1990= root.find("./genre[@category='Action']/decade[@years='1990s']")
decade_1990.remove(batman)

#Again writing the changes to the file
tree.write('movies1.xml')

#View the changes
print(ET.tostring(root, encoding = 'utf8').decode('utf8'))



