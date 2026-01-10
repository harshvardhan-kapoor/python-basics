# Day 5: Loops
# Topics:
# - for loop
# - while loop
# - repeating actions in Python

print("---- Program 1: Print numbers 1 to 10 (for loop) ----")
for i in range(1, 11):
    print(i)

print("\n-----------------------------\n")

print("---- Program 2: Sum of first n numbers (for loop) ----")
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)

print("\n-----------------------------\n")

print("---- Program 3: Countdown (while loop) ----")
x = int(input("Enter a number: "))

while x > 0:
    print(x)
    x = x - 1

print("Done")
