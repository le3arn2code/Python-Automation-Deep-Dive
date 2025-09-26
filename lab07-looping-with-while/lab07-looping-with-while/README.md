# Lab 7 – Looping with while

## Objectives
- Understand the basic concept of a while loop.
- Learn to use while loops to execute code repeatedly based on a condition.
- Interactively prompt users for input using a loop.
- Gracefully terminate loops based on specific user input.

## Lab Tasks

### Task 1: Print Numbers 1 to 5
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### Task 2: Interactive Loop
```python
user_input = ''
while True:
    user_input = input("Enter a string (type 'exit' to quit): ")
    if user_input == "exit":
        break
    print("You entered:", user_input)
```

### Task 3: Graceful Exit
```python
user_input = ''
try:
    while True:
        user_input = input("Enter a string (type 'exit' to quit): ")
        if user_input == "exit":
            print("Exiting the loop. Goodbye!")
            break
        print("You entered:", user_input)
finally:
    print("Program terminated successfully.")
```
