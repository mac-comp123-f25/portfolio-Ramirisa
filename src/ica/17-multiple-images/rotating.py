from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *



def rotate_left(oldPic):
    w = oldPic.getWidth()
    h = oldPic.getHeight()
    new_pic = Picture(h, w)
    for x in range(w):
        for y in range(h):
            old_color = oldPic.getColor(x, y)
            newX = y
            newY = w - x - 1
            new_pic.setColor(newX, newY, old_color)

    return new_pic
