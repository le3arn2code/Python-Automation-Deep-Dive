# Interview Q&A – Lab 19

1. What is JSON? -> A lightweight data-interchange format.
2. How do you parse JSON in Python? -> `response.json()`.
3. How can you save a dict to JSON file? -> `json.dump()`.
4. What HTTP status code indicates success? -> 200.
5. Which Python module is used for API requests? -> `requests`.
6. What does `response.status_code` return? -> The HTTP status code.
7. How do you pretty-print JSON? -> Use `indent=4` in `json.dump()`.
8. Why is JSON widely used in APIs? -> Lightweight, human-readable, language-independent.
9. How do you handle request failures? -> Check status code and use try/except.
10. Difference between `json.load()` and `json.loads()`? -> `load()` reads from file, `loads()` parses a string.
