

def i_words(filename):
    file_in = open(filename, 'r')
    all_text = file_in.read()
    file_in.close()

    words = all_text.split()
    result = [w for w in words if 'i' in w]

    return result

