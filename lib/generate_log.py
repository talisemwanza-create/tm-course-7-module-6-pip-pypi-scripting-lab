from datetime import datetime

import requests


API_URL = "https://jsonplaceholder.typicode.com/posts/1"

def generate_log(data):
    """Write log entries to today's log file and return its filename."""
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data(url=API_URL):
    """Fetch a JSON post, returning an empty dictionary on HTTP failure."""
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return {}


def main():
    post = fetch_data()
    title = post.get("title", "No title found")
    print("Fetched Post Title:", title)
    generate_log(["User logged in", "User updated profile", "Report exported"])


if __name__ == "__main__":
    main()
