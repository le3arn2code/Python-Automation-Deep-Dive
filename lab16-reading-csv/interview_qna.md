# Lab 16 – Interview Q&A

**Q1: What is the csv module in Python?**  
A: It's a built-in module that allows reading and writing CSV files.

**Q2: What does csv.reader() do?**  
A: It reads CSV file content row by row into a list.

**Q3: How do you skip a header row in CSV?**  
A: Use `next(csv_reader)` before looping.

**Q4: What happens if the file does not exist?**  
A: Python raises a `FileNotFoundError`.

**Q5: How do you convert a string to integer safely?**  
A: Use `int()` inside try-except block to handle errors.

**Q6: How do you count the number of rows in a CSV?**  
A: Use a counter variable while iterating rows.

**Q7: What is the difference between 'w' and 'a' mode when opening a file?**  
A: 'w' overwrites while 'a' appends content.

**Q8: Can csv.reader handle delimiters other than commas?**  
A: Yes, pass `delimiter=';'` or another symbol to csv.reader.

**Q9: Why use CSV instead of Excel?**  
A: CSV is lightweight, plain text, and language-independent.

**Q10: How do you handle missing values in CSV files?**  
A: Check for empty strings and handle accordingly in code.
