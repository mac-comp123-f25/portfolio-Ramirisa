from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def simple_blend(p1, p2):
    """
    Blend two same-sized pictures 50/50.
    """
    w = p1.getWidth()
    h = p1.getHeight()
    new_pic = Picture(w, h)

    for x in range(w):
        for y in range(h):
            (r1, g1, b1) = p1.getColor(x, y)
            (r2, g2, b2) = p2.getColor(x, y)

            r = (r1 + r2) // 2
            g = (g1 + g2) // 2
            b = (b1 + b2) // 2

            new_pic.setColor(x, y, (r, g, b))

    return new_pic


def blend2(p1, p2):
    """
    Blend two pictures, possibly of different sizes, over their overlapping region.
    """
    w = min(p1.getWidth(),  p2.getWidth())
    h = min(p1.getHeight(), p2.getHeight())

    new_pic = Picture(w, h)

    for x in range(w):
        for y in range(h):
            (r1, g1, b1) = p1.getColor(x, y)
            (r2, g2, b2) = p2.getColor(x, y)

            r = (r1 + r2) // 2
            g = (g1 + g2) // 2
            b = (b1 + b2) // 2

            new_pic.setColor(x, y, (r, g, b))

    return new_pic

def weighted_blend(p1, p2, wgt1):
    """
    Blend two pictures with weights:
    result = wgt1 * p1 + (1 - wgt1) * p2
    """
    w = min(p1.getWidth(),  p2.getWidth())
    h = min(p1.getHeight(), p2.getHeight())

    wgt2 = 1.0 - wgt1
    new_pic = Picture(w, h)

    for x in range(w):
        for y in range(h):
            (r1, g1, b1) = p1.getColor(x, y)
            (r2, g2, b2) = p2.getColor(x, y)

            r = wgt1 * r1 + wgt2 * r2
            g = wgt1 * g1 + wgt2 * g2
            b = wgt1 * b1 + wgt2 * b2

            new_pic.setColor(x, y, (r, g, b))

    return new_pic


def main():
    p1 = Picture("../SampleImages/daylilies.jpg")
    p2 = Picture("../SampleImages/wildColumbine.jpg")
    p3 = simple_blend(p1, p2)
    p3.show()
    keep_windows_open()

if __name__ == "__main__":
    main()

