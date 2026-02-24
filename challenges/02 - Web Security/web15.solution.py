import requests
from bs4 import BeautifulSoup as soup, Comment
import re

base_url = "http://web-15.challs.olicyber.it"
response = requests.get(base_url)

#  Analizza l'HTML con BeautifulSoup
zuppa = soup(response.text, 'html.parser')

links = [tag.get('href') for tag in zuppa.find_all('link', href=True)]

scripts = [tag.get('src') for tag in zuppa.find_all('script', src=True)]


for url in [*links, *scripts]:
    resource = requests.get(f"{base_url}/{url}")
    if resource.status_code == 200:
        match = re.search(r"flag\{.*?\}", resource.text)
        if match:
            print(match.group(0))