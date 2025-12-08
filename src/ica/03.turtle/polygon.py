import turtle
n = 360/6

wind = turtle.Screen()
turt = turtle.Turtle()


for back_color in ['pink', 'lightgreen', 'yellow', 'blue']:
    turt.begin_fill()
    wind.bgcolor(back_color)
    turt.forward(200)
    turt.left(n)
    turt.forward(200)
    turt.left(n)
    turt.forward(200)
    turt.left(n)
    turt.forward(200)
    turt.left(n)
    turt.forward(200)
    turt.left(n)
    turt.forward(200)
    turt.left(n)
    turt.end_fill()
    wind.exitonclick()

