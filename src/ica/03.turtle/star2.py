import turtle
wind = turtle.Screen()
turt = turtle.Turtle()

for back_color in ['pink', 'lightgreen', 'yellow', 'blue']:
    wind.bgcolor(back_color)
    turt.forward(200)
    turt.right(180)
    wind.exitonclick()
