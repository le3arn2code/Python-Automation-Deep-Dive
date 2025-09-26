# Lab 9 – Working with Lists and Tuples

# Task 1: Creating and Printing a List
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("The list of fruits is:", fruits)

# Task 2: Modifying the List
fruits.append("fig")
print("After adding 'fig':", fruits)

fruits.remove("date")
print("After removing 'date':", fruits)

fruits.sort()
print("The sorted list of fruits is:", fruits)

# Task 3: Demonstrating Lists vs Tuples
fruit_tuple = ("apple", "banana", "cherry", "elderberry", "fig")
try:
    fruit_tuple[0] = "avocado"
except TypeError as e:
    print("Error:", e)
