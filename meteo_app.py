import requests         # si importa la libreria 'requests' per fare richieste HTTP
import json         # si importa la libreria 'json' per visualizzare meglio i dati JSON
import config



api_key = config.api_key


base_url = "http://api.openweathermap.org/data/2.5/weather"     # URL di base dell'API per il meteo attuale

# Inizio del ciclo principale del programma
while True:

    nome_citta_utente = input("\nInserisci il nome della città (o premi Invio senza testo per uscire): ")

    # Condizione di uscita: se l'utente preme Invio senza inserire testo
    if not nome_citta_utente: # Controlla se la stringa è vuota
        print("Nessuna città inserita. Uscita dal programma...")
        break # Interrompe il ciclo while


    # Costruiamo l'URL completo con i parametri necessari, usando l'input dell'utente
    url_completo = f"{base_url}?q={nome_citta_utente}&appid={api_key}&units=metric"

    print(f"Sto contattando l'URL: {url_completo}\n") # Utile per debug

    # Si effettua la richiesta GET all'API
    # Si aggiunge un blocco try-except per gestire possibili errori di connessione o API
    try:
        risposta_api = requests.get(url_completo, timeout=10) # Timeout di 10 secondi

        # Controlliamo se la richiesta ha avuto successo (codice di stato 200 OK)
        if risposta_api.status_code == 200:
            print("Richiesta API riuscita!\n")
            dati_meteo = risposta_api.json()

            nome_citta_api = dati_meteo.get("name")
            dati_principali = dati_meteo.get("main", {})
            temperatura = dati_principali.get("temp")
            umidita = dati_principali.get("humidity")
            temperatura_percepita = dati_principali.get("feels_like")

            lista_weather = dati_meteo.get("weather", [])
            descrizione_meteo = "Non disponibile"
            if lista_weather and isinstance(lista_weather[0], dict):
                descrizione_meteo = lista_weather[0].get("description", "Non disponibile")

            dati_vento = dati_meteo.get("wind", {})
            velocita_vento = dati_vento.get("speed")

            print(f"\n--- Meteo Attuale per {nome_citta_api} ---")
            if temperatura is not None: print(f"  Temperatura: {temperatura}°C")
            if temperatura_percepita is not None: print(f"  Temperatura Percepita: {temperatura_percepita}°C")
            if umidita is not None: print(f"  Umidità: {umidita}%")
            if descrizione_meteo and descrizione_meteo != "Non disponibile": print(f"  Condizioni: {descrizione_meteo.capitalize()}")
            if velocita_vento is not None: print(f"  Vento: {velocita_vento} m/s")
            print("--------------------------------------")

        else:
            # Errore dall'API (es. API key sbagliata, città non trovata, ecc.)
            print(f"Errore durante la richiesta API!")
            print(f"Codice di Stato: {risposta_api.status_code}")
            # Tentiamo di leggere il messaggio di errore JSON se disponibile
            try:
                errore_json = risposta_api.json()
                messaggio_errore = errore_json.get("message", risposta_api.text)
                print(f"Messaggio: {messaggio_errore}")
            except json.JSONDecodeError: # Se la risposta d'errore non è JSON
                print(f"Messaggio: {risposta_api.text}")
            if risposta_api.status_code == 404:
                print(f"Suggerimento: la città '{nome_citta_utente}' potrebbe non essere stata trovata o scritta male.")
            elif risposta_api.status_code == 401:
                print("Suggerimento: controlla la tua API key. Potrebbe essere errata o non ancora attiva.")

    except requests.exceptions.Timeout:
        print("Errore: la richiesta ha impiegato troppo tempo (Timeout). Riprova.")
    except requests.exceptions.ConnectionError: # Più specifico per errori di connessione
            print("Errore di connessione. Controlla la tua connessione internet e riprova.")
    except requests.exceptions.RequestException as e: # Per altri errori della libreria requests
            print(f"Errore durante la richiesta API: {e}")
    except Exception as e: # Per altri errori imprevisti
        print(f"Si è verificato un errore imprevisto: {e}")

# Questa riga viene eseguita solo dopo che il ciclo 'while' è terminato (con 'break')
print("\nGrazie per aver usato il programma Meteo! Arrivederci.")