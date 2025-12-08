

def select_words(s, fn):
    file_in = open(fn, 'r')

    result = []
    for line in file_in:
        word = line.strip()
        if s in word:
            result.append(word)

    file_in.close()
    return result


# Example tests:
# print(select_words("ii", "./TextFiles/shortcross.txt"))   # should return 2 words
# print(select_words("quo", "./TextFiles/shortcross.txt"))  # should return 0
# print(len(select_words("ii", "./TextFiles/crosswords.txt")))   # expected: 38
# print(len(select_words("quo", "./TextFiles/crosswords.txt")))  # expected: 65
