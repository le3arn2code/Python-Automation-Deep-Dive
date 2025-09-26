# Lab 6 – Looping with for

## Objectives
- Understand how to use the for loop in Python.
- Learn to iterate over numerical ranges and collections like lists.
- Gain experience in summarizing items processed through iteration.

## Lab Tasks

### Task 1: Print Numbers from 1 to 5
```python
for number in range(1, 6):
    print(number)
```

### Task 2: Loop Through a List
```python
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)
```

### Task 3: Summarize Processed Items
```python
item_count = 0
for fruit in fruits:
    item_count += 1
    print(fruit)

print(f"Total number of items processed: {item_count}")
```
