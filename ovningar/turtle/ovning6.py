import turtle
george = turtle.Turtle()


# a)
george.pendown()
for i in range(3):
    george.forward(100)
    george.left(90)
    george.forward(50)
    george.right(90)

# b)
for i in range(10):
    george.forward(10)
    george.left(90)
    george.forward(5)
    george.right(90)