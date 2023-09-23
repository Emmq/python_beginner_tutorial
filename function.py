#Python function
"""def greet(name,age):
    print("hello ",name," you are ",age," years old")

greet("emmanuel",40)"""
#arbitrary arguments(*rgs)
"""def fam(*family):
    head = "the head of the family is the "+family[1]
    print(head)
fam("father","mother","sister","brother")"""


#keyword arguments(kwarg)
"""def earth(first_man, first_woman):
    print(f"the first man on earth is {first_man}")

earth(first_man="Adam",first_woman="Eve")
"""
#passing list into a function

"""def item(items):
    for item in items:
        print(item)

school_item= ["shoes","bag","note","pen"]
item(school_item)
"""
#return value

def greet(anything):
    print("good day "+anything)
    return

age= 35
message= greet("emmanuel")
print(f"{message} you are {age} year old")