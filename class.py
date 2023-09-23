"""
python class
python is an object oriented programming language and
almost everything in python is object with properties and 
methods. class is the foundation on which we build this objects.
"""
"""class person:
    name= "emmanuel"
    age= 30

first_person= person()
print(first_person.age)"""

#the __init__() function is used to assign value to object properties
"""class person:
    def __init__(self,age,name):
        self.name= name
        self.age= age

first_person= person(50,"emmanuel")
print(first_person.name)"""

#the __str__() function controls what should be return when objects are represented as string
"""class person:
    def __init__(self,age,name):
        self.name= name
        self.age= age

    def __str__(self):
        return f"{first_person.name} is older than {secon_person.name}"
        

first_person= person(50,"emmanuel")
secon_person= person(30,"joy")
print(first_person)"""


#object methods are function that belongs to object
class person:
    def __init__(self,age,name):
        self.name= name
        self.age= age

    def __str__(self):
        return f"{first_person.name} is older than {secon_person.name}"
    
    def dance(self):
        print(first_person.name, "is dancing")

first_person= person(50,"emmanuel")
secon_person= person(30,"joy")
first_person.name = "john"

del first_person.name
print(first_person.name)
#object property(modify,deleted)