# Lab 5 – Conditional Statements (if, elif, else)

## Objectives
- Understand the concept of conditional statements in Python.
- Learn how to use if, elif, and else to control program flow.
- Write scripts to compare values and handle different conditions.

## Prerequisites
- Basic understanding of Python syntax.
- Familiarity with variables and data types.

## Lab Tasks

### Task 1: Compare Two Numbers
```python
number1 = 10
number2 = 20

if number1 > number2:
    print("Number 1 is larger")
else:
    print("Number 2 is larger")
```

### Task 2: Add `elif` for Equality
```python
number1 = 10
number2 = 10

if number1 > number2:
    print("Number 1 is larger")
elif number1 < number2:
    print("Number 2 is larger")
else:
    print("Both numbers are equal")
```

### Task 3: Test Cases
```python
# Case 1: number1 > number2
number1 = 30
number2 = 20

# Case 2: number1 < number2
number1 = 15
number2 = 25

# Case 3: number1 == number2
number1 = 50
number2 = 50
```
