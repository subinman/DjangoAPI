import requests
import json

URL="http://127.0.0.1:8000/stuinfo/2"

r=requests.get(URL=URL)

data=r.json()

print(data)


