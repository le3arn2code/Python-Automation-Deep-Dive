# Interview Q&A – Lab 29

**Q1.** What is pandas in Python?  
**A1.** A powerful data analysis library used for manipulating structured data.

**Q2.** How do you read a CSV into pandas?  
**A2.** Using `pd.read_csv('file.csv')`.

**Q3.** How do you preview data in pandas?  
**A3.** Use `df.head()` for first rows or `df.tail()` for last rows.

**Q4.** How do you filter rows by a condition?  
**A4.** Example: `df[df['Age'] > 30]`.

**Q5.** What happens if the column name is wrong?  
**A5.** pandas raises a `KeyError`.

**Q6.** How do you save a DataFrame to CSV?  
**A6.** `df.to_csv('file.csv', index=False)`.

**Q7.** What data structures does pandas provide?  
**A7.** `Series` (1D) and `DataFrame` (2D).

**Q8.** How do you check column names?  
**A8.** `df.columns`.

**Q9.** How does pandas handle missing values?  
**A9.** With functions like `dropna()` and `fillna()`.

**Q10.** Why use pandas over pure Python lists/dicts?  
**A10.** Easier handling of tabular data, optimized performance, and built-in functions.
