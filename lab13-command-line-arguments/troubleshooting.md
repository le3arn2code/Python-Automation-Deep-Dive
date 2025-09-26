# Troubleshooting for Lab 13

- **Error: argparse requires arguments**
  - Cause: You did not provide the required positional argument `name`.
  - Fix: Run `python3 command_args.py Alice`

- **Error: invalid literal for int()**
  - Cause: You passed a non-integer to `--age`.
  - Fix: Provide a valid integer, e.g. `--age 30`
