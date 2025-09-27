import requests
import csv
import logging
import argparse
import sys

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_data(api_url):
    """Fetch data from API"""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        logging.info("Data fetched successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        sys.exit(1)

def process_data(data, user_id):
    """Filter and transform data"""
    processed_data = [{"userId": post["userId"], "title": post["title"]} for post in data]
    user_posts = [post for post in processed_data if post["userId"] == user_id]
    logging.info(f"Processed {len(user_posts)} posts for user {user_id}")
    return user_posts

def save_to_csv(data, filename="user_posts.csv"):
    """Save data to CSV"""
    try:
        with open(filename, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["userId", "title"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.error(f"Error writing to file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and process API data")
    parser.add_argument("--user_id", type=int, default=1, help="User ID to filter posts by")
    args = parser.parse_args()

    API_URL = "https://jsonplaceholder.typicode.com/posts"

    # Workflow
    data = fetch_data(API_URL)
    print(f"Fetched {len(data)} records from API")

    user_posts = process_data(data, args.user_id)
    print(f"User {args.user_id} has {len(user_posts)} posts")

    save_to_csv(user_posts)
    print("Results saved to user_posts.csv")
