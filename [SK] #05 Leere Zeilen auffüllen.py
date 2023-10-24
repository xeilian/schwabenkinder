#05 | LEERE ZEILEN AUFFÜLLEN

import pandas as pd

# Pfad zur Excel-Datei
excel_file = 'D:\schwabenkinder\schwabenkinder_geonames_filled.xlsx'

# Lese die Excel-Datei
df = pd.read_excel(excel_file)

# Iteriere über die Zeilen des DataFrames
for index, row in df.iterrows():
    ort1 = row['ort1']
    ort2 = row['ort2']

    # Überprüfe, ob Ort1 bereits in den vorherigen Zeilen vorkam
    if ort1 in df.loc[:index - 1, 'ort1'].values:
        # Hole die gespeicherten Daten für Ort1
        gespeicherte_daten_ort1 = df.loc[df['ort1'] == ort1, 'Spalte D':'Spalte H'].values[0]

        # Aktualisiere die leeren Zellen für Ort1 mit den gespeicherten Daten
        df.loc[(df['ort1'] == ort1) & (df['Spalte D'].isnull()), 'Spalte D':'Spalte H'] = gespeicherte_daten_ort1

    else:
        # Speichere die Daten für Ort1
        gespeicherte_daten_ort1 = row['Spalte D':'Spalte H'].values

    # Aktualisiere die gespeicherten Daten für Ort1
    df.loc[df['ort1'] == ort1, 'Spalte D':'Spalte H'] = gespeicherte_daten_ort1

    # Überprüfe, ob Ort2 bereits in den vorherigen Zeilen vorkam
    if ort2 in df.loc[:index - 1, 'ort2'].values:
        # Hole die gespeicherten Daten für Ort2
        gespeicherte_daten_ort2 = df.loc[df['ort2'] == ort2, 'Spalte I':'Spalte M'].values[0]

        # Aktualisiere die leeren Zellen für Ort2 mit den gespeicherten Daten
        df.loc[(df['ort2'] == ort2) & (df['Spalte I'].isnull()), 'Spalte I':'Spalte M'] = gespeicherte_daten_ort2

    else:
        # Speichere die Daten für Ort2
        gespeicherte_daten_ort2 = row['Spalte I':'Spalte M'].values

    # Aktualisiere die gespeicherten Daten für Ort2
    df.loc[df['ort2'] == ort2, 'Spalte I':'Spalte M'] = gespeicherte_daten_ort2

    # Gib den Fortschritt aus
    print(f"Fortschritt: {index+1}/{len(df)} Zeilen verarbeitet")

# Speichere das aktualisierte DataFrame zurück in die Excel-Datei
df.to_excel(excel_file, index=False)
