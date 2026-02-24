import requests
from bs4 import BeautifulSoup

url = "http://web-12.challs.olicyber.it/"
response = requests.get(url)

#  Analizza l'HTML con BeautifulSoup
zuppa = BeautifulSoup(response.text, 'html.parser')

# Trova tutti i paragrafi <p>
paragrafi = zuppa.find_all('p')

# Estrai il testo del secondo paragrafo (indice 1)
if len(paragrafi) >= 2:
    flag = paragrafi[1].text
    print(flag)
else:
    print("Secondo paragrafo non trovato.")


print(response.text)