with open("text.txt", "r") as file:
    lines = file.readlines()
    print(lines)
print("Number of lines:", len(lines))
print(f"2nd line: {lines[1]}")
print(f"3rd line: {lines[2]}")

