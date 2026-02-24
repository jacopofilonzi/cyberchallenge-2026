import requests


# Prima richiesta: ottieni il token
url = "http://web-07.challs.olicyber.it/"
response = requests.head(url)

print(response.headers.get("X-Flag"))