import xml.etree.ElementTree as ET

tree = ET.parse("movies1.xml")
root = tree.getroot()

# print(tree)
# print(root)

# print(root.tag)
# print(root.attrib)

#anime = root.find("./genre[@category='Anime']")
anime = ET.SubElement(root,'genre')
print("Added new Genre")

anime.attrib["category"] = 'Anime'
print("added new genre attribute category=Anime")

new_dec = ET.SubElement(anime, 'decade')
print("added new decade")

new_dec.attrib["years"] = '1990s'
print("added decade attribute year = 1990s")

batman = root.find("./genre/decade/movie[@title='Batman Returns']")
dec1990s = root.find("./genre[@category='Anime']/decade[@years='1990s']")

dec1990s.append(batman)
print("copy movie element Batman from Action genre to Anime genre ")

dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(batman)
print("remove Batman movie element from Action genre ")


tree.write("movies1.xml")
