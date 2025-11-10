from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def clamp8(v):
    v = int(v)
    return 0 if v < 0 else 255 if v > 255 else v

def change_red(picture, factor):
    for (x, y) in picture:
        r, g, b = picture.getColor(x, y)
        picture.setColor(x, y, (clamp8(r * factor), g, b))

def change_blue(picture, factor):
    for (x, y) in picture:
        r, g, b = picture.getColor(x, y)
        picture.setColor(x, y, (r, g, clamp8(b * factor)))

def remove_blue(picture):
    for (x, y) in picture:
        r, g, b = picture.getColor(x, y)
        picture.setColor(x, y, (r, g, 0))

def fix_green(picture, number):
    number = clamp8(number)
    for (x, y) in picture:
        r, g, b = picture.getColor(x, y)
        picture.setColor(x, y, (r, number, b))

def main():
    pic = Picture("../SampleImages/stateFairCorn.jpg")
    pic.show()                 # initial view

    # ---- try one at a time ----
    # change_red(pic, 1.5)      # more red
    # change_blue(pic, 0.5)     # less blue
    # remove_blue(pic)          # no blue
    # fix_green(pic, 40)        # set all green to 40

    pic.show()                  # update the window after changes
    keep_windows_open()

if __name__ == "__main__":
    main()
