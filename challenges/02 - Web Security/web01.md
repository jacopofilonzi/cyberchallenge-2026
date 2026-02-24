# Web 01 - HTTP: una semplice richiesta GET

In questa serie di challenge introduttive per la web security saranno presentati il protocollo HTTP e le principali tecnologie web ad esso comunemente associate, e alcuni semplici strumenti per interagirvi.

Le singole challenge seguiranno il modello jeopardy, concentrandosi quindi sull'ottenimento di flag.

Gli esempi e le spiegazioni proposti faranno riferimento al linguaggio Python e alla sua libreria standard, nonché alle librerie requests e BeautifulSoup, che si consiglia quindi di installare per seguire al meglio questo percorso.

Installazione delle librerie consigliate su Debian e Ubuntu Linux:

`sudo apt install python3-requests python3-bs4`

Sui sistemi Windows, installare manualmente l'interprete Python ottenibile dal sito ufficiale del progetto Python ed eseguire nel prompt dei comandi

`pip install requests bs4`

Concepito per facilitare l'accesso a documenti ipertestuali, lo HyperText Transfer Protocol HTTP è oggi utilizzato per trasferire informazioni di ogni tipo da e verso server remoti attraverso la rete. Queste informazioni sono organizzate in risorse, identificate da stringhe di indirizzo dette URL (Unified Resource Locators), e le operazioni fondamentali eseguibili su queste risorse sono dette verbi HTTP.

Il più semplice di questi verbi, GET, è utilizzato per ottenere una una risorsa da un server remoto. L'obiettivo di questa challenge è ottenere il testo della risorsa radice del server web-01.challs.olicyber.it, identificata dall'URL http://web-01.challs.olicyber.it/

Si consiglia di utilizzare la funzione [get](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request) della libreria requests.

Approfondimento: è possibile osservare che un URL è generalmente composto da uno schema (in questo caso http) che identifica il meccanismo di accesso alla risorsa, un indirizzo internet opzionalmente comprensivo di porta (web-01.challs.olicyber.it) e un percorso (in questo caso / che identifica la risorsa radice). Le risorse sono organizzate in una struttura ad albero che ricorda quella di un file system, in cui / è la risorsa principale, mentre le risorse figlie sono identificate come /risorsa1, /risorsa2, /super-risorsa/sotto-risorsa, /risorsa/annidata/su/cinque/livelli. Questo rende possibile rappresentare facilmente risorse decomponibili in parti più piccole (p.e. /utenti la risorsa che rappresenta tutti gli utenti di un sito, mentre /utenti/luca rappresenta un unico utente, Luca).