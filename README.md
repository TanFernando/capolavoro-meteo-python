# Meteo App Semplice

Un'applicazione Python semplice che recupera e visualizza le condizioni meteorologiche attuali per una città specificata utilizzando l'API di OpenWeatherMap.

---

## Prerequisiti

Prima di iniziare, assicurati di avere installato:

* **Python 3.10.10** o versioni successive.

---

## Installazione

1.  **Clona il repository (o scarica i file):**
    ```bash
    git clone [https://github.com/TanFernando/capolavoro-meteo-python.git]
    cd capolavoro-meteo-python
    ```

2.  **Installa le dipendenze:**
    Assicurati di avere `pip` (il gestore di pacchetti di Python) aggiornato e installa la libreria `requests` necessaria per le chiamate API:
    ```bash
    python -m pip install requests
    ```

---

## Configurazione della Chiave API

Per far funzionare l'applicazione, è necessaria una chiave API valida da OpenWeatherMap.

1.  **Ottieni la tua chiave API:**
    * Registrati gratuitamente su [OpenWeatherMap](https://openweathermap.org/api) per ottenere la tua chiave API personale.

2.  **Crea il file di configurazione:**
    * Nella stessa cartella in cui si trova `meteo_app.py`, crea un nuovo file chiamato **`config.py`**.
    * **In alternativa**, puoi rinominare il file `config_example.py` (se presente nel repository) in `config.py`.

3.  **Inserisci la tua chiave API in `config.py`:**
    * Apri il file `config.py` e incolla la tua chiave API al suo interno, seguendo questo formato:

    ```python
    # config.py

    API_KEY = "LA_TUA_VERA_CHIAVE_API_DI_OPENWEATHERMAP_VA_QUI"
    ```
    * **Ricorda:** Non caricare mai il tuo file `config.py` su GitHub per motivi di sicurezza! La tua chiave API dovrebbe rimanere privata.

---

## Esecuzione dell'Applicazione

Dopo aver configurato la chiave API, puoi eseguire l'applicazione:

1.  **Apri il terminale** (o il prompt dei comandi) nella directory principale del progetto.
2.  **Esegui lo script Python:**
    ```bash
    python meteo_app.py
    ```
    Lo script ti chiederà di inserire il nome di una città.

---
