# Day 3: Lists Practice
# Topics:
# - list creation and append()
# - sum, max, min, average
# - sorting
# - searching

print("---- Program 1: Create a list ----")
nums = []
n = int(input("How many numbers you want to enter? "))

for i in range(n):
    value = int(input("Enter number: "))
    nums.append(value)

print("Your list:", nums)

print("\n-----------------------------\n")

print("---- Program 2: List calculations ----")
print("Length:", len(nums))
print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Average:", sum(nums) / len(nums))

print("\n-----------------------------\n")

print("---- Program 3: Sorting ----")
sorted_nums = nums.copy()
sorted_nums.sort()
print("Sorted list:", sorted_nums)

print("\n-----------------------------\n")

print("---- Program 4: Search in list ----")
target = int(input("Enter a number to search: "))

if target in nums:
    print(target, "found ✅")
else:
    print(target, "not found ❌")

print("\n-----------------------------\n")

print("---- Program 5: Remove last element ----")
if len(nums) > 0:
    removed = nums.pop()
    print("Removed:", removed)
    print("List now:", nums)
else:
    print("List is empty, nothing to remove")
