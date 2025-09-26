#!/usr/bin/env python3
# Lab 3 – Working with Variables and Data Types

# Creating variables
my_integer = 10
my_float = 20.5
my_string = "Hello, World!"
my_boolean = True

# Print variables
print(my_integer)
print(my_float)
print(my_string)
print(my_boolean)

# Checking types
print(type(my_integer))   # <class 'int'>
print(type(my_float))     # <class 'float'>
print(type(my_string))    # <class 'str'>
print(type(my_boolean))   # <class 'bool'>

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
