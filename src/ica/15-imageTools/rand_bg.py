import time
from src.ica.helpers.dummyWindow import *


def get_rand_bg():
    ...


def main():
    for i in range(10):
        pic = get_rand_bg()
        pic.show()
        time.sleep(1)

    keep_windows_open()


if __name__ == "__main__":
    main()
