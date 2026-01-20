# Day 1: Strings Practice
# Topics:
# - string input
# - len()
# - indexing and slicing
# - common string methods

print("---- Program 1: Basic String Input ----")
name = input("Enter your name: ")
print("Hello,", name)
print("Length of name:", len(name))

print("\n-----------------------------\n")

print("---- Program 2: Indexing and Slicing ----")
text = input("Enter a word: ")

if len(text) > 0:
    print("First character:", text[0])
    print("Last character:", text[-1])

print("First 3 letters:", text[:3])
print("Last 3 letters:", text[-3:])
print("Reversed:", text[::-1])

print("\n-----------------------------\n")

print("---- Program 3: Count vowels ----")
s = input("Enter a sentence: ").lower()

vowels = 0
for ch in s:
    if ch in "aeiou":
        vowels += 1

print("Total vowels:", vowels)

print("\n-----------------------------\n")

print("---- Program 4: Palindrome check ----")
word = input("Enter a word: ").lower()

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

print("\n-----------------------------\n")

print("---- Program 5: String methods ----")
message = input("Enter a sentence: ")

print("Upper:", message.upper())
print("Lower:", message.lower())
print("Title:", message.title())
print("Replace space with - :", message.replace(" ", "-"))
