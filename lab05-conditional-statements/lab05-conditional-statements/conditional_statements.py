#!/usr/bin/env python3
# Lab 5 – Conditional Statements

# Define two numbers
number1 = 10
number2 = 20

# Basic if/else
if number1 > number2:
    print("Number 1 is larger")
else:
    print("Number 2 is larger")

# Extend with elif
number1 = 10
number2 = 10

if number1 > number2:
    print("Number 1 is larger")
elif number1 < number2:
    print("Number 2 is larger")
else:
    print("Both numbers are equal")

# Test cases
number1 = 30
number2 = 20
# Output: Number 1 is larger

number1 = 15
number2 = 25
# Output: Number 2 is larger

number1 = 50
number2 = 50
# Output: Both numbers are equal
