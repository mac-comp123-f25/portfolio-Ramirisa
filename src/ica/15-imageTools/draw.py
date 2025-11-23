from src.ica.helpers.imageTools import *   # <-- make sure this is here
from src.ica.helpers.dummyWindow import *
import random

def draw_something():
    # 1) make a canvas
    w, h = 300, 300
    pic = Picture(w, h)

    # 2) fill a solid background (so we know something drew)
    bg = (200, 220, 255)
    for x in range(w):
        for y in range(h):
            pic.setColor(x, y, bg)

    # 3) draw a visible red border
    red = (255, 0, 0)
    for x in range(w):
        pic.setColor(x, 0, red)
        pic.setColor(x, h - 1, red)
    for y in range(h):
        pic.setColor(0, y, red)
        pic.setColor(w - 1, y, red)

    # 4) draw a diagonal so it’s unmistakable
    for i in range(min(w, h)):
        pic.setColor(i, i, (0, 0, 0))

    return pic  # <-- must return the Picture

def main():
    drawing = draw_something()
    drawing.show()
    keep_windows_open()

if __name__ == "__main__":
    main()


