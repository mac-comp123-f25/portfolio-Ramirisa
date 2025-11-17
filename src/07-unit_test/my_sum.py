def sum3(lst):
    assert type(lst) in [list, tuple], "Input must be a list or tuple"
    assert len(lst) >= 3,  "List must have at least 3 elements"
    assert all(type(lst[i]) in [int, float] for i in range(3)), "First 3 elements must be numbers"

    return lst[0] + lst[1] + lst[2]

print(sum3([2, 2, 2]))
print(sum3([2, 4, 6, 8]))
print(sum3((2, 2.2, 2.22)))

if __name__ == "__main__":
  print( sum3([5, 2, 8, -2, 6, 15]) )  #good
  print( sum3([5, 2]) ) #This one for lack of 1 more number
  print( sum3(5) ) #Lack of list or tuple
  print( sum3(["h", "i", 1, 2, 3]) ) #Numbers aren't first
  print( sum3([1, 2, 3, "h", "i"]) )  #good

