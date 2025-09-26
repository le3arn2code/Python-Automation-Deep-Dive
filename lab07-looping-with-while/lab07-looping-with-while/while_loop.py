#!/usr/bin/env python3
# Lab 7 – Looping with while

# Task 1: Print numbers 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1

# Task 2: Interactive Loop
user_input = ''
while True:
    user_input = input("Enter a string (type 'exit' to quit): ")
    if user_input == "exit":
        break
    print("You entered:", user_input)

# Task 3: Graceful Exit
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
