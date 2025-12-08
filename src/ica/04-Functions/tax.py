def add_tax(price, tax_rate):
    tax_amt = price * tax_rate
    return price + tax_amt

print(add_tax(25.99, 0.0725))

def smallest_diff(x, y, z):
    print('smallest_diff inputs:', x, y, z)
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    print(diff1, diff2, diff3, 'return value:', min_diff)
    return min_diff

smallest_diff(3, 9, 5)

