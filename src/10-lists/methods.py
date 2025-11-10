def end_points(nums):
    return (min(nums), max(nums))

points = end_points([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("points:", points)
print(points[0], points[1])

(min_val, max_val) = end_points([5, 10, 15, 20])
print(min_val, "and", max_val)
