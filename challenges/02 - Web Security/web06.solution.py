import requests


# Prima richiesta: ottieni il token
url1 = "http://web-06.challs.olicyber.it/token"
response1 = requests.get(url1)
token = response1.cookies.get("token")

if not isinstance(token, str):
    raise ValueError("Token non è una stringa")

# Seconda richiesta: usa il token condiviso
url2 = "http://web-06.challs.olicyber.it/flag"
cookies = {"token": token}
response2 = requests.get(url2, cookies=cookies)

print(response2.text)

