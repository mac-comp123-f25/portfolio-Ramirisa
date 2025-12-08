
income = {}

years = {
    "Susan": 1968,
    "Mark": 1999,
    "Tori": 2001
}

years2 = years.copy()

print("Susan's birth year:", years["Susan"])

years["Henry"] = 2004

del years2["Susan"]

print("years:", years)
print("years2:", years2)
