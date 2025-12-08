def range_limit(num):
    if num < 1:
        return 1
    elif num > 10:
        return 10
    else:
        return num

if __name__ == "__main__":
    assert range_limit(8) == 8
    assert range_limit(-1) == 1
    assert range_limit(50) == 10
    print("All tests passed!")
