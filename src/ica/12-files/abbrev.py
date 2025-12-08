
def print_abbrev(filename):
    file_in = open(filename, 'r')

    for line in file_in:
        shortened = line[:20]
        print(shortened.strip())

    file_in.close()




