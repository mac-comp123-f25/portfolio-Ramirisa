def square_user_nums():
  # Initialize loop variable
  user_inp = input("Enter the next number (negative to quit): ") #if we were to rid of these first 2, usernum technically would not exist for the while loop to run
  user_num = int(user_inp)
  while user_num >= 0:
    print(user_num, "squared is", user_num ** 2)
    user_inp = input("Enter the next number (negative to quit): ")
    user_num = int(user_inp) #If we removed from within the loop, the loop would never change, it would just be the same 

#First two lines are repeated because, the first set forms original value while the 2nd set allows for the value to update as the loop goes on.
