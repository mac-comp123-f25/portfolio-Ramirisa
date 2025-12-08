def middle_value(a, b, c):

    if (a <= b and a >= c) or (a >= b and a <= c):
        return a

    elif (b <= a and b >= c) or (b >= a and b <= c):
        return b

    else:
        return c

if __name__ == "__main__":
    assert middle_value(5, 2, 77) == 5
    assert middle_value(-10, 50, 57) == 50
    assert middle_value(-1, -6, -3) == -3
    print("All tests passed!")
