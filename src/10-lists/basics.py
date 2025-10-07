def every_other(lst):
    return lst[::2] #print every 2
print(every_other([10, 20, 30, 40, 50, 60]))

def sum_positive(nums):
    total = 0 #sets total equal to 0
    for n in nums:
        if n > 0:
            total += n
    return total
print(sum_positive([-5, 3, 0, 8, -2]))

