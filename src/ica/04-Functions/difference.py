def smallest_diff(x, y, z):
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    return min_diff

print(smallest_diff(3, 9, 5))
print(smallest_diff(32, 43, 90))


