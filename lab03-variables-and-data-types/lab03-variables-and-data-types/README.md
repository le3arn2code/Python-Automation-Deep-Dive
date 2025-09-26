# Lab 3 – Working with Variables and Data Types

## Objectives
- Understand how to create and manipulate variables in Python.
- Explore different data types such as integers, floats, strings, and booleans.
- Learn to check the data type of a variable using Python functions.
- Experiment with type casting between different data types.

## Prerequisites
- Basic understanding of Python syntax.
- Python environment set up on your system.

## Lab Tasks

### Task 1: Creating Variables
```python
my_integer = 10
my_float = 20.5
my_string = "Hello, World!"
my_boolean = True

print(my_integer)
print(my_float)
print(my_string)
print(my_boolean)
```

### Task 2: Checking Types
```python
print(type(my_integer))   # <class 'int'>
print(type(my_float))     # <class 'float'>
print(type(my_string))    # <class 'str'>
print(type(my_boolean))   # <class 'bool'>
```

### Task 3: Type Casting
```python
# Integer to Float
new_float = float(my_integer)
print(new_float)
print(type(new_float))

# Float to String
new_string = str(my_float)
print(new_string)
print(type(new_string))

# String to Integer
another_string = "15"
new_integer = int(another_string)
print(new_integer)
print(type(new_integer))

# Boolean to Integer
new_integer_from_boolean = int(my_boolean)
print(new_integer_from_boolean)
```
