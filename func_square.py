import turtle
t = turtle.Pen()

def mySquare(size):
    for i in range(1,5):
        t.forward(size)
        t.left(90)

t.reset()

#mySquare(50)
# mySquare(100)
# mySquare(150)
# mySquare(200)
# mySquare(250)

for i in range(250,10,-10):
    mySquare(i)




