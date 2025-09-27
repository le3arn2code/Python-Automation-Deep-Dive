import argparse

parser = argparse.ArgumentParser(description="Enhanced CLI Example")

parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
parser.add_argument('--file', type=str, help='File path to process')
parser.add_argument('--level', type=int, choices=[1, 2, 3], help='Set the level of operation')
parser.add_argument('--timeout', type=int, default=30, help='Timeout duration in seconds')

args = parser.parse_args()

if args.verbose:
    print("Verbose mode is activated.")

if args.file:
    print(f"Processing file: {args.file}")

if args.level:
    print(f"Level set to: {args.level}")

print(f"Timeout set to: {args.timeout} seconds")
