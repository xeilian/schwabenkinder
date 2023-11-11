#10 | FÜR MAPBOX: XLSX ZU GEOJSON KONVERTIEREN

import pandas as pd
import json

# Beispiel-Datenrahmen mit Ihren Datenüberschriften (ersetzen Sie diese durch Ihre eigenen Daten)
data = pd.read_excel('schwabenkinder_mapbox.xlsx')

# Entfernen Sie Leerzeichen aus den Spaltenüberschriften
data.columns = data.columns.str.replace(' ', '')

features = []
for index, row in data.iterrows():
    feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [float(row['lon1'].replace(',', '.')), float(row['lat1'].replace(',', '.'))]
        },
        'properties': {
            'ID': row['id'],
            'Region1': row['region1'],
            'Title1': row['title1'],
            'Year': row['year']
        }
    }
    features.append(feature)

    feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [float(row['lon2'].replace(',', '.')), float(row['lat2'].replace(',', '.'))]
        },
        'properties': {
            'ID': row['id'],
            'Region2': row['region2'],
            'Title2': row['title2'],
            'Year': row['year']
        }
    }
    features.append(feature)

feature_collection = {
    'type': 'FeatureCollection',
    'features': features
}

with open('schwabenkinder_mapbox.geojson', 'w') as outfile:
    json.dump(feature_collection, outfile)
