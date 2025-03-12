import requests

endpoint = "https://httpbin.org"

response = requests.get(endpoint)
print(response.text)