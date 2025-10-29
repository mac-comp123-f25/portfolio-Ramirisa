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

