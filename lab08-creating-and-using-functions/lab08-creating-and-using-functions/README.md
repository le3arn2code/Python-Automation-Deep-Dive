# Lab 8 – Creating and Using Functions

## Objectives
- Understand the concept of functions in programming.
- Learn how to define and call functions.
- Explore parameters and return values.
- Gain experience using functions to modularize code.

## Lab Tasks

### Task 1: Simple Function
```python
def greet(name):
    print(f"Hello, {name}!")

def main():
    greet("Alice")
    greet("Bob")

main()
```

### Task 2: Return Values
```python
def greet(name):
    return f"Hello, {name}!"

def main():
    greeting1 = greet("Alice")
    greeting2 = greet("Bob")
    print(greeting1)
    print(greeting2)

main()
```

### Task 3: Modularity
Functions allow for code reuse and better organization.  
Example: an e-commerce site can use the same `calculate_discount()` function in checkout, promotions, and cart modules to ensure consistent logic.
