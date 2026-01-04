def add_numbers(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add_numbers(x, y)
print("Sum:", result)

print("\n-----------------------------\n")

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print("Number is:", check_even_odd(num))

print("\n-----------------------------\n")

def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest:", simple_interest(p, r, t))
