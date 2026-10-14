with open("text.txt", "r") as file:
    content = file.read()
    words = content.split()

    print(f"Total number of words: {len(words)}")
unique_words = set(words)
print("Unique words:", unique_words)