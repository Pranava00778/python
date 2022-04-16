import random
import math   
prints a random value from the list
num=[]
sum=0
for i in range(20):
    n=random.randrange(100,250)
    num.append(n)
    sum=sum+n
print(num)
print(sum)
