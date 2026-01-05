# Day 2: Expressions and Calculations
# Topics:
# - Variables and data types
# - Arithmetic operations (+, -, *, /, //, %)
# - Type conversion using int() and float()
# - Taking numeric input from users
#
# Programs included:
# - Addition of two numbers
# - Celsius to Fahrenheit conversion
# - Simple Interest calculation
#
# Goal:
# Understand how Python evaluates expressions and performs calculations

# Program 1: Add two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

print("--------------")

# Program 2: Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)

print("--------------")

# Program 3: Simple Interest
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)