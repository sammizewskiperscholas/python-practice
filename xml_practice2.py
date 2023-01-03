
import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()

# we got the tree and went in root
print(len(root))  # how many children element has
print(root.tag)  # name of the elemnt tag-collection
# giving us element attributes in a adictionary###blank dict means no attributes
print(root.attrib)

print([elem.tag for elem in root.iter()])

for movie in root.iter('movie'):  # iterate over movie tag starting from root
    print(movie.attrib)

for rating in root.iter('rating'):
    print(rating.text)
    # giving us all the text in rating but we cant manipulate the things
for rating in root.findall("./genre/decade/movie/[rating='PG']"):
    print(rating.attrib)
    # find the particular

# in movies there is one movie in uppercase - convert it into normal way

kkid = root.find("./genre/decade/movie[@title='THE KARATE KID']")

kkid.attrib['title'] = "The Karate Kid"
print(kkid.attrib)

# add a new genre tag


anime_genre = ET.SubElement(root, 'genre')

# we add attribute to new genre anime_genre now
anime_genre.attrib['catogory'] = 'Anime'
print(ET.tostring(root, encoding='utf8').decode('utf8'))
# to create a new decade with in this new genre and add a movie into it movie the batman return into this movie category here
