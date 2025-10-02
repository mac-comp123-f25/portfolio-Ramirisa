def between(value, lo, hi):
    """Takes in three numbers: a value, a low number, and a high number
    and it returns True if value is between lo and hi, inclusively."""
    assert type(value) in [int, float]
    assert type(lo) in [int, float]
    assert type(hi) in [int, float]
    if (lo <= value) and (value <= hi):
        return True
    else:
        return False



if __name__ == "__main__":
  print( between(10, 0, 20) )
  print( between(25, 10, 20) )
  print( between(5.3, 6.7, 3.1) )
  print( between(5.3, 3.1, 6.7) )
  print(between("kookaburra", "aardvark", "tapir")) # cause error
