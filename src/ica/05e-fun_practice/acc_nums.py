def sum_range(start_val, end_val):
    cnt=0   #initialize accumalator to default value 0
    for x in range(start_val, end_val+1):
        cnt=cnt+x   #update: add new x value to old value of cnt
    return cnt
print (sum_range(-20,-10,))