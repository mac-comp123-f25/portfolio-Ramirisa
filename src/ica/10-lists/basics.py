def every_other(lst):
    return lst[::2]

def sum_positive(lst):
    total = 0
    for x in lst:
        if x > 0:
            total += x
    return total
