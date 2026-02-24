Le Regex si leggono sempre da **sinistra a destra**. Ogni simbolo o gruppo di simboli definisce cosa deve apparire in una specifica posizione della stringa.

## 1. Gli Ancoraggi (Dove?)

Definiscono i confini della ricerca. Senza di questi, la regex cercherà il pattern ovunque nel testo.

| **Simbolo** | **Descrizione**                   | **Esempio**                              |
| ----------- | --------------------------------- | ---------------------------------------- |
| `^`         | **Inizio** della stringa          | `^A` (Inizia con A)                      |
| `$`         | **Fine** della stringa            | `Z$` (Finisce con Z)                     |
| `\b`        | Confine di parola (word boundary) | `\bciao\b` (Cerca solo la parola intera) |

## 2. Classi di Caratteri (Cosa?)

Definiscono il "tipo" di carattere ammesso in una singola posizione.

| **Simbolo** | **Descrizione**                                   | **Equivalente** |
| ----------- | ------------------------------------------------- | --------------- |
| `.`         | **Jolly**: qualsiasi carattere (tranne newline)   | -               |
| `\d`        | Qualsiasi **cifra** numerica                      | `[0-9]`         |
| `\D`        | Qualsiasi carattere **NON numerico**              | `[^0-9]`        |
| `\w`        | Carattere **alfanumerico** (lettere, numeri, `_`) | `[a-zA-Z0-9_]`  |
| `\s`        | Spazio bianco (spazi, tab, invio)                 | -               |
| `[abc]`     | **Set**: solo 'a', 'b', o 'c'                     | -               |
| `[a-z]`     | **Intervallo**: lettere minuscole da 'a' a 'z'    | -               |
| `[^abc]`    | **Negazione**: tutto tranne 'a', 'b', o 'c'       | -               |

## 3. Quantificatori (Quanti?)

Indicano quante volte il carattere precedente deve ripetersi.

| **Simbolo** | **Quantità**        | **Descrizione**                       |
| ----------- | ------------------- | ------------------------------------- |
| `*`         | **0 o più**         | Opzionale, ripetuto infinite volte    |
| `+`         | **1 o più**         | Obbligatorio almeno una volta         |
| `?`         | **0 o 1**           | Rende l'elemento precedente opzionale |
| `{n}`       | **Esattamente $n$** | Es: `{3}` per tre volte               |
| `{n,}`      | **Almeno $n$**      | Minimo $n$ volte                      |
| `{n,m}`     | **Da $n$ a $m$**    | Range specifico                       |

## 4. Caratteri Speciali ed Escaping

Se vuoi cercare un carattere che ha un significato speciale (come il punto o la parentesi), devi "annullare" il suo potere magico con il backslash `\`.

- **Per cercare un punto:** `\.`
- **Per cercare un punto interrogativo:** `\?`
- **Per cercare un backslash:** `\\`
- **Caratteri letterali:** Trattini `-`, underscore `_`, chiocciole `@` e lettere/numeri scritti fuori dalle quadre non hanno bisogno di escape (tranne il trattivo dentro le quadre `[-]`).


## 5. Gruppi e Logica (Come?)

| **Simbolo** | **Descrizione**                               | **Esempio**            |
| ----------- | --------------------------------------------- | ---------------------- |
| `( )`       | **Gruppo**: racchiude più elementi come unità | `(abc){2}` -> `abcabc` |
| `\|`        | **OR**: operatore logico "oppure"             | `(mela\|pera)`         |