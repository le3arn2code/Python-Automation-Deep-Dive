# Troubleshooting - Lab 27

1. **Error: `ModuleNotFoundError: No module named 'requests'`**
   - Solution: Install requests using `pip install requests` or `sudo apt install python3-requests`.

2. **Error: `python: command not found`**
   - Solution: Use `python3` instead of `python`.

3. **Error: Invalid JSON in response**
   - Solution: Check the endpoint URL. Use `https://httpbin.org/post` for testing.

4. **Script runs but no output**
   - Ensure `print()` statements are included to display results.
