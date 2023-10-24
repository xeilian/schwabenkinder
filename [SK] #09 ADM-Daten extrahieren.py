#09 | ADM-DATEN EXTRAHIEREN
#Voraussetzung: Excel-Tabelle mit zwei Spalten. A = DB-ID, B = Geoname-ID, --> Code legt die Daten ab Spalte C ab

import pandas as pd
import requests
import json

# Lese die Excel-Datei
data = pd.read_excel(f"D:\schwabenkinder\schwabenkinder_dok_admex_a.xlsx", sheet_name='Tabelle1')

# Funktion zum Abfragen der Geonames API
def query_geonames_api(geoname_id):
    endpoint = 'http://api.geonames.org/hierarchyJSON'
    api_key = 'power'

    # API-Anfrage senden
    params = {
        "geonameId": geoname_id,
        "username": api_key
    }

    print(geoname_id)
    response = requests.get(endpoint, params=params)
    print(f'API-Anfrage für {geoname_id} gesendet')

    # Ergebnis verarbeiten
    if response.status_code == 200:
        data = response.json()
        results = {
            'name': [],
            'geonameId': [],
            'lat': [],
            'lng': []
        }

        for geoname in data.get('geonames', []):
            fcode = geoname.get('fcode')
            country_code = geoname.get('countryCode')

            if country_code == 'DE':
                if fcode in ['ADM3','ADM4']:
                    results['name'].append(geoname.get('name'))
                    results['geonameId'].append(geoname.get('geonameId'))
                    results['lat'].append(geoname.get('lat'))
                    results['lng'].append(geoname.get('lng'))
            else:
                if fcode in ['ADM2', 'ADM3']:
                    results['name'].append(geoname.get('name'))
                    results['geonameId'].append(geoname.get('geonameId'))
                    results['lat'].append(geoname.get('lat'))
                    results['lng'].append(geoname.get('lng'))
        return results
    return None

# Schleife über die Datensätze in der Excel-Datei
for index, row in data.iterrows():
    geoname_id = int(row.iloc[2])  # Verwende Spalte C

    # Überprüfen, ob alle benötigten Informationen vorhanden sind
    if pd.notnull(geoname_id):
        result = query_geonames_api(geoname_id)
        print(result)

        if result is not None:
            # Ergebnisse in die Excel-Datei eintragen
            for column_name in result.keys():
                data.loc[index, column_name] = json.dumps(result[column_name])

# Ergebnisse in eine neue Excel-Datei schreiben
data.to_excel(f"D:\schwabenkinder\schwabenkinder_dok_admex_a.xlsx", sheet_name="Tabelle1", index=False)
print('Vorgang abgeschlossen.')