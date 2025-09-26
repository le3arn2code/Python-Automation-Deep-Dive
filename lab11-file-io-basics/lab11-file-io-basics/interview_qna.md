# Interview Q&A – Lab 11 File I/O Basics

**Q1: What are the main file modes in Python?**  
A: 'r' = read, 'w' = write, 'a' = append, 'x' = exclusive creation.

**Q2: What happens when you open a file in write mode?**  
A: It creates the file if it does not exist, otherwise overwrites it.

**Q3: How do you ensure a file is closed after operations?**  
A: Use the `with open(...) as f:` context manager.

**Q4: What is the difference between read() and readline()?**  
A: `read()` returns the full file content, `readline()` reads a single line.

**Q5: How do you append text to an existing file?**  
A: Open the file in 'a' mode and use `.write()`.

**Q6: What happens if you try to read a file that doesn’t exist?**  
A: Python raises a `FileNotFoundError`.

**Q7: Can you read and write in the same file open call?**  
A: Yes, by using 'r+' or 'w+' modes.

**Q8: What is buffering in file I/O?**  
A: Buffering improves performance by reducing direct disk operations.

**Q9: How can you read a file line by line efficiently?**  
A: Use a `for line in file:` loop.

**Q10: Why is file I/O important?**  
A: It enables data persistence across program executions.
