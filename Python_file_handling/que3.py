s = input("Enter a sentence: ")
with open("data.txt", "w") as file:
    file.write(s)
with open("data.txt", "r") as file:
    words = file.read().split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word:", longest_word)