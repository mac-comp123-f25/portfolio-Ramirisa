import time
import random
from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def get_rand_bg():
    """Return a Picture with a random solid background color."""
    width, height = 200, 200   # you can adjust the size if you want
    pic = Picture(width, height)

    # Pick random RGB values (0–255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    # Fill the whole picture
    for x in range(width):
        for y in range(height):
            pic.setColor(x, y, color)

    return pic


def main():
    for i in range(10):
        pic = get_rand_bg()
        pic.show()
        time.sleep(1)

    keep_windows_open()


if __name__ == "__main__":
    main()

