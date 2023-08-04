import requests
import os
import pandas as pd
from xlrd import open_workbook
from geonamescache import GeonamesCache

# Schritt 1: Herunterladen der XLS-Dateien
download_folder = "D:\schwabenkinder"
url_template = "https://www.schwabenkinder.eu/de/Datenbank/datenbank-suche/export/xls/{}"

num_files = 7000  # Anzahl der herunterzuladenden Dateien
#for i in range(1, num_files + 1):
    #url = url_template.format(i)
    #filename = os.path.join(download_folder, f"datei_{i}.xls")
    #response = requests.get(url)
    #if response.status_code == 200:
        #with open(filename, "wb") as file:
            #file.write(response.content)
        #print(f"Datei {i} heruntergeladen.")
    #else:
        #print(f"Fehler beim Herunterladen der Datei {i}.")

# Schritt 2: Kombinieren der Daten
# Ordnerpfad mit den XLS-Dateien
folder_path = "D:\schwabenkinder"

# Kombinierte Daten initialisieren
combined_data = pd.DataFrame()

# Durch alle Dateien im Ordner iterieren
for filename in os.listdir(folder_path):
    if filename.endswith(".xls") or filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)
        try:
            df = pd.read_excel(file_path)
            # Dateinamen als neue Spalte hinzufügen
            df.insert(0, "Dateiname", filename)
            combined_data = pd.concat([combined_data, df])
            print(f"Datei {filename} kombiniert.")
        except Exception as e:
            print(f"Fehler beim Kombinieren der Daten aus Datei {filename}: {str(e)}")

# Kombinierte Daten in eine neue Excel-Datei speichern
combined_data.to_excel("kombinierte_daten.xlsx", index=False)
print("Alle Daten kombiniert und in kombinierte_daten.xlsx gespeichert.")
