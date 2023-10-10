import turtle

def rita_kvadrat(sida):
    myTurtle = turtle.Turtle()
    myTurtle.pendown()

    for i in range(4):
        myTurtle.forward(sida)
        myTurtle.left(90)

rita_kvadrat(300)