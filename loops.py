#for loop
"""items= ["shoes", "bag","cap"]

for item in items:
    print(item)
    if item== "bag":
        pass"""

"""for item in range(1,9):
    print(item)"""

"""inputs = int(input("pls enter a number "))
num = [1,2,3,4,5,6,7,8,9]

for number in num:
    mul= inputs*number
    print(f"{inputs} * {number} = {mul}")"""

#break, pass, continue, range

#nexted loop
"""items= ["shoes", "bag","cap"]
adj= ["red","blue", "green"]

for item in items:
    for add in adj:
        print(item, add)"""

#While loop
"""counter = 0

while True:
    counter += 1
    print(counter)
    if counter == 10:
        break"""

name = input("enter name ")
psd = input("enter password ")

password="12345"
while psd != password:
    psd = input("enter password ")
    if psd == password:
        print("welcome")
        break





