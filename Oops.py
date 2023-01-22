#****************************Classes and Objects(Practice Program)*****************************************
class Employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya'
#*************************************************************************

print(help(int))

#*************************************************************************
class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "Red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = "sugar is sweet and so you are"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 
#**********************************************************************

a,b,c=1,2,3
print(a)
print(b)
print(c)
a = "hello"
b="hai"
x=a
a=b
b=x

print(a)
print(b)

#********************************************************************************
class Dog:
  years = 0
  def dog_years(breed):
    return breed.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())

#***************************************************************************************
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(some_person.name)

# Create a new instance with a name of your choice
some_person = Person("sam")
# Call the greeting method
print(some_person.greeting())
#**********************************************************************************************

class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)

#********************************************************************************************
class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

#***********************************************************************************************

class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)

#***************************************************************************************
import datetime, random
now = datetime.datetime.now()
print(now)
print(random.randint(1,20))
#**************************************************************

class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Hello",name)
    def get_name(self):
        print(self.name)
        return self.name
    def get_age(self):
        print(self.age)
    def bark(self):
        print("bark")
d=Dog("Tim",25)
d1=Dog("Bill",36)
d.get_name()
d.get_age()
d1.get_age()
d1.get_name()
d.bark()
d.bark()
print(type(d))

