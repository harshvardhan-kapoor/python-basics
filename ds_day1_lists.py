# Day 1: Python Data Structures - Lists
# Topics: list basics, loops, sum, max, min

numbers = []

n = int(input("How many numbers you want to enter? "))

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

print("\nYour list:", numbers)
print("Total numbers:", len(numbers))
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Average:", sum(numbers) / len(numbers))
