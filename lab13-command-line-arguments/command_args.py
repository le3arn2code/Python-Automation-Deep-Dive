# Lab 13 – Command-Line Arguments
import sys
import argparse

print("Number of arguments:", len(sys.argv))
print("Argument List:", str(sys.argv))

# Print each argument separately
for i, arg in enumerate(sys.argv):
    print(f"Argument {i}: {arg}")

# Handle case where no arguments are provided
if len(sys.argv) == 1:
    print("No command-line arguments provided.")

# Using argparse
parser = argparse.ArgumentParser(description='Example script to demonstrate command-line arguments')
parser.add_argument('name', type=str, help='Name of the user')
parser.add_argument('--age', type=int, help='Age of the user', required=False, default=25)

args = parser.parse_args()
print(f"Name: {args.name}")
print(f"Age: {args.age}")
