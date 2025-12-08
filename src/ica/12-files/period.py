
def up_to_period(filename):
    file_in = open(filename, 'r')
    text = file_in.read()
    file_in.close()

    result = ""
    for ch in text:
        result += ch
        if ch == '.':
            break

    return result



