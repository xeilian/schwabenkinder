import openpyxl
import requests

# Lade die neue Excel-Datei
file_path = 'D:\schwabenkinder\kombinierte_daten - Kopie.xlsx'
workbook = openpyxl.load_workbook(file_path)
worksheet = workbook.active

# Definiere Spaltenbuchstaben
spalte_a = 'A'
spalte_b = 'B'
spalte_c = 'C'
spalte_d = 'D'

# Ermittle die Spaltennummern
spalte_b_num = openpyxl.utils.column_index_from_string(spalte_b)

# Gehe die Zeilen in Spalte B (Ort) durch
for index, row in enumerate(worksheet.iter_rows(min_row=2, values_only=True, min_col=spalte_b_num), start=2):
    ort = row[0]
    koordinaten = None
    geonames_link = None

    # Ort nicht leer, frage Geonames-API ab
    if ort:
        url = f'http://api.geonames.org/searchJSON?q={ort}&featureCode=PPL&country=DE&country=AT&country=LI&country=CH&maxRows=1&username=xeilian'
        response = requests.get(url)
        data = response.json()

        # Extrahiere Koordinaten und Geonames-Link aus der API-Antwort
        if 'geonames' in data and len(data['geonames']) > 0:
            place = data['geonames'][0]
            lat = place.get('lat', None)
            lon = place.get('lng', None)
            geoname_id = place.get('geonameId', None)
            geonames_link = f'http://www.geonames.org/{geoname_id}'
            koordinaten = f'{lat}, {lon}'

    # Speichere Koordinaten und Geonames-Link in der Excel-Datei
    worksheet[f'{spalte_c}{index}'] = koordinaten
    worksheet[f'{spalte_d}{index}'] = geonames_link

# Speichere die neue Excel-Datei
new_file_path = 'D:\schwabenkinder\kombinierte_daten - Kopie_neu.xlsx'
workbook.save(new_file_path)
