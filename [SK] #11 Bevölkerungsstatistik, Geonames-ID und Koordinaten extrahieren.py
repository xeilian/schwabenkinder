#11 | GEONAMES-ID UND KOORDINATEN EXTRAHIEREN (FÜR BEVÖLKERUNGSSTATISTIK)
#Voraussetzung: Excel-Tabelle mit mind. einer Spalte mit Gemeindenamen --> Code legt ID und Koordinaten in G ab

import pandas as pd
import requests

# Lese die Excel-Datei
data = pd.read_excel(r"C:\Users\quqiu\PycharmProjects\schwabenkinder\schwabenkinder_bevölkerungsstatistik_1880.xlsx", sheet_name='Bevölkerungsstatistik 1880')

# Funktion zum Abfragen der Geonames API
def query_geonames_api(place):
    endpoint = 'http://api.geonames.org/searchJSON'
    api_key = 'power'

    # API-Anfrage senden
    params = {
        "q": place,
        "country": "AT",
        "maxRows": 1,
        "featureCode": "ADM3",
        "username": api_key
    }

    print(place)
    response = requests.get(endpoint, params=params)
    print(f'API-Anfrage für {place} gesendet')

    # Ergebnis verarbeiten
    if response.status_code == 200:
        data = response.json()
        if 'geonames' in data and len(data['geonames']) > 0:
            result = data['geonames'][0]
            return {
                'geonameId': result.get('geonameId', ''),
                'lat': result.get('lat', ''),
                'lon': result.get('lng', '')
            }

    return None


# Schleife über die Datensätze in der Excel-Datei
for index, row in data.iterrows():
    place = row.iloc[2]  # Verwende Spalte C

    # Überprüfen, ob alle benötigten Informationen vorhanden sind
    if pd.notnull(place):
        result = query_geonames_api(place)
        print(result)

        if result is not None:
            # Ergebnisse in die Excel-Datei eintragen
            data.loc[index, "Spalte G"] = str(result)

# Ergebnisse in eine neue Excel-Datei schreiben
data.to_excel(r"C:\Users\quqiu\PycharmProjects\schwabenkinder\schwabenkinder_bevölkerungsstatistik_1880.xlsx", sheet_name="Bevölkerungsstatistik 1880", index=False)
print('Vorgang abgeschlossen.')