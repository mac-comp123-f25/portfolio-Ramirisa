def end_points(lst):
    return (min(lst), max(lst))

result = end_points([5, 2, 9, 1, 7])
print(result)

low, high = end_points([5, 2, 9, 1, 7])
print(low, high)
