def copy_str(string,num_times):
    ans_str = ""  # initialize accumulator to empty string
    for x in range(num_times):
        ans_str = ans_str + string    # update ans_str
    return ans_str

print(copy_str(3,5))