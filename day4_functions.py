# Day 4: Functions
# Topics:
# - Defining functions
# - Passing parameters
# - Returning values
# - Reusing logic

def add_numbers(first_number, second_number):
    """Returns the sum of two numbers"""
    return first_number + second_number


def check_even_odd(number):
    """Returns whether a number is Even or Odd"""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def calculate_simple_interest(principal, rate, time):
    """Returns simple interest value"""
    return (principal * rate * time) / 100


# ---- Using the functions ----

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum:", add_numbers(x, y))

print("\n-----------------------------\n")

num = int(input("Enter a number: "))
print("Number is:", check_even_odd(num))

print("\n-----------------------------\n")

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest:", calculate_simple_interest(p, r, t))
