import requests

url = "http://web-01.challs.olicyber.it"
params = {"id": "flag"}
response = requests.get(url, params=params)

print(response.text)