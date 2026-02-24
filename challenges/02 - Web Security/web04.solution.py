import requests
import re

url = "http://web-04.challs.olicyber.it/users"
headers = {
    "Accept": "application/xml"
}

response = requests.get(url, headers=headers)

flag_match = re.search(r'flag\{[^}]+\}', response.text)
if flag_match:
    print(flag_match.group(0))
else:
    print(response.text)