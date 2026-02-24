import requests
from bs4 import BeautifulSoup as soup, Comment

url = "http://web-14.challs.olicyber.it/"
response = requests.get(url)

#  Analizza l'HTML con BeautifulSoup
zuppa = soup(response.text, 'html.parser')

# Trova tutti i commenti HTML
commenti = zuppa.find_all(string=lambda text: isinstance(text, Comment))

for commento in commenti:
    if "flag" in commento.lower():
        print(commento.strip())

