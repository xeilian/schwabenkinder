# 06 | GEONAMES-ID EXTRAHIEREN

import pandas as pd
import requests

# Lese die Excel-Datei
data = pd.read_excel(f"D:\schwabenkinder\schwabenkinder_dok_admex_a.xlsx", sheet_name='Tabelle1')

# Funktion zum Abfragen der Geonames API
def query_geonames_api(place, country, adm1):
    endpoint = 'http://api.geonames.org/searchJSON'
    api_key = 'code'

    # API-Anfrage senden
    params = {
        "q": place,
        "country": country,
        "adminCode1": adm1,
        "maxRows": 1,
        "username": api_key
    }

    print(place, country, adm1)
    response = requests.get(endpoint, params=params)
    print(f'API-Anfrage für {place} gesendet')

    # Ergebnis verarbeiten
    if response.status_code == 200:
        data = response.json()
        if 'geonames' in data and len(data['geonames']) > 0:
            result = data['geonames'][0]
            return {
                'geonameId': result.get('geonameId', ''),
            }

    return None


# Schleife über die Datensätze in der Excel-Datei
for index, row in data.iterrows():
    place = row[0]  # Verwende Spalte A
    country = row[1]  # Verwende Spalte B
    adm1 = (row[2])  # Verwende Spalte C

    # Überprüfen, ob alle benötigten Informationen vorhanden sind
    if pd.notnull(place) and pd.notnull(country) and pd.notnull(adm1):
        result = query_geonames_api(place, country, adm1)
        print(result)

        if result is not None:
            # Ergebnisse in die Excel-Datei eintragen
            data.loc[index, 'Spalte D'] = str(result)

# Ergebnisse in eine neue Excel-Datei schreiben
data.to_excel(f"D:\schwabenkinder\schwabenkinder_dok_admex_a.xlsx", sheet_name="Tabelle1", index=False)
print('Vorgang abgeschlossen.')