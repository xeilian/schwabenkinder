#08 | WAHRHEITSTEST FÜR ORTSCHAFTEN
#Voraussetzung: Excel-Tabelle mit zwei Spalten. A = DB-ID, B = Geoname-ID, --> Code legt die Daten ab Spalte C ab

import pandas as pd
import requests
import json

# Lese die Excel-Datei
data = pd.read_excel(f"D:\schwabenkinder\schwabenkinder_dok_admex_bool.xlsx", sheet_name='Tabelle1')

# Funktion zum Abfragen der Geonames API
def query_geonames_api(geoname_id):
    endpoint = 'http://api.geonames.org/hierarchyJSON'
    api_key = 'xeilian'

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

        for geoname in data.get('geonames', []):
            fcl = geoname.get('fcl')

            if fcl == 'P':
                return 'P'
        return 'X'
    return 'False'

# Schleife über die Datensätze in der Excel-Datei
for index, row in data.iterrows():
    geoname_id = int(row.iloc[0])  # Verwende Spalte A

    # Überprüfen, ob alle benötigten Informationen vorhanden sind
    if pd.notnull(geoname_id):
        result = query_geonames_api(geoname_id)
        print(result)

        if result is not None:
            # Ergebnisse in die Excel-Datei eintragen
            data.loc[index, 'Spalte B'] = result

# Ergebnisse in eine neue Excel-Datei schreiben
data.to_excel(f"D:\schwabenkinder\schwabenkinder_dok_admex_bool.xlsx", sheet_name="Tabelle1", index=False)
print('Vorgang abgeschlossen.')