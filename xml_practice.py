import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
print(tree)
#print(root)

#print(root.tag)
#print(root.attrib)

#for child in root:
    #print(child.tag,child.attrib)
#print([elem.tag for elem in root.iter()])
