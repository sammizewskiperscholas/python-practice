import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
print('Starting...')
print(f'root.tag {root.tag}')
print(root.attrib)
for child in root:
    print(child.tag, child.attrib)


print([elem.tag for elem in root.iter()])
print(ET.tostring(root, encoding = 'utf8').decode('utf8'))
for movie in root.iter('movie'):
   print(movie.attrib)
for description in root.iter('description'):
        print(description.text)
for movie in root.findall("./genre/decade/movie/[year='1992']"):
     print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
     print(movie.attrib)

for movie in root.iter('movie'):
     print(movie.attrib)
#bt2f = root.find("./genre/decade/movie[@title = 'Back 2 the Future']")
#bt2f.attrib['title'] = 'Back to the Future'
#tree.write('movies.xml')
#tree = ET.parse('movies.xml')
root = tree.getroot()
for movie in root.iter('movie'):
     print(movie.attrib)
for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)

for decade in root.findall("./genre/decade"):
     print(decade.attrib)
for year in decade.findall("./movie/year"):
        print(year.text, '\n')

action = root.find("./genre[@category='Action']")
new_dec = ET.SubElement(action, 'decade')
new_dec.attrib["years"] = '2000s'
print(ET.tostring(action, encoding='utf8').decode('utf8'))
xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)
print(ET.tostring(action, encoding='utf8').decode('utf8'))

animation = root.find("./genre")
anime_genre = ET.SubElement(root, 'genre')
anime_genre.attrib['category'] = 'Animation'
animation1 = root.find("./genre[@category='Animation']")
new_anime = ET.SubElement(animation1, 'decade')
new_anime.attrib["years"] = '1990s'
print(ET.tostring(anime_genre, encoding='utf8').decode('utf8'))
bat_man = root.find("./genre/decade/movie[@title = 'Batman Returns']")
new_genre = root.find("./genre[@category='Animation']/decade[@years='1990s']")
new_genre.append(bat_man)
old_genre = root.find("./genre[@category='Action']/decade[@years='1990s']")
old_genre.remove(bat_man)
print(ET.tostring(root, encoding='utf8').decode('utf8'))
