import turtle


def spiral_in(spiro_turt, side_len):
    pass


def check_spiral_in(size: int) -> None:
    """A faster way to test spiral_in function"""
    scr = turtle.Screen()
    turt = turtle.Turtle()
    spiral_in(turt, size)
    scr.exitonclick()


if __name__ == '__main__':
    check_spiral_in(20)
