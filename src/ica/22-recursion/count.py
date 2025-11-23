def countdown(n):
    """Print numbers from n down to 1, then 'Blast Off!' using recursion."""
    if n <= 0:                 # base case
        print("Blast Off!")
    else:                      # recursive case
        print(n)
        countdown(n - 1)
