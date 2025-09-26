# Troubleshooting – Lab 10

1. **KeyError** when accessing dictionary keys:
   - Ensure the key exists before accessing it.
   - Use `dict.get(key)` to safely retrieve values.

2. **SyntaxError** when defining dictionary:
   - Ensure keys and values are separated by colons `:` and pairs by commas `,`.

3. **Overwriting keys**:
   - Remember dictionary keys must be unique. Defining the same key twice will overwrite the previous value.
