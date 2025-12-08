def percent_to_letter(pct):
    if pct >= 90:
        return "A"
    elif pct >= 80:
        return "B"
    elif pct >= 70:
        return "C"
    elif pct >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    assert percent_to_letter(95) == "A"
    assert percent_to_letter(82) == "B"
    assert percent_to_letter(71) == "C"
    assert percent_to_letter(67) == "D"
    assert percent_to_letter(12) == "F"
    print("All tests passed!")
