# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:24:04 2022

@author: SAE
"""

import xml.etree.ElementTree as ET
import re

# import xml
tree = ET.parse('movies.xml')
root = tree.getroot()

# -Add a new genre called Anime to the root
new_genre = ET.SubElement(root, 'genre')
new_genre.attrib["category"] = 'Anime'
print(ET.tostring(new_genre))

# -Add a new decade to the new anime genre. First check the decade for the Batman movies: 

for title in root.findall("./genre/decade/movie/[@title]"):
  match = re.match('Batman', title.attrib['title'])
  if match: 
    print(title.attrib['title'])  

# returns two movies:
#  Batman Returns
#  Batman: The Movie

# Find which year these movies belong to:

for movie in root.iter('movie'):
  for y in movie.iter('year'):
    match = re.match('Batman', movie.attrib['title'])
    if match: 
      print(movie.attrib['title'], y.text)

# returns two movies with dates:
#  Batman Returns 1992
#  Batman: The Movie 1966

# Create anime decade 1990s 
anime = root.find("./genre[@category='Anime']")
new_decade = ET.SubElement(anime, 'decade')
new_decade.attrib["years"] = '1990s'
print(new_decade.attrib)

# Add Batman returns
batman = root.find("./genre/decade/movie[@title='Batman Returns']")
decade1990s = root.find("./genre[@category='Anime']/decade[@years='1990s']")
decade1990s.append(batman)
print(ET.tostring(root, encoding='utf8').decode('utf8'))


# Delete Batman from the old genre:
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(batman)  
print(ET.tostring(root, encoding='utf8').decode('utf8'))
  
# Write updated tree to xml file
tree.write("movies.xml")