import requests


# Prima richiesta: ottieni il token
url = "http://web-10.challs.olicyber.it/"

response = requests.put(url)

print(response.headers.get("X-Flag"))