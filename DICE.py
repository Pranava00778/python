import random
# import math   
# prints a random value from the list
# num=[]
# sum=0
# for i in range(20):
#     n=random.randrange(100,250)
#     num.append(n)
#     sum=sum+n
# print(num)
# print(sum)
list1 = [1, 2, 3, 4, 5, 6]
playNext = "y"
while playNext=="y":
    firstDice = random.choice(list1)
    secondDice= random.choice(list1)
    print("")
    print("%s + %s = %s" % (firstDice,secondDice, firstDice + secondDice))
    print("")
    playNext=input("Next: ")