a = 1
y = 1
t = 0
while t < 1000 :
    t = t + a * (a + 1) + y + (y + 1)
    a = a + 1
    y = y + 1
    print(t)
