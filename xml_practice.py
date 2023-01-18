import xml.etree.ElementTree as ET

tree = ET.parse("movies.xml")
root = tree.getroot()

print(tree)
print(root)

print(root.tag)
print(root.attrib)

#for child in root:
#     print(child.tag,child.attrib)
#print([elem.tag for elem in root.iter()])
#print(ET.tostring(root,encoding='utf8').decode('utf8'))

#for movie in root.iter("movie"):
#    print(movie.attrib)

#for description in root.iter("description"):
#    print(description.text)
#     pass

#for movies in root.findall("./genre/decade/movie/[year='1992']"):
#    print(movies.attrib)
#     pass

#for movies in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
#    print(movies.attrib)

#for movies in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
#    print(movies.attrib)

back = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(back)
back.attrib = 'Back to the Future'
print(back.attrib)

tree.write("movies.xml")
# tree = ET.parse("movies.xml")
# root = tree.getroot()

# for movie in root.iter("movie"):
#     print(movie.attrib)