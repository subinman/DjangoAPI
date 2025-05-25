import json
import requests

URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    params = {}
    if id is not None:
        params = {'id': id}
    r = requests.get(url=URL, params=params)
    data = r.json()
    print(data)

# Call the function outside the definition
# get_data()  # Get all data
# get_data(1)  # To get data for student with ID 1

def post_data():
    data = {
        'name': 'Ravi',
        'roll': 104,
        'city': 'Hetuda'
    }

    try:
        r = requests.post(url=URL, json=data)  # Correct way to send JSON
        print("Status Code:", r.status_code)
        print("Response Text:", r.text)

        # Try parsing response JSON
        response_data = r.json()
        print("Parsed JSON:", response_data)

    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response was:")
        print(r.text)

# post_data()

def update_data():
    data = {
        'id': 3,
        'name': 'Ravi',
        'roll': 104,
        'city': 'Hetuda'
    }

    try:
        r = requests.put(url=URL, json=data)  # Correct way to send JSON
        print("Status Code:", r.status_code)
        print("Response Text:", r.text)

        # Try parsing response JSON
        response_data = r.json()
        print("Parsed JSON:", response_data)

    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response was:")
        print(r.text)

# update_data()

def delete_data():
    data = {
        'id': 3
    }

    try:
        r = requests.delete(url=URL, json=data)  # Correct way to send JSON
        print("Status Code:", r.status_code)
        print("Response Text:", r.text)

        # Try parsing response JSON
        response_data = r.json()
        print("Parsed JSON:", response_data)

    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response was:")
        print(r.text)

delete_data()
