import turtle

def draw_square_print(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)
    print(t.position())  # just prints text like "(80.00,0.00)"
    # returns None implicitly!

scr = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

end_pos = draw_square_print(t, 80)  # end_pos is None
t.penup()
# This line fails or behaves wrong because end_pos is None:
# t.goto(end_pos[0] + 40, end_pos[1])  # TypeError
scr.exitonclick()
