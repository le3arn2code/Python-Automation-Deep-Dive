# Troubleshooting – Lab 9 Lists and Tuples

## Issue: Error with Tuple Modification
Error: 'tuple' object does not support item assignment

### Cause
- Tuples in Python are immutable.
- Once created, their elements cannot be changed.

### Resolution
- This is expected behavior, not a bug.
- To use a modifiable collection, use a list instead of a tuple.
