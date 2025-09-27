# Lab 26 – Interview Q&A

**Q1: What library did you use to work with Excel in Python?**  
A: We used `openpyxl` for creating and reading Excel files.

**Q2: How do you create a new Excel workbook in Python?**  
A: By using `Workbook()` from `openpyxl`.

**Q3: How do you access the active worksheet?**  
A: Using `workbook.active`.

**Q4: How do you read a specific cell value?**  
A: Access it by cell reference, e.g., `sheet['A1'].value`.

**Q5: How can you iterate over rows in openpyxl?**  
A: Using `sheet.iter_rows()` with `values_only=True`.

**Q6: What function is used to save the workbook?**  
A: `workbook.save("filename.xlsx")`.

**Q7: How do you calculate a column sum?**  
A: Iterate over the column and sum the values.

**Q8: What is the default file format supported by openpyxl?**  
A: `.xlsx` files.

**Q9: Why might you use pandas instead of openpyxl?**  
A: For more advanced data analysis and manipulation.

**Q10: What is the importance of logging errors when handling Excel files?**  
A: Logging helps identify issues like missing files, permission errors, or invalid data types.
