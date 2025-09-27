# Troubleshooting – Lab 17 Writing CSV Files

1. **Extra blank lines in CSV (Windows users):**
   - Use `newline=''` when opening the file in write mode.

2. **Encoding errors when writing special characters:**
   - Open file with `encoding='utf-8'`.

3. **File not created:**
   - Ensure you have write permissions in the working directory.
