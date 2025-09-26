# Interview Q&A – Lab 10 Dictionary Operations

**Q1: What is a dictionary in Python?**  
A: A dictionary is a built-in data type that stores data as key-value pairs.

**Q2: How do you retrieve a value from a dictionary?**  
A: Use `dict[key]` or `dict.get(key)`.

**Q3: What happens if you try to access a key that doesn’t exist?**  
A: It raises a KeyError unless you use `get()` which returns None or a default.

**Q4: Are dictionary keys mutable?**  
A: No, keys must be immutable types like strings, numbers, or tuples.

**Q5: Can dictionaries store duplicate keys?**  
A: No, duplicate keys overwrite earlier values.

**Q6: How do you update a dictionary?**  
A: Assign a new value to an existing key or use `update()`.

**Q7: How do you add a new key-value pair?**  
A: Simply assign a value to a new key: `dict[new_key] = value`.

**Q8: What is the difference between list and dictionary?**  
A: A list uses indices, a dictionary uses keys to access values.

**Q9: How can you iterate through a dictionary?**  
A: Using `.items()` for key-value pairs, `.keys()` for keys, and `.values()` for values.

**Q10: Why use a dictionary instead of a list?**  
A: Dictionaries provide faster lookups for key-based access, making them efficient for structured data.
