def remove_all(value, lst):
    while lst.count(value) > 0:
        lst.remove(value)
nums = [1, 2, 3, 2, 4, 2, 5]
remove_all(2, nums)
print(nums)
