from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def main():
    # Load the original image from the SampleImages folder (relative path)
    orig = Picture("../SampleImages/mightyMidway.jpg")

    # 1) Print number of pixels
    w, h = orig.getWidth(), orig.getHeight()
    num_pixels = w * h
    print(f"Width: {w}, Height: {h}, Number of pixels: {num_pixels}")

    # 2) Make a copy and set each corner pixel to red
    red = (255, 0, 0)
    copy_img = orig.copy()
    # top-left
    copy_img.setColor(0, 0, red)
    # top-right
    copy_img.setColor(w - 1, 0, red)
    # bottom-left
    copy_img.setColor(0, h - 1, red)
    # bottom-right
    copy_img.setColor(w - 1, h - 1, red)

    # 3) Save the result
    out_path = "../SampleImages/mightyMidway-redCorners.jpg"
    copy_img.save(out_path)
    print(f"Saved: {out_path}")

    # 4) Explore the new picture (zoom to verify corners)
    copy_img.explore()

    # Keep the window(s) open so you can inspect
    keep_windows_open()

if __name__ == "__main__":
    main()

