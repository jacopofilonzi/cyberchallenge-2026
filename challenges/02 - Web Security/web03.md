# Web 03 - HTTP: richiesta GET con header manuale

Quando viene inviata una richiesta HTTP, oltre al verbo, al percorso della risorsa desiderata e ad eventuali parametri associati, vengono comunicate al server alcune informazioni aggiuntive in campi detti header (dal fatto che vengono inviati nella prima parte del messaggio HTTP). Allo stesso modo, anche il server allegherà alla risposta degli header in aggiunta al contenuto richiesto. Questi header differiscono dai parametri della richiesta GET perché non vengono utilizzati per specificare la risorsa richiesta, ma contengono informazioni riguardanti il client (detto user-agent), il server e il canale di comunicazione, metadati associati alle risorse ed eventuali informazioni di debug.

Questi header vengono generalmente inseriti automaticamente dalle librerie client e dal server e appartengono ad un insieme standard definito come parte del protocollo stesso; ciononostante è possibile specificarne di aggiuntivi per soddisfare le esigenze di particolari applicazioni. Questi header non-standard hanno normalmente nomi che iniziano per X- e quando vengono inviati a un sistema non in grado di riconoscerli vengono solitamente ignorati.

In questa challenge, uno header non-standard è stato usato per fornire un meccanismo di autenticazione artigianale. L'obiettivo è ottenere il testo della risorsa all'indirizzo http://web-03.challs.olicyber.it/flag, ma il server risponderà solo a richieste che conterranno lo header X-Password contenente la password corretta, admin.

Si consiglia di utilizzare [la parola chiave headers](https://requests.readthedocs.io/en/latest/user/quickstart/#custom-headers) della funzione get utilizzata nelle challenge precedenti.

N.B.: il protocollo HTTP fornisce già diversi meccanismi di autenticazione tramite lo header standard Authorization, che sono generalmente più complessi dell'esempio di autenticazione "artigianale" presentato in questa challenge. Anziché manipolare direttamente lo header Authorization, quando necessario librerie come requests forniscono [metodi specifici](https://requests.readthedocs.io/en/latest/user/authentication/) per interfacciarsi con esso.

