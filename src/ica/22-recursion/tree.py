import tkinter as tk
import turtle


def check_draw_tree(sz):
    """Tester function for the draw_tree"""

    # setup window
    win = tk.Toplevel()
    win.title(f"Tree Fractal {sz}")
    win_size = sz * 7
    cv = tk.Canvas(win, width=win_size, height=win_size)
    cv.pack()
    ts = turtle.TurtleScreen(cv)
    t = turtle.RawTurtle(ts)

    # set up turtle
    t.left(90)
    t.up()
    t.backward(sz * 3)
    t.down()
    t.speed(0)
    t.color("green")

    # draw the draw_tree
    draw_tree(sz, t)


def draw_tree(branch_len, turt):
    """The Interactive Textbook's draw_fractal_treedraw_fractal_tree drawing fractal function.
    Takes in the length of the main branch and a turtle, and it draws
    a symmetrical draw_fractal_treedraw_fractal_tree shape with branching to left and right. The fractal
    stops if the branch length gets to be less than or equal to 5"""
    if branch_len > 5:
        turt.forward(branch_len)
        turt.right(20)
        draw_tree(branch_len - 15, turt)
        turt.left(40)
        draw_tree(branch_len - 15, turt)
        turt.right(20)
        turt.backward(branch_len)


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    # write tests below
    check_draw_tree(30)
    check_draw_tree(75)
    check_draw_tree(125)

    root.mainloop()

