def count_words(word, text):
    words = text.split()
    return words.count(word)
print(count_words("Zay", "Zay Zay what's up dude?"))