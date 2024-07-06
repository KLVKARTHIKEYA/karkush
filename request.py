import requests
import json
# Define the URL of the Flask endpoint
url = 'http://127.0.0.1:5000/login'
# Authentication credentials and token (replace with actual data)
payload = {
    "username": "test",
    "password": "test"
}
response = requests.get(url,json=payload)
response = requests.get(url,json=payload)
data = response.json()
# Example JWT token (replace with your actual JWT token)
print(data)
# Example file to send
# Prepare headers with the JWT token
# headers = {
#     "Authorization": f"Bearer {jwt_token}",
# }

