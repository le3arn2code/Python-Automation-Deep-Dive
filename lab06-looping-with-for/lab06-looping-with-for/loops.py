#!/usr/bin/env python3
# Lab 6 – Looping with for

# Task 1: Print numbers from 1 to 5
for number in range(1, 6):
    print(number)

# Task 2: Loop through a list
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# Task 3: Summarize processed items
item_count = 0
for fruit in fruits:
    item_count += 1
    print(fruit)

print(f"Total number of items processed: {item_count}")
