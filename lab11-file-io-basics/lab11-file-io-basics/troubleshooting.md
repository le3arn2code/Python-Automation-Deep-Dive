# Troubleshooting – Lab 11

1. **FileNotFoundError** when reading a file:
   - Ensure the file exists before opening in read mode.

2. **PermissionError**:
   - Check file permissions and ensure the user has write/read rights.

3. **File overwritten accidentally**:
   - Remember that opening in 'w' mode overwrites the file. Use 'a' to append instead.
