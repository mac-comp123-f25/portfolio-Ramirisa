# word_freq.py

def compute_frequencies(filename):
    """Reads the contents of a file and prints them (Step 1)."""
    try:
        with open(filename, "r") as f:
            text = f.read()
        print(text)   # Temporary: just confirm we can read the file
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


# --- testing area ---
if __name__ == "__main__":
    # Replace 'alice.txt' with the file you want to test
    compute_frequencies("alice.txt")

# word_freq.py
import string

def compute_frequencies(filename):
    """Reads file, splits text into cleaned words, and prints them (Step 2)."""
    try:
        with open(filename, "r") as f:
            text = f.read()

        # Split text into words
        words = text.split()

        # Create a new list for cleaned-up words
        cleaned_words = []
        for word in words:
            # Remove punctuation from beginning and end of each word
            new_word = word.strip(string.punctuation)
            cleaned_words.append(new_word)

        # Print the cleaned list to verify
        print(cleaned_words)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


# --- testing area ---
if __name__ == "__main__":
    compute_frequencies("alice.txt")  # or your test file

    # word_freq.py
    import string


    def compute_frequencies(filename):
        """Reads file, cleans words, and loops through them (Step 3)."""
        try:
            with open(filename, "r") as f:
                text = f.read()

            # Step 2: split and clean
            words = text.split()
            cleaned_words = []

            for word in words:
                new_word = word.strip(string.punctuation)
                cleaned_words.append(new_word)

            # Step 3: independent loop to print each cleaned word
            for w in cleaned_words:
                print(w)

        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")


    # --- testing area ---
    if __name__ == "__main__":
        compute_frequencies("alice.txt")  # or your test file

    # word_freq.py
    import string


    def compute_frequencies(filename):
        """Reads file, cleans words, and returns a frequency dictionary."""
        try:
            with open(filename, "r") as f:
                text = f.read()

            # Step 2: split and clean
            words = text.split()
            cleaned_words = []
            for word in words:
                new_word = word.strip(string.punctuation)
                cleaned_words.append(new_word)

            # Step 3+4: create dictionary accumulator
            freq = {}

            # Loop over cleaned words to count occurrences
            for w in cleaned_words:
                if w in freq:
                    freq[w] += 1
                else:
                    freq[w] = 1

            # Return the frequency dictionary
            return freq

        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return {}  # Return empty dict if file not found


    # --- testing area ---
    if __name__ == "__main__":
        result = compute_frequencies("alice.txt")  # or your own file
        print(result)

