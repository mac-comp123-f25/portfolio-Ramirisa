def add_user_nums():
    sum_of_nums = 0
    user_num = int(input("Enter a number (0 to quit): "))
    while user_num != 0:
        sum_of_nums += user_num
        user_num = int(input("Enter a number (0 to quit): "))

    return sum_of_nums

add_user_nums()