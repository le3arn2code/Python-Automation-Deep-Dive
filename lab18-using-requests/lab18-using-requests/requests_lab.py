# Lab 18 – Using the requests Module
import requests

# Send GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check if request was successful
if response.status_code == 200:
    print("Request was successful!")
else:
    print(f"Request failed with status code: {response.status_code}")

# Parse JSON
data = response.json()

# Print fields
print(f"Title: {data['title']}")
print(f"Body: {data['body']}")
