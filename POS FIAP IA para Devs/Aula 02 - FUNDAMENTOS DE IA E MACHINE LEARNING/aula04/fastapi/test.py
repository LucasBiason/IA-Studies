import requests
import json

url = "localhost:8000/items"

payload = json.dumps({
  "name": "Example",
  "description": "This is an example description for the item.",
  "price": 10.99,
  "on_offer": False
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)