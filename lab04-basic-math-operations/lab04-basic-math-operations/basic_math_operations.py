#!/usr/bin/env python3
# Lab 4 – Basic Math Operations

# Prompting the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Handle division by zero
if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Undefined (division by zero)"

# Display results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
