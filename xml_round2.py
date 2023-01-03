import xml.etree.ElementTree as ET

tree= ET.parse(r'C:\Users\Learner_XZHCG223\Documents\movies.xml')
root= tree.getroot()

#print(tree)
#print(ET.tostring(root, encoding = 'utf8').decode('utf8'))
#print(root.tag) #giving us the name of the element tag
#print(root.attrib) #giving us the element attributes in a dictionary
################blank dicitonary means no attributes
#print(len(root)) ##how many children the element has
#print([elem.tag for elem in root.iter()]) #gives me a list of all the elements

for rating in root.iter('rating'):
#    print(rating.text)
   pass
   

for rating_pg in root.findall("./genre/decade/movie/[rating='PG']"):
    #print(rating_pg.attrib)
    pass

# kkid= root.find("./genre/decade/movie[@title= 'THE KARATE KID']")
# kkid.attrib['title']= "The Karate Kid"
# print(kkid.attrib)

anime_genre = ET.SubElement(root, 'genre')
# print(ET.tostring(root, encoding = 'utf8').decode('utf8'))
anime_genre.attrib['category']='Anime'

# print(ET.tostring(anime_genre, encoding='utf8').decode('utf8'))

adding_decade = root.find("./genre[@category= 'Anime']")

new_decade= ET.SubElement(adding_decade, 'decade')
new_decade.attrib['years']= '2000s'

add_movie = root.find("./genre[@category='Anime']/decade[@years = '2000s']")
new_movie = ET.SubElement(add_movie, 'movie')
new_movie.attrib['favorite'] = 'True'
new_movie.attrib['title'] = 'Gladiator'

movie_path = root.find("./genre[@category='Anime']/decade[@years = '2000s']/movie[@title = 'Gladiator']")
new_format = ET.SubElement(movie_path, 'format')
new_format.attrib['multiple'] = 'No'
new_format.text = 'DVD'

new_year = ET.SubElement(movie_path, 'year')
new_year.text = '2000s'

new_rating = ET.SubElement(movie_path, 'rating')
new_rating.text = 'R'

new_description = ET.SubElement(movie_path, 'description')
new_description.text = 'A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.'

tree.write(r"C:\Users\Learner_XZHCG223\Documents\movies.xml")

tree = ET.parse(r"C:\Users\Learner_XZHCG223\Documents\movies.xml")
root = tree.getroot()

batman = root.find("./genre/decade/movie[@title= 'Batman Returns']")
decade_path = root.find("./genre[@category='Anime']/decade[@years= '2000s']")
decade_path.append(batman)

# dec1990= root.find("./genre[@category='Action']/decade[@years= '1990s']")
# dec1990.remove(batman)
# action_path = root.find("./genre[@category= 'Action']") 

# print(ET.tostring(root, encoding='utf8').decode('utf8'))

tree.write(r"C:\Users\Learner_XZHCG223\Documents\movies.xml")

