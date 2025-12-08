import turtle
n = 360/3

wind = turtle.Screen()
turt = turtle.Turtle()


for back_color in ['pink', 'lightgreen', 'yellow', 'blue']:
    turt.begin_fill()
    wind.bgcolor(back_color)
    turt.forward(100)
    turt.left(n)
    turt.forward(100)
    turt.left(n)
    turt.forward(100)
    turt.left(n)
    turt.end_fill()
    turt.begin_fill()
    turt.penup()
    turt.goto(0, 50)
    turt.pendown()
    turt.forward(100)
    turt.right(n)
    turt.forward(100)
    turt.right(n)
    turt.forward(100)
    turt.right(n)
    turt.end_fill()
    wind.exitonclick()