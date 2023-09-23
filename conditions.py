#if
gender = "male"
age = int(input("enter your age pls? "))
if age >= 18:
    pass
  
#elif
elif age >= 10 and age <= 18:
    print("you are a teeneger")
elif age != 0 and age <= 10:
    print("you are a child")
#else
else:
    print("you are not human")
#nexted if and pass

if age >= 18:
    if gender == "male":
        print("you are a man")


