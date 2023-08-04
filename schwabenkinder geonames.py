import pandas as pd
import requests

# Lese die Excel-Datei
data = pd.read_excel("D:\schwabenkinder\schwabenkinder_geonames_filled.xls", sheet_name='Tabelle2')
print(data.columns)

# Variablen für die Anzahl der API-Anfragen und Auffüllungen
api_requests = 0
fill_count = 0

# Liste für bereits abgefragte Orte
queried_places = []

# Funktion zum Abfragen der Geonames API
def query_geonames_api(place):

    # Überprüfen, ob Ort bereits abgefragt wurde
    if place in queried_places:
        print(f'API-Anfrage für {place} übersprungen (bereits abgefragt)')
        return None

    endpoint = 'http://api.geonames.org/searchJSON'
    api_key = 'xeilian'

    # API-Anfrage senden
    anfrage = endpoint + "?q=" + place + "&MaxRows=1&featureClass=P&username=" + api_key
    print(anfrage)
    response = requests.get(anfrage)
    print(f'API-Anfrage für {place} gesendet')

    # Ergebnis verarbeiten
    if response.status_code == 200:
        data = response.json()
        if 'geonames' in data and len(data['geonames']) > 0:
            result = data['geonames'][0]
            return {
                'adminname1': result.get('adminName1', ''),
                'lat': result.get('lat', ''),
                'lng': result.get('lng', ''),
                'population': result.get('population', ''),
                'toponym_name': result.get('toponymName', '')
            }

    return None

# Schleife über die Datensätze in der Excel-Datei
for index, row in data.iterrows():
    place1 = row[0]  # Verwende Spalte B
    #place2 = row[2]  # Verwende Spalte C

    # Überprüfen, ob Ort 1 bereits abgefragt wurde
    if pd.notnull(place1) and pd.isnull(row[3]):  # Überprüfe Spalte D
        result1 = query_geonames_api(place1)
        api_requests += 1

        if result1 is not None:
            # Ergebnisse in die Excel-Datei eintragen
            data.at[index, 'Spalte D'] = result1['adminname1']  # Spalte D
            data.at[index, 'Spalte E'] = result1['lat']  # Spalte E
            data.at[index, 'Spalte F'] = result1['lng']  # Spalte F
            data.at[index, 'Spalte G'] = result1['population']  # Spalte G
            data.at[index, 'Spalte H'] = result1['toponym_name']  # Spalte H
            fill_count += 1
            print(f'Auffüllung für {place1} abgeschlossen')
            print(f'Auffüllungen: {fill_count} / API-Abfragen: {api_requests}')

            # Ort zur Liste der bereits abgefragten Orte hinzufügen
            queried_places.append(place1)

    # Überprüfen, ob Ort 2 bereits abgefragt wurde
    #if pd.notnull(place2) and pd.isnull(row[8]):  # Überprüfe Spalte I
        #result2 = query_geonames_api(place2)
        #api_requests += 1

        #if result2 is not None:
            # Ergebnisse in die Excel-Datei eintragen
            #data.at[index, 'Spalte I'] = result2['adminname1']  # Spalte I
            #data.at[index, 'Spalte J'] = result2['lat']  # Spalte J
            #data.at[index, 'Spalte K'] = result2['lng']  # Spalte K
            #data.at[index, 'Spalte L'] = result2['population']  # Spalte L
            #data.at[index, 'Spalte M'] = result2['toponym_name']  # Spalte M
            #fill_count += 1
            #print(f'Auffüllung für {place2} abgeschlossen')
            #print(f'Auffüllungen: {fill_count} / API-Abfragen: {api_requests}')

            # Ort zur Liste der bereits abgefragten Orte hinzufügen
            #queried_places.append(place2)

# Ergebnisse in eine neue Excel-Datei schreiben
data.to_excel('D:\schwabenkinder\Mappe6-2.xlsx', index=False)
print('Vorgang abgeschlossen.')
