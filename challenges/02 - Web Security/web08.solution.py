import requests


# Prima richiesta: ottieni il token
url = "http://web-08.challs.olicyber.it/login"
data = {
    "username": "admin",
    "password": "admin"
}
response = requests.post(url, data=data)

print(response.text)