
income = {}

years = {
    "Alice": 1999,
    "Bob": 2002,
    "Susan": 1968
}

years2 = years.copy()

print("Susan's birth year:", years["Susan"])

years["Henry"] = 2004

del years2["Susan"]

print("years:", years)
print("years2:", years2)
