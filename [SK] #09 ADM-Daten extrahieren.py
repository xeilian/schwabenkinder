#09 | ADM-DATEN EXTRAHIEREN
#Voraussetzung: Excel-Tabelle mit zwei Spalten. A = DB-ID, B = Geoname-ID, --> Code legt die Daten ab Spalte C ab

import pandas as pd
import requests
import json

# Lese die Excel-Datei
data = pd.read_excel(f"D:\schwabenkinder\schwabenkinder_dok_admex_a.xlsx", sheet_name='Tabelle1')
endpoint = 'http://api.geonames.org/hierarchyJSON'
counter = 0
api_key_index = 0
api_keys = ['brain', 'world', 'six', 'power', 'cool', 'help', 'jackie', 'nice', 'mind', 'sing', 'dive', 'time', 'money', 'california', 'doggy', 'free', 'bird', 'radio', 'swift', 'brian', 'heavy', 'value', 'stop', 'happy', 'moin', 'light']

# Funktion zum Abfragen der Geonames API
def query_geonames_api(geoname_id):
        # API-Anfrage senden
    params = {
        "geonameId": geoname_id,
        "username": api_keys[api_key_index]
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
    geoname_id = row.iloc[5]  # Verwende Spalte F

    # Überprüfen, ob alle benötigten Informationen vorhanden sind
    if geoname_id is not None and not pd.isnull(geoname_id) and str(geoname_id).strip() != '':
        geoname_id = int(geoname_id)
        result = query_geonames_api(geoname_id)
        print(result)

        if result is not None:
            # Ergebnisse in die Excel-Datei eintragen
            for column_name in result.keys():
                data.loc[index, column_name] = json.dumps(result[column_name])
    else:
        pass

    counter += 1
    print(counter)

    if counter & 900 == 0:
        api_key_index = (api_key_index + 1) % len(api_keys)

# Ergebnisse in eine neue Excel-Datei schreiben
data.to_excel(f"D:\schwabenkinder\schwabenkinder_dok_admex_a.xlsx", sheet_name="Tabelle1", index=False)
print('Vorgang abgeschlossen.')