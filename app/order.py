import requests
api_url = "http://127.0.0.1:5000/"
order = {"pizza": "napolitana", "size": "family", "amount": 2}
response = requests.post(api_url+"order", json=order)
print(response.json())

response = requests.get(api_url+"ping")
print(response.json())

response = requests.get(api_url+"health")
print(response.json())