# Interview Q&A – Lab 25 (argparse)

1. **What is argparse in Python?**
   - A standard library module for parsing command-line arguments.

2. **Difference between positional and optional arguments?**
   - Positional are mandatory, optional are prefixed with `--`.

3. **How do you specify default values for arguments?**
   - Use the `default` parameter in `add_argument`.

4. **How can you restrict input values to specific options?**
   - Use the `choices` parameter.

5. **What does `action='store_true'` do?**
   - Sets a boolean flag to `True` if the option is specified.

6. **How do you show help information?**
   - argparse automatically generates help with `-h` or `--help`.

7. **What is the difference between `parse_args()` and `parse_known_args()`?**
   - `parse_args()` throws errors on unknown args, `parse_known_args()` ignores them.

8. **How to parse integer arguments?**
   - Use `type=int` in `add_argument`.

9. **How do you handle multiple file inputs in argparse?**
   - Use `nargs='+'` or `nargs='*'` with the file argument.

10. **Why use argparse over sys.argv?**
   - Provides structured parsing, validation, defaults, and help generation.
