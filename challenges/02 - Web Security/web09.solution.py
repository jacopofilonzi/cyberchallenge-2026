import requests


# Prima richiesta: ottieni il token
url = "http://web-09.challs.olicyber.it/login"
json_data = {
    "username": "admin",
    "password": "admin"
}
headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, headers=headers, json=json_data)

data = response.json()
print(data["token"])