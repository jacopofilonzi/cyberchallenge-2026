# Web 06 - HTTP: ricevere un cookie

Quello dei cookie non è un meccanismo ridondante rispetto agli altri tipi di parametro osservati finora. A differenza di essi, infatti, il server è in grado di richiedere l'installazione di cookie da esso forniti nella memoria del client. Questi cookie vengono associati al sito che li ha generati, e possono contenere una data di scadenza.

Nei browser web questa memorizzazione viene gestita automaticamente, e i cookie salvati vengono automaticamente inviati nelle richieste successive inviate allo stesso sito, e cancellati al raggiungimento della data indicata. In questo modo essi possono essere utilizzati per identificare una sessione con un client specifico, ovvero una serie di richieste consecutive eseguite dallo stesso dispositivo, anche quando più dispositivi sono connessi a internet attraverso la stessa sottorete e quindi condividono indirizzo IP.

L'obiettivo di questa challenge è eseguire una richiesta GET alla risorsa http://web-06.challs.olicyber.it/token che cercherà di installare un cookie di sessione, una volta ottenuto il quale sarà possibile accedere a http://web-06.challs.olicyber.it/flag per ottenere la flag.

La funzione get della libreria requests usata finora adotta un modello senza stato, ovvero non utilizza nessuna delle informazioni precedentemente ricevute dal server nella composizione delle richieste successive. Per completare questa challenge, si consiglia di istanziare un oggetto di classe [Session](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects) ed eseguire le richieste tramite il suo metodo get, che differisce dalla normale funzione get proprio per la caratteristica di salvare queste informazioni all'interno dell'oggetto emulando parzialmente il comportamento un browser.
