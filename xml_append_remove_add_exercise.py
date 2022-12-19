import xml.etree.ElementTree as ET

#### EXERCISE ####
## ADD, APPEND, REMOVE ##
### WITH ELEMENT TREE XML API ###

def xml_check():
    print(f"\t\t\t {'#' * 10} XML PRINTOUT {'#' * 10}\n\n\n" )
    print(ET.tostring(collection, encoding='utf8').decode('utf8'))



# hw, create new decade within anime 
# add a movie 
# also move batman movie into anime
# delete other copy of batman

# Instructions: 
# 1. 
# Create an Anime Genre
# 2. 
# Add a movie into the Anime Genre
# 3.
# Append Batman into the Anime Genre
# 4. 
# Remove Batman from previous Genre

# Note 📝 I'm working with the original 
# 'Dirty' .XML file segment copied from the website


# SETTING UP THE OBJECTS #
#####
# First we have to import the module, 
# preferably import with an alias, which I did. 
#####

#####
# next we have to assign a variable to the xml file 
#####
movie_xml_file = ET.parse("xml/movies_dirty.xml")

# we can verify a file object was created by printing 
# print(movie_xml_file)

####
# Next we can assign a variable to the root of the file object
###

# Because I know the root of this xml is collection,
# I'm going to just call it collection. 
collection = movie_xml_file.getroot()

# Let's take a peek into the xml file with the 
# tostring() function

entire_movies_xml = ET.tostring(collection, encoding='utf8').decode('utf8')

print(entire_movies_xml)

# collection is root
    # decade is a tag
        # decade has the attribute 'years'

# movie is the next tag 
    # movie has several attributes: 'favorite', 'title'

#movie has sub-tags
# only the format tag has an attribute: 'multiple'
# every other subtag just has string info

## CREATING A GENRE 
# We have to add genre tags to the root

# sub element added to root, tag name genre, attribute 'category' is Anime
Anime = ET.SubElement(collection, 'genre')
Anime.attrib["category"] = 'Anime'

Anime_Decade = ET.SubElement(Anime, 'decade')
Anime_Decade.attrib["years"] = '2000s'

Anime_Movie = ET.SubElement(Anime_Decade, 'movie')
Anime_Movie.attrib["favorite"] = "False"
Anime_Movie.attrib["title"] = ""

Anime_Format = ET.SubElement(Anime_Movie, 'format')
Anime_Format.attrib["multiple"] = "Yes"
Anime_Format.text = "Blu_Ray, DVD, Online"
year_rating_description = {
        "year":"2001", 
        "rating":"R", 
        "description":"A space-faring bounty hunter group must stop a bio-terrorist."}
for item in year_rating_description:
    Sub = ET.SubElement(Anime_Movie, item)
    Sub.text = year_rating_description[item]




print("\t\t\t #### XML BEGIN ### ")
# print(entire_movies_xml)
print(ET.tostring(collection, encoding='utf8').decode('utf8')) # 🌟
# list, dict

# ⚠ I learned that you have to make these on-the-fly,
# they can't be stored and re run if you want to see
# the most updated info about your XML file.
# To prevent storage I've created a function vs assigning to a variable

# Let's move batman to the anime section. 
# because decade comes after genre we have to make
# the decade subtag in the anime seciton.


# I guess if you had a lot of tags you can 
# copy-paste a segment or write a function to
# auto-generate every time. I'm going to just write
# out the lines for now. 

#xml_check()

