import json

def fetch_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found.")
        return None

def display_data(data):
    if data:
        print("Post ID:", data["id"])
        print("Title:", data["title"])
        print("Body:", data["body"])
    else:
        print("No data to display.")

if __name__ == "__main__":
    fetched_data = fetch_data()
    display_data(fetched_data)
