import requests

url = "http://web-01.challs.olicyber.it"
headers = {
    "X-Password": "admin"
}

response = requests.get(url, headers=headers)

print(response.text)