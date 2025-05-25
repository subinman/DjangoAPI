import json
import requests

URL = 'http://127.0.0.1:8000/studentapi/'

# def get_data(id=None):
#     params = {}
#     if id is not None:
#         params = {'id': id}
    
#     try:
#         r = requests.get(url=URL, params=params)
#         print("Status Code:", r.status_code)
#         print("Response Text:", r.text[:200])  # Print first 200 chars of response
        
#         # Safely try to parse JSON
#         data = r.json()
#         print("JSON Data:", data)
#     except requests.exceptions.JSONDecodeError:
#         print("❌ Error: Response is not valid JSON. Check the API endpoint or server.")
#     except requests.exceptions.RequestException as e:
#         print("❌ Request failed:", e)

#get_data()  # Get all data
# get_data(1)  # To get data for student with ID 1

# def post_data():
#     data = {
#         'name': 'RaviRaj',
#         'roll': 110,
#         'city': 'Janakpur'
#     }

#     try:
#         r = requests.post(url=URL, json=data)
#         print("Status Code:", r.status_code)

#         try:
#             response_data = r.json()
#             print("Parsed JSON:", response_data)
#         except requests.exceptions.JSONDecodeError:
#             print("Failed to decode JSON. Response text:")
#             print(r.text)

#     except requests.exceptions.RequestException as e:
#         print("Request failed:", e)
# post_data()

# def update_data():
#     data = {
#         'id': 1,                # Existing student ID
#         'name': 'Ravi Raj Updated',
#         'roll': 110,
#         'city': 'Kathmandu'
#     }

#     try:
#         r = requests.put(url=URL, json=data)
#         print("Status Code:", r.status_code)
#         print("Response:", r.json())
#     except requests.exceptions.RequestException as e:
#         print("Request failed:", e)
#     except requests.exceptions.JSONDecodeError:
#         print("Response is not valid JSON:", r.text)

# update_data()

# def delete_data():
#     data = {'id': 1}  # Replace with actual ID to delete

#     try:
#         r = requests.delete(url=URL, json=data)
#         print("Status Code:", r.status_code)
#         print("Response:", r.json())
#     except requests.exceptions.RequestException as e:
#         print("Request failed:", e)
#     except requests.exceptions.JSONDecodeError:
#         print("Response is not valid JSON:", r.text)

# delete_data()
