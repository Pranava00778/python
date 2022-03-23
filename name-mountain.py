name = input("Enter your full name: ")
# print(name[1:2]) # Slicing
#print(name[3:8])
#manoj
#for i in range(1,len(name)+1):
#    print(name[0:i])
#for j in range(len(name)+1,1):
#    print(name[0:j])

#for i in range(0,10):
#    print("-"*(11-i), name * (2*i+1))

for i in range(0,len(name)+1):
    print(name[i:i+1])