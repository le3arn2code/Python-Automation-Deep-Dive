# Troubleshooting – Lab 21

## Common Issues & Fixes

### 1. ModuleNotFoundError: No module named 'subprocess'
- subprocess is part of Python's standard library. Ensure you are using Python 3.x.

### 2. CommandNotFoundError
- If 'ls' does not work (Windows), replace it with 'dir' and set `shell=True` in subprocess.

### 3. Permission denied
- Ensure your Python script has execute permissions and you are running in the correct directory.
