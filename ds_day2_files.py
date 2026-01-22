# Day 2: File Handling Practice
# Topics:
# - writing to a file
# - reading from a file
# - counting lines
# - try/except for file errors

print("---- Program 1: Write to a file ----")

text = input("Enter a message to save in file: ")

with open("message.txt", "w") as f:
    f.write(text + "\n")

print("Saved to message.txt ✅")

print("\n-----------------------------\n")

print("---- Program 2: Read from file ----")

try:
    with open("message.txt", "r") as f:
        content = f.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("File not found ❌ (message.txt is missing)")

print("\n-----------------------------\n")

print("---- Program 3: Count lines in a file ----")

try:
    with open("message.txt", "r") as f:
        count = 0
        for line in f:
            count += 1

    print("Total lines in file:", count)
except FileNotFoundError:
    print("File not found ❌")
