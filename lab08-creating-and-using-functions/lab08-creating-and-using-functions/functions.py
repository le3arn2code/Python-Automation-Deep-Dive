#!/usr/bin/env python3
# Lab 8 – Creating and Using Functions

# Task 1: Print greeting directly
def greet(name):
    print(f"Hello, {name}!")

def main():
    greet("Alice")
    greet("Bob")

main()

# Task 2: Return values
def greet(name):
    return f"Hello, {name}!"

def main():
    greeting1 = greet("Alice")
    greeting2 = greet("Bob")
    print(greeting1)
    print(greeting2)

main()
