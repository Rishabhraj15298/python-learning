import requests

# ------------------------ Random Products ------------------------
def fetch_random_items_detail():
    """
    Fetches a list of random products from FreeAPI.
    Returns a list of tuples containing (title, brand).
    """
    url = "https://api.freeapi.app/api/v1/public/randomproducts"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if HTTP request failed

    content = response.json()

    # Check if the response contains valid data
    if content["success"] and content["data"] and "data" in content["data"]:
        item_data = content["data"]["data"]
        items = []
        for item in item_data:
            # Use get() to avoid KeyErrors
            title = item.get("title", "N/A")
            brand = item.get("brand", "N/A")
            items.append((title, brand))
        return items
    else:
        raise Exception("Failed to fetch details or no data found")


def main_products():
    """Prints random products fetched from API."""
    try:
        items = fetch_random_items_detail()
        for i, (title, brand) in enumerate(items, start=1):
            print(f"Item {i}: Title = {title}, Brand = {brand}")
    except Exception as e:
        print(str(e))


# ------------------------ Random Jokes ------------------------
def fetch_random_jokes():
    """
    Fetches a random joke from FreeAPI.
    Returns the joke as a string.
    """
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    response.raise_for_status()  # Raises exception for HTTP errors

    data = response.json()

    # Extract joke content
    if data["success"] and data["data"]:
        joke = data["data"]["content"]
        return joke
    else:
        raise Exception("Failed to fetch joke")


def main_jokes():
    """Prints a random joke fetched from API."""
    try:
        joke = fetch_random_jokes()
        print(f"Random joke: {joke}")
    except Exception as e:
        print(str(e))


# ------------------------ Simulated POST Request ------------------------
def add_joke():
    """
    Simulates adding a joke by POSTing to httpbin.org.
    Returns the response JSON.
    """
    url = "https://httpbin.org/post"
    payload_joke = {
        "statusCode": 200,
        "success": True,
        "message": "Random joke fetched successfully",
        "data": {
            "id": 490,
            "categories": [],
            "content": "Sometimes it's hard to see Chuck Norris for all the steam rising from his 'nads."
        }
    }

    response = requests.post(url, json=payload_joke)
    
    if response.ok:
        print("Data added successfully")
        return response.json()
    else:
        raise Exception("Failed to add details")


def main_add_joke():
    """Performs the simulated POST request and prints the response."""
    try:
        jokes = add_joke()
        print(f"Response: {jokes}")
    except Exception as e:
        print(str(e))


# ------------------------ Run Scripts ------------------------
if __name__ == "__main__":
    print("Fetching random products...")
    main_products()
    print("\nFetching a random joke...")
    main_jokes()
    print("\nSimulating adding a joke via POST...")
    main_add_joke()
