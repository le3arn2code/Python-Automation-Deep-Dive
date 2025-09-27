import requests
import json

api_url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    post_info = {"title": data['title'], "body": data['body']}

    print("Extracted Post Information:")
    print(post_info)

    with open('post_info.json', 'w') as json_file:
        json.dump(post_info, json_file, indent=4)

    print("Data saved to post_info.json")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
