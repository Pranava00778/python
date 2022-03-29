age = int(input("Enter your age: "))

if age < 5 :
    print("you are a kid")
elif age >= 5 and age < 13:
    print("you are a boy")
elif age >=13 and age <=19 :
    print("YOu are a teenager")
elif age > 19 and age < 40 :
    print("you are an adult")
elif age > 40 and age < 60 :
    print("You are an old man")
else :
    print("You are a senior citizon")