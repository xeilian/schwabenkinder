#03 | KOORDINATEN EXTRAHIEREN I

import requests
import pandas as pd

# Initialize an empty list to store the already used coordinates and IDs
verwendete_orte = []

# Read the Excel file
df = pd.read_excel('C:/Users/quqiu/Documents/koordinaten.xlsx')

# Iterate over each row in the dataframe
for index, row in df.iterrows():
    ort1_longitude = str(row['Spalte A']).replace(',', '.')
    ort1_latitude = str(row['Spalte B']).replace(',', '.')
    ort2_longitude = str(row['Spalte D']).replace(',', '.')
    ort2_latitude = str(row['Spalte E']).replace(',', '.')

    # Check if the coordinates have already been used
    if (ort1_longitude, ort1_latitude) in verwendete_orte:
        # Coordinates have already been used, retrieve the ID from the cache
        ort1_id = verwendete_orte[verwendete_orte.index((ort1_longitude, ort1_latitude))][2]
    else:
        # Coordinates have not been used, query the ID from the Geonames API
        url = f"http://api.geonames.org/findNearbyJSON?lat={ort1_latitude}&lng={ort1_longitude}&maxRows=1&username=xeilian"
        response = requests.get(url)
        try:
            response_json = response.json()
            if 'geonames' in response_json and len(response_json['geonames']) > 0:
                ort1_id = response_json['geonames'][0]['geonameId']
                verwendete_orte.append((ort1_longitude, ort1_latitude, ort1_id))
            else:
                print(f"Keine Ergebnisse gefunden für Ort 1: {ort1_longitude}, {ort1_latitude}")
                continue
        except requests.exceptions.JSONDecodeError as e:
            print(f"Fehler bei der Verarbeitung der API-Antwort für Ort 1: {e}")
            print(f"API-Antwort: {response.text}")

    # Check if the coordinates have already been used
    if (ort2_longitude, ort2_latitude) in verwendete_orte:
        # Coordinates have already been used, retrieve the ID from the cache
        ort2_id = verwendete_orte[verwendete_orte.index((ort2_longitude, ort2_latitude))][2]
    else:
        # Coordinates have not been used, query the ID from the Geonames API
        url = f"http://api.geonames.org/findNearbyJSON?lat={ort2_latitude}&lng={ort2_longitude}&username=xeilian"
        response = requests.get(url)
        try:
            response_json = response.json()
            if 'geonames' in response_json and len(response_json['geonames']) > 0:
                ort2_id = response_json['geonames'][0]['geonameId']
                verwendete_orte.append((ort2_longitude, ort2_latitude, ort2_id))
            else:
                print(f"Keine Ergebnisse gefunden für Ort 2: {ort2_longitude}, {ort2_latitude}")
                continue
        except requests.exceptions.JSONDecodeError as e:
            print(f"Fehler bei der Verarbeitung der API-Antwort für Ort 2: {e}")
            print(f"API-Antwort: {response.text}")

    # Update the IDs in the respective columns of the dataframe
    df.at[index, 'Spalte C'] = ort1_id
    df.at[index, 'Spalte F'] = ort2_id

    # Print a progress indicator
    print(f"Fortschritt: {index+1}/{len(df)}")

# Save the updated dataframe to the Excel file
df.to_excel('C:/Users/quqiu/Documents/koordinaten2.xlsx', index=False)
