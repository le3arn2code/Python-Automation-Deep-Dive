# Lab 15 – Functions in Python

# Task 1: Define and Call a Function
def greet():
    print("Hello, World from a function!")

# Task 2: Function with Parameters
def greet_user(name):
    print(f"Hello, {name}!")

# Task 3: Function with Return Value
def add_numbers(a, b):
    return a + b

# Task 4: Function with Default Parameters
def greet_city(name, city="New York"):
    print(f"Hello {name}, welcome to {city}!")

# ---- Execution Section ----
if __name__ == "__main__":
    greet()                          # Task 1
    greet_user("Alice")              # Task 2
    print("Sum:", add_numbers(5, 7)) # Task 3
    greet_city("Alice")              # Task 4
    greet_city("Bob", "London")      # Task 4
