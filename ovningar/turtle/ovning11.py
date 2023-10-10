import turtle

myTurtle = turtle.Turtle()
myTurtle.pendown()
myTurtle.speed(0)

def ny_sida():
    for i in range(100000000):
        myTurtle.forward(100)
        myTurtle.right(100)
        myTurtle.forward(40)
        myTurtle.right(80)
        myTurtle.forward(80)
        myTurtle.left(0.01)

ny_sida()