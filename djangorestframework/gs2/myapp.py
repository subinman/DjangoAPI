import requests

URL = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name': 'Sonam',
    'roll': 101,
    'city': 'Ranchi'
}

# Send JSON directly using the json= parameter
r = requests.post(url=URL, json=data)

# Safer: check status and parse JSON only if response is valid
if r.status_code == 200 or r.status_code == 201:
    try:
        data = r.json()
        print(data)
    except ValueError:
        print("Response is not valid JSON:", r.text)
else:
    print(f"Failed with status code {r.status_code}: {r.text}")
