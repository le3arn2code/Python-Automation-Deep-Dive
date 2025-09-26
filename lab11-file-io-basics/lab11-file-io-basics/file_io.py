# Lab 11 – File I/O Basics

# Task 1: Create and Write to a File
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a test of file I/O.\n')

# Task 2: Append Text to the File
with open('output.txt', 'a') as file:
    file.write('Appending new text.\n')

# Task 3: Read From the File and Print the Contents
with open('output.txt', 'r') as file:
    content = file.read()
    print("File Content:\n", content)

print("Text appended to file and file content displayed.")
