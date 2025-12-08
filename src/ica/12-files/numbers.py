
def write_to_n(n, filename):
    file_out = open(filename, 'w')

    for k in range(1, n + 1):
        file_out.write(str(k) + "\n")

    file_out.close()



