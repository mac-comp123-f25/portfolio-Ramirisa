def has_QOCD(s):
    return ('Q' in s) or ('O' in s) or ('C' in s) or ('D' in s)

if __name__ == "__main__":
    assert has_QOCD("Quick") == True
    assert has_QOCD("Odd") == True
    assert has_QOCD("MAC") == True
    assert has_QOCD("WiLD") == True
    assert has_QOCD("MATH") == False
    assert has_QOCD("comp123") == False
    print("All tests passed!")
