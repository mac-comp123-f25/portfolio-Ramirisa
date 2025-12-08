

file_in = open("./TextFiles/alice.txt", 'r')

count = 0
for text_line in file_in:
    text_line = text_line.strip()
    print("Line", count, ":", text_line)
    count += 1

file_in.close()
