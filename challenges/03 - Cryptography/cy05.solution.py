ciphertext_hex = "104e137f425954137f74107f525511457f5468134d7f146c4c"
data = bytes.fromhex(ciphertext_hex)

print("Tentativi di decifrazione:")
print("-" * 30)

# La chiave è un singolo byte, quindi provo tutte le possibili chiavi da 0 a 255
for k in range(256):
    plaintext_bytes = bytes([b ^ k for b in data])
    
    try:
        # decodifica i byte in ASCII
        decoded = plaintext_bytes.decode('ascii')
        
        # Escludo il testo che può sembrare insensato o non stampabile
        if all(32 <= b <= 126 for b in plaintext_bytes):
            if "_" in decoded: # quasi sicuramente contiene un underscore
                print(f"Chiave {k} (0x{k:02x}): flag{{{decoded}}}")
    except:
        # Salta se i byte non sono rappresentabili in ASCII
        continue