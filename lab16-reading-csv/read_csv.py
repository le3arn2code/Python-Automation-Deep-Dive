import csv

# Task 2: Read CSV and print rows
with open('sample.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(f'Name: {row[0]}, Age: {row[1]}, Occupation: {row[2]}')

total_age = 0
row_count = 0

# Task 4: Summarize data
with open('sample.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # skip header
    for row in csv_reader:
        total_age += int(row[1])
        row_count += 1
        print(f'Name: {row[0]}, Age: {row[1]}, Occupation: {row[2]}')

print(f"\nTotal number of entries: {row_count}")
print(f"Total age combined: {total_age}")
