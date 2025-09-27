# Troubleshooting – Lab 25

1. **ModuleNotFoundError: No module named argparse**
   - argparse is part of Python's standard library. Ensure you are using Python 3.x.

2. **File not found error**
   - Ensure the file specified in `--file` exists in the correct directory.

3. **Invalid choice for --level**
   - The `--level` argument only accepts 1, 2, or 3.

4. **Default values not applied**
   - Ensure you defined defaults in `parser.add_argument`.

5. **Script doesn’t execute**
   - Verify Python 3 is installed and use `python3` instead of `python` on some systems.
