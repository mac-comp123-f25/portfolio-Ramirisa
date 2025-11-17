from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

from src.ica.helpers.dummyWindow import *
import math

def scale_down(pic):
    """
    Return a new picture that is half the width and half the height of pic.
    """
    old_w = pic.getWidth()
    old_h = pic.getHeight()

    new_w = math.ceil(old_w / 2)
    new_h = math.ceil(old_h / 2)

    new_pic = Picture(new_w, new_h)

    for x in range(new_w):
        for y in range(new_h):
            src_x = 2 * x
            src_y = 2 * y

            if src_x < old_w and src_y < old_h:
                color = pic.getColor(src_x, src_y)
                new_pic.setColor(x, y, color)

    return new_pic

def scale_up(pic):
    """
    Return a new picture that is twice the width and twice the height of pic.
    """
    old_w = pic.getWidth()
    old_h = pic.getHeight()

    new_w = old_w * 2
    new_h = old_h * 2

    new_pic = Picture(new_w, new_h)

    for (x, y) in pic:
        color = pic.getColor(x, y)

        target_x = 2 * x
        target_y = 2 * y

        # fill the 2x2 block
        new_pic.setColor(target_x,     target_y,     color)
        new_pic.setColor(target_x + 1, target_y,     color)
        new_pic.setColor(target_x,     target_y + 1, color)
        new_pic.setColor(target_x + 1, target_y + 1, color)

    return new_pic

def main():
    pic = Picture("../SampleImages/daylilies.jpg")
    small = scale_down(pic)
    big = scale_up(pic)

    pic.show()
    small.show()
    big.show()
    keep_windows_open()

if __name__ == "__main__":
    main()

