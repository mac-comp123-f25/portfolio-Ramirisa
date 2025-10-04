def square_user_nums2():
  while True:
      user_inp = input("Enter the next number (negative to quit): ")
      user_num = int(user_inp)
      if user_num < 0:
        break
        print(user_num, "squared is", user_num ** 2)

square_user_nums2()
