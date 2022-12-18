import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

 
#Creating anime genre
 anime_genre = ET.SubElement(root, 'genre')
 anime_genre.attrib['category'] = 'Anime'
 anime = root.find("./genre[@category='Anime']")
 new_dec = ET.SubElement(anime, 'decade')
 new_dec.attrib["years"] = '2000s'
 print(ET.tostring(anime_genre, encoding='utf8').decode('utf8'))

 tree.write("movies.xml")

 tree = ET.parse('movies.xml')
 root = tree.getroot()

 print(ET.tostring(root, encoding='utf8').decode('utf8'))
#Moving batman to anime genre and removing from original
batman = root.find("./genre/decade/movie[@title='Batman: The Movie']")
animedec2000s = root.find("./genre[@category='Anime']/decade[@years='2000s']")
animedec2000s.append(batman)
dec1960s = root.find("./genre[@category='Comedy']/decade[@years='1960s']")
dec1960s.remove(batman)
print(ET.tostring(root, encoding='utf8').decode('utf8'))

