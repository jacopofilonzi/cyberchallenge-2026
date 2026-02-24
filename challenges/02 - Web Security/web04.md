# Web 04 - HTTP: l'header Accept

Quello di risorsa, in HTTP, è un concetto molto astratto. Una risorsa non designa necessariamente un file su un disco, ma potrebbe tranquillamente essere un dispositivo hardware, il contenuto di un database, l'output di un programma, o più in generale qualsiasi cosa sia rappresentabile astrattamente come una collezione di dati.

Quando "richiediamo una risorsa" tramite HTTP, non stiamo veramente ricevendo la risorsa originale (che in certi casi non è neanche fisicamente trasferibile tramite la rete, si pensi all'esempio di un dispositivo hardware), bensì una sua rappresentazione.

Le risorse che vengono offerte da un server hanno solitamente una singola rappresentazione, ma in alcuni casi è possibile richiedere (e ricevere) più rappresentazioni equivalenti, in modo da poter scegliere il formato che è più semplice da elaborare per il client.

Lo header Accept inviato come parte della richiesta specifica una lista di formati che il client considera "accettabili" in ordine di preferenza, usando un sistema di classificazione detto tipo MIME (un elenco completo dei tipi MIME disponibili è consultabile sul sito ufficiale dell'organizzazione [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml) che si occupa di assegnarli).

Talvolta, a causa ad esempio di una disattenzione legata alle differenti caratteristiche dei vari formati, le varie rappresentazioni di una risorsa non sono veramente equivalenti, e una rappresentazione alternativa può rivelare informazioni aggiuntive che si pensavano segrete.

L'obiettivo di questa challenge è richiedere la risorsa http://web-04.challs.olicyber.it/users utilizzando la rappresentazione alternativa application/xml anziché quella di default application/json.

Si consiglia di provare ad ottenere la risorsa normalmente, e successivamente specificando un tipo di rappresentazione diversa (application/xml) tramite lo header Accept.