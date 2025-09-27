# Interview Q&A - Lab 24: Python Logging Setup

1. **Q:** What is the purpose of Python's logging module?
   **A:** It provides a flexible framework for emitting log messages from applications.

2. **Q:** What are the main logging levels?
   **A:** DEBUG, INFO, WARNING, ERROR, CRITICAL.

3. **Q:** What is the default logging level in Python?
   **A:** WARNING.

4. **Q:** How do you configure logging output format?
   **A:** By using `logging.basicConfig(format=...)`.

5. **Q:** How can you log messages to a file instead of console?
   **A:** Pass `filename='app.log'` in `logging.basicConfig`.

6. **Q:** Why use logging instead of print statements?
   **A:** Logging provides severity levels, better control, persistence, and configurability.

7. **Q:** How can you prevent duplicate log entries?
   **A:** Avoid multiple `basicConfig` calls and check handler duplication.

8. **Q:** What is `logger.propagate`?
   **A:** A property that determines whether a logger passes messages to parent loggers.

9. **Q:** How to log exceptions in Python?
   **A:** Use `logging.exception("message")` inside an exception block.

10. **Q:** Can logging be configured dynamically?
    **A:** Yes, using `logging.config` module or dictConfig/YAML/JSON configs.
