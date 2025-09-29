
def double_return(x):
    return x * 2          # produces a value

def double_print(x):
    print(x * 2)          # just displays text

a = double_return(10)
b = double_print(10)      # prints "20", but b == None

print (a)
print(b)

"""Code using return"""

def load_numbers():
    return [3, 10, 5, 7, 10, 3]

def dedupe(xs):             #gets rid of duplicates in out list but keeps order of #'s
    return list(dict.fromkeys(xs))

def square(xs):
    return [x * x for x in xs]

def avg(xs):
    return sum(xs) / len(xs)

result = avg(square(dedupe(load_numbers())))
print("pipeline result:", result)

"""Code using print"""

def load_numbers():
    print(3, 10, 5, 7, 10, 3)

def dedupe(xs):
    print (list(dict.fromkeys(xs))) # preserves order

def square(xs):
    print (x * x for x in xs)

def avg(xs):
    print (sum(xs) / len(xs))

result = avg(square(dedupe(load_numbers())))
print("pipeline result:", result)

