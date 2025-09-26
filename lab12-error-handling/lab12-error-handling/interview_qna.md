# Interview Q&A – Lab 12 Error Handling

**Q1: What is exception handling in Python?**
A1: It is the process of responding to exceptions (errors) gracefully using try-except blocks.

**Q2: What is the difference between syntax errors and exceptions?**
A2: Syntax errors prevent code from running, exceptions occur during runtime.

**Q3: How does the try-except block work?**
A3: Code inside try is executed, if an exception occurs, control shifts to the except block.

**Q4: Can multiple except blocks be used?**
A4: Yes, to handle different types of exceptions specifically.

**Q5: What is ZeroDivisionError?**
A5: An exception raised when dividing by zero.

**Q6: What is ValueError?**
A6: Raised when an invalid value is used for an operation (e.g., converting text to int).

**Q7: Why is exception handling important?**
A7: It makes applications more robust and prevents unexpected crashes.

**Q8: What is the use of 'finally' in Python?**
A8: Code inside finally executes regardless of whether an exception occurred.

**Q9: How do you raise a custom exception?**
A9: Using the `raise` keyword with an exception type.

**Q10: What are best practices for error handling?**
A10: Catch specific exceptions, provide clear messages, and avoid bare except clauses.
