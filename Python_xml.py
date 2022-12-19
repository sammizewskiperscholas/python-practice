
import xml.etree.ElementTree as ET
import re

tree = ET.parse('movies.xml')
root = tree.getroot()

print(tree)
print(root)
print(root.tag)
print(len(root))

#for child in root:
#    print(child)

print(len(root))

for child in root:
    print(child.tag, child.attrib)

print([i.tag for i in root.iter()])

print(ET.tostring(root, encoding = 'utf8').decode('utf8'))

for movie in root.iter('movie'):
    print(movie.attrib)

for description in root.iter('description'):
    print(description.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format/[@multiple = 'Yes']"):
    print(movie.attrib)

#back = root.find("./genre/decade/movie[@title = 'Back to the Future']")
#print(back)

#back.attrib['title'] = "Back 2 the Future"
#print(back.attrib)

tree.write('movies.xml')
tree = ET.parse('movies.xml')
root = tree.getroot()

for movie in root.iter('movie'):
    print(movie.attrib)

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)

for form in root.findall("./genre/decade/movie/format"):
    match = re.search(',', form.text)
    if match:
        form.set('multiple', 'Yes')
    else:
        form.set('multiple', 'No')

    print(form.attrib, form.text)

for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text, '\n')

for movie in root.findall("./genre/decade/movie/[year = '2000']"):
    print(movie.attrib)

add = root.find("./genre[@category = 'Action']")
new_dec = ET.SubElement(add, 'decade')
print(new_dec)

for genre in root.findall("./genre"):
    print(genre.attrib)

print(ET.tostring(root, encoding = 'utf8').decode('utf8'))
new_dec.attrib['years'] = '2000s'

#xmen = root.find("./genre/decade/movie/[@title = 'X-Men']")
#dec2000 = root.find("./genre[@category = 'Action']/decade[@years = '2000s']")
#dec2000.append(xmen)
#dec1990 = root.find("./genre/[@category = 'Action']/decade[@years = '1990s']")
#dec1990.remove(xmen)
#tree.write('movies.xml')
#print(ET.tostring(root, encoding = 'utf8').decode('utf8'))

new_anime1 = ET.SubElement(root, 'genre')
print(new_anime1)

new_anime1.attrib['category'] = 'Anime'
print(ET.tostring(root, encoding='utf8').decode('utf8'))

add1 = root.find("./genre[@category = 'Anime']")
new_dec2 = ET.SubElement(add1, 'decade')
print(new_dec2)

new_dec2.attrib['years'] = '2000s'
btman = root.find("./genre/decade/movie/[@title = 'Batman Returns']")
dec_2000 = root.find("./genre[@category = 'Anime']/decade[@years = '2000s']")
dec_2000.append(btman)
dec_1990 = root.find("./genre/[@category = 'Action']/decade[@years = '1990s']")
dec_1990.remove(btman)

