# Interview Q&A – Lab 14 Regular Expressions

**Q1: What is a regular expression?**
A tool for matching patterns in text.

**Q2: Difference between re.match() and re.search()?**
- re.match(): only at start of string
- re.search(): anywhere in string

**Q3: What does `\d{3}` mean in regex?**
It matches exactly 3 digits.

**Q4: How do you make regex more readable in Python?**
By using re.VERBOSE flag.

**Q5: Why use re.compile()?**
To reuse patterns efficiently.

**Q6: How to find all matches in text?**
Use re.findall().

**Q7: What’s the difference between groups and findall?**
Groups capture subpatterns, findall returns all full matches.

**Q8: How do you escape special characters in regex?**
Prefix with backslash (e.g., `\.`).

**Q9: When to use raw strings r'' in regex?**
Always recommended to avoid escaping issues.

**Q10: Real-world use case of regex in automation?**
Log parsing, form validation, or extracting structured data from text.
