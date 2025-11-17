from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def crop_picture(pic, start_x, start_y, width, height):
    """
    Return a new picture that is a crop from pic, starting at (start_x, start_y)
    with the given width and height.
    """
    new_pic = Picture(width, height)

    for x in range(width):
        for y in range(height):
            src_x = start_x + x
            src_y = start_y + y
            color = pic.getColor(src_x, src_y)
            new_pic.setColor(x, y, color)

    return new_pic


def main():
    dam = Picture("../SampleImages/hooverDam.jpg")

    dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
    dam_crop2 = crop_picture(dam, 100, 150, 100, 150)

    dam_crop1.show()
    dam_crop2.show()
    keep_windows_open()

if __name__ == "__main__":
    main()
