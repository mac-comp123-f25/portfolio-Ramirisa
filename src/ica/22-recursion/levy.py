import math
import tkinter as tk
import turtle


def calc_next_size(curr_size: float) -> float:
    """Takes in the current straight-line length, and computes
    and returns the length of the isosceles triangle's side. """
    h_dist = (curr_size / 2)
    v_dist = h_dist * math.tan(math.radians(45))
    hypot = math.sqrt(v_dist ** 2 + h_dist ** 2)
    return hypot


def check_draw_levy(size: float, reps: int) -> None:
    """Tester function for the draw_levy"""

    # setup window
    win = tk.Toplevel()
    win.title(f"Levy C Fractal {reps}")
    win_size = size * 7
    cv = tk.Canvas(win, width=win_size, height=win_size)
    cv.pack()
    ts = turtle.TurtleScreen(cv)
    t = turtle.RawTurtle(ts)

    # set up turtle
    t.left(90)
    t.up()
    # t.backward(size * 3)
    t.down()
    t.speed(0)
    t.color("green")

    # draw the draw_tree
    draw_levy(t, size, reps)


# TODO: Complete the function
def draw_levy(turt, size, reps):
    ...


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    # write tests below
    check_draw_levy(100, 1)
    check_draw_levy(100, 2)
    check_draw_levy(100, 3)
    check_draw_levy(100, 4)
    check_draw_levy(100, 5)
    check_draw_levy(100, 10)

    root.mainloop()
