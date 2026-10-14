with open("text.txt",'r') as f:
    content = f.read()
    print(content)
vowels = "aeiouAEIOU"
vowels_count = 0
for ch in content:
    if ch in vowels:
        vowels_count += 1
print(f"Total vowels {vowels_count}")