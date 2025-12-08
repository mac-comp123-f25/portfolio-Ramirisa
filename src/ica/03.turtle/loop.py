import turtle
wind = turtle.Screen()
turt = turtle.Turtle()
wind.bgcolor("pink")
turt.forward(200)
turt.right(180)

wind.bgcolor("lightgreen")
turt.forward(200)
turt.right(180)

wind.bgcolor("yellow")
turt.forward(200)
turt.right(180)

wind.bgcolor("blue")
wind.exitonclick()

wind = turtle.Screen()
turt = turtle.Turtle()

for back_color in ['pink', 'lightgreen', 'yellow', 'blue']:
    wind.bgcolor(back_color)
    turt.forward(200)
    turt.right(180)
    wind.exitonclick()

    wind = turtle.Screen()
    turt=turtle.Turtle()
    wind.bgcolor("lightgreen")
    turt.forward(200)
    turt.right(180)
    wind.exitonclick()