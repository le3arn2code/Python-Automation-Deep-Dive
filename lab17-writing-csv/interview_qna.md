# Lab 17 – Writing CSV Files Q&A

**Q1: What Python module is used to handle CSV files?**  
A1: The `csv` module.

**Q2: Difference between `csv.writer` and `csv.DictWriter`?**  
A2: `csv.writer` works with sequences (lists/tuples), while `csv.DictWriter` works with dictionaries and requires fieldnames.

**Q3: Why use `newline=''` when writing CSV files?**  
A3: To prevent extra blank lines, especially on Windows.

**Q4: How do you specify headers when writing dictionaries?**  
A4: Use `writer.writeheader()` after initializing `csv.DictWriter`.

**Q5: What happens if a dictionary key is missing in `DictWriter`?**  
A5: That field will be left blank in the CSV output.

**Q6: Can you append to an existing CSV file?**  
A6: Yes, open the file in `'a'` mode instead of `'w'`.

**Q7: How do you handle special characters in CSV?**  
A7: Use `encoding='utf-8'` when opening the file.

**Q8: Is CSV format language-specific?**  
A8: No, it's plain text and supported across platforms and languages.

**Q9: What delimiter does Python’s csv module use by default?**  
A9: A comma (`,`). You can change it with `delimiter=';'` or another character.

**Q10: Where are CSV files useful in real-world scenarios?**  
A10: Data exchange, configuration files, importing/exporting data between applications, and analytics pipelines.
