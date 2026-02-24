## Operandi
| **Categoria**    | **Operatore (Simbolo)** | **Operatore (Inglese)** | **Descrizione**              | **Esempio**                  |
| ---------------- | ----------------------- | ----------------------- | ---------------------------- | ---------------------------- |
| **Confronto**    | `==`                    | `eq`                    | Uguale a                     | `ip.src == 10.0.0.1`         |
|                  | `!=`                    | `ne`                    | Diverso da                   | `tcp.port != 80`             |
|                  | `>`                     | `gt`                    | Maggiore di                  | `frame.len > 500`            |
|                  | `<`                     | `lt`                    | Minore di                    | `frame.len < 100`            |
|                  | `>=`                    | `ge`                    | Maggiore o uguale            | `tcp.window_size >= 1024`    |
|                  | `<=`                    | `le`                    | Minore o uguale              | `tcp.window_size <= 512`     |
| **Logici**       | `&&`                    | `and`                   | AND logico (entrambi veri)   | `ip.addr == 1.1.1.1 && tcp`  |
|                  | `\|`                    | `or`                    | OR logico (almeno uno vero)  | `http                        |
|                  | `^^`                    | `xor`                   | XOR logico (esclusivo)       | `tr.dst[0:3] ^^ tr.src[0:3]` |
|                  | `!`                     | `not`                   | Negazione                    | `!ip.addr == 192.168.1.1`    |
| **Appartenenza** | `in`                    | `in`                    | Set di valori o range        | `tcp.port in {80 443 8080}`  |
| **Stringhe**     | `~`                     | `matches`               | Espressione regolare (Regex) | `http.host matches "google"` |
|                  | `contains`              | `contains`              | Contiene una sequenza        | `http.uri contains "admin"`  |

**NOTE:**
- **Sottostringhe:** È possibile usare le parentesi quadre per filtrare porzioni di dati, es: `eth.src[0:3] == 00:00:5e`.
- **Raggruppamento logico:** Si possono usare le parentesi tonde `(` `)` per raggruppare le operazioni logice

## Known filter flags

- **pkt_comment:** i file pcap possono avere dei commenti