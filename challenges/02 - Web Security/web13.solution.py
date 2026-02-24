import requests
from bs4 import BeautifulSoup

url = "http://web-13.challs.olicyber.it/"
response = requests.get(url)

#  Analizza l'HTML con BeautifulSoup
zuppa = BeautifulSoup(response.text, 'html.parser')

# Trova tutti i tag <span> con classe "red"
paragrafi = zuppa.find_all('span', class_='red')


flag_content = ""

for p in paragrafi:
    flag_content += p.text

print(f"flag{{{flag_content}}}")

