from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

from src.ica.imageTools import *
from src.ica.helpers.dummyWindow import *
import random

def copy_pic_into_random(small_pic, big_pic):
    small_w = small_pic.getWidth()
    small_h = small_pic.getHeight()
    big_w = big_pic.getWidth()
    big_h = big_pic.getHeight()

    # choose a spot where the whole small image will fit
    start_x = random.randrange(0, big_w - small_w + 1)
    start_y = random.randrange(0, big_h - small_h + 1)

    for (x, y) in small_pic:
        color = small_pic.getColor(x, y)
        target_x = start_x + x
        target_y = start_y + y
        big_pic.setColor(target_x, target_y, color)

    return big_pic


def main():
    turtle = Picture("../SampleImages/greenTurtle.jpg")
    scene = Picture("../SampleImages/bearLake.jpg")

    for _ in range(5):
        copy_pic_into_random(turtle, scene)

    scene.show()
    keep_windows_open()

if __name__ == "__main__":
    main()
