#07 | GEONAMES-ID EXTRAHIEREN (FÜR ARBEITSORTE)
#Voraussetzung: Excel-Tabelle mit drei Spalten. Name, Land, ADM-Code 1 --> Code legt ID via API in D ab

import pandas as pd
import requests

# Lese die Excel-Datei
data = pd.read_excel(f"D:\schwabenkinder\schwabenkinder_dok_admex_a.xlsx", sheet_name='Tabelle1')
endpoint = 'http://api.geonames.org/searchJSON'
counter = 0
api_key_index = 0
api_keys = ['xeilian', 'code', 'brain', 'world', 'six', 'power', 'cool', 'help', 'jackie', 'nice', 'mind', 'sing', 'dive', 'time', 'money', 'california', 'doggy', 'free', 'bird', 'radio', 'swift', 'brian', 'heavy', 'value', 'stop', 'happy', 'moin', 'light']

# Funktion zum Abfragen der Geonames API
def query_geonames_api(place, country, adm1):
    # API-Anfrage senden
    params = {
        "q": place,
        "country": country,
        "adminCode1": adm1,
        "maxRows": 1,
        "featureClass": "P",
        "username": api_keys[api_key_index]
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
                'lat': result.get('lat', ''),
                'lng': result.get('lng', '')
            }
    return None

# Schleife über die Datensätze in der Excel-Datei
for index, row in data.iterrows():
    place = row.iloc[2]
    country = row.iloc[3]
    test = row.iloc[5]

    if country == "AT" or country == "DE":
        adm1 = "0" + str(int(row.iloc[4]))
    elif country == "CH" or country == "IT" or country == "LI":
        adm1 = str(row.iloc[4])
    elif pd.isnull(country):
        pass
    elif pd.notnull(test):
        pass

    # Überprüfen, ob alle benötigten Informationen vorhanden sind
    if pd.notnull(place) and pd.notnull(country) and pd.notnull(adm1):
        result = query_geonames_api(place, country, adm1)
        print(result)

        if result is not None:
            # Ergebnisse in die Excel-Datei eintragen
           data.loc[index, 'Spalte F'] = str(result)

    counter += 1
    print(counter)

    if counter & 900 == 0:
        api_key_index = (api_key_index + 1) % len(api_keys)

# Ergebnisse in eine neue Excel-Datei schreiben
data.to_excel(f"D:\schwabenkinder\schwabenkinder_dok_admex_a.xlsx", sheet_name="Tabelle1", index=False)
print('Vorgang abgeschlossen.')