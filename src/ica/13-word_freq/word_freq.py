import string


def compute_frequencies(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    cleaned_words = []
    for word in words:
        new_word = word.strip()
        if new_word:
            cleaned_words.append(new_word)
    freq = {}
    for word in cleaned_words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

if __name__ == "__main__":
    filename = "sample.txt"
    with open(filename, 'w') as f:
        f.write("Ray Rivers sat in the ray of the sun while Rivers Ray sat in the shade.")
    frequencies = compute_frequencies(filename)
    print(frequencies)
