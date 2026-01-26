# Day 5: Tuples Practice
# Topics:
# - creating tuples
# - indexing
# - unpacking
# - tuple methods

print("---- Basic Tuple ----")
t = (10, 20, 30, 40)

print("Tuple:", t)
print("Length:", len(t))
print("First element:", t[0])
print("Last element:", t[-1])

print("\n-----------------------------\n")

print("---- Loop through tuple ----")
for item in t:
    print(item)

print("\n-----------------------------\n")

print("---- Tuple unpacking ----")
a, b, c = (5, 10, 15)
print("a =", a)
print("b =", b)
print("c =", c)

print("\n-----------------------------\n")

print("---- Tuple count & index ----")
nums = (1, 2, 2, 3, 4, 2)

print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))

print("\n-----------------------------\n")

print("---- Tuple as return value ----")

def get_min_max(values):
    return (min(values), max(values))

result = get_min_max((5, 8, 1, 10))
print("Min and Max:", result)
