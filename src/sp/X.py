import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)
    return t.position()

# setup
scr = turtle.Screen()
t = turtle.Turtle()
t.speed(0)


end_pos = draw_square(t, 80)

t.penup()
t.goto(end_pos[0] + 40, end_pos[1])  # 40 px gap to the right
t.pendown()
draw_square(t, 80)

scr.exitonclick()
