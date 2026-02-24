import requests

session = requests.Session()

# 1) Login
payload = {
    "username": "admin",
    "password": "admin"
}
login_request = session.post(
    "http://web-11.challs.olicyber.it/login",
    json=payload,
)
login_request.raise_for_status()
data = login_request.json()
csrf = data["csrf"]          # primo token


flag_pieces = []

# 2) Richiesta dei pezzi del flag finche non trovo uno che finisce con "}"

i = 0
while True:
    r = session.get(
        "http://web-11.challs.olicyber.it/flag_piece",
        params={"index": i, "csrf": csrf},  # csrf in query string
    )
    if r.status_code != 200:
        print("Finito a index", i, ":", r.text)
        break

    data = r.json()
    flag_piece = data["flag_piece"]
    flag_pieces.append(flag_piece)
    csrf = data["csrf"]      # aggiorna il token per la chiamata successiva
    
    if flag_piece.endswith("}"):
        break
    
    i += 1

print("".join(flag_pieces))