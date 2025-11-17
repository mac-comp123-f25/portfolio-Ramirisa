

import imagetools

from src.ica.helpers.dummyWindow import *   # keeps image windows open


# ---------------------------------------------------------
# Basic grayscale conversion (equal weights)
# ---------------------------------------------------------
def grayscale(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (r + g + b) / 3
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic




# ---------------------------------------------------------
# Weighted grayscale conversion
# ---------------------------------------------------------
def weighted_scale(pic, w1, w2, w3):
    """
    Returns a weighted grayscale version of the picture.
    w1, w2, w3 are weights for the red, green, and blue channels.
    (They should each be between 0.0 and 1.0 and sum to 1.0)
    """
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = w1 * r + w2 * g + w3 * b
        new_pic.setColor(x, y, (lumin, lumin, lumin))
    return new_pic


# ---------------------------------------------------------
# Script section: test functions
# ---------------------------------------------------------
if __name__ == "__main__":
    # Load test images from your SampleImages folder
    pic1 = Picture("../SampleImages/antiqueTractors.jpg")

    # Regular grayscale
    gray = grayscale(pic1)
    gray.show()

    # Weighted grayscale: emphasize red
    weighted_red = weighted_scale(pic1, 0.8, 0.1, 0.1)
    weighted_red.show()

    # Weighted grayscale: emphasize green
    weighted_green = weighted_scale(pic1, 0.1, 0.8, 0.1)
    weighted_green.show()

    # Weighted grayscale: emphasize blue
    weighted_blue = weighted_scale(pic1, 0.1, 0.1, 0.8)
    weighted_blue.show()

    keep_windows_open()
