# Lab 12 – Error Handling with try-except

try:
    number = int(input("Enter a number to divide 100: "))
    result = 100 / number
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
