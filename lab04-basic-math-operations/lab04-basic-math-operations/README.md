# Lab 4 – Basic Math Operations

## Objectives
- Understand and perform basic mathematical operations in a programming environment.
- Learn to prompt user input and display output.
- Develop coding skills to handle arithmetic operations.

## Prerequisites
- Basic understanding of programming concepts (variables, data types, input/output).
- Familiarity with Python programming language.

## Lab Tasks

### Task 1: Setup
```bash
python --version
```

### Task 2: Prompt User for Input
```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
```

### Task 3: Perform Operations
```python
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Undefined (division by zero)"
```

### Task 4: Display Results
```python
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
```

## Conclusion
✅ Performed basic math operations in Python  
✅ Handled user input and type conversion  
✅ Managed division by zero gracefully
