# Troubleshooting - Lab 24: Python Logging Setup

1. **No logs appearing in console**
   - Ensure you used `logging.basicConfig(level=logging.DEBUG, ...)` before logging calls.

2. **File not created when using filename**
   - Check permissions in the directory.
   - Ensure correct `filename='app.log'` in `basicConfig`.

3. **Duplicate log messages**
   - Avoid calling `basicConfig()` multiple times.
   - Restart Python session if needed.

4. **Encoding issues in log file**
   - Use `encoding='utf-8'` in `basicConfig()`.
