import re

# Define the pattern for a phone number
phone_pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')

def find_phone_numbers(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        return phone_pattern.findall(text)

if __name__ == "__main__":
    file_name = 'contacts.txt'
    matches = find_phone_numbers(file_name)
    if matches:
        print("Phone numbers found:")
        for match in matches:
            print(match)
    else:
        print("No phone numbers found.")
