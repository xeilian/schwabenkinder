# Die Sozialtopographie der Schwabenkinder: Eine GIS-gestützte Untersuchung jugendlicher Arbeitsmigration aus Vorarlberg und Tirol nach Oberschwaben 1812-1938

*For an English version, see [here](https://github.com/xeilian/schwabenkinder/blob/main/README_en.md)*


## Inhaltsverzeichnis

* **[1. Ziel des Projekts](#1-ziel-des-projekts)**
* **[2. Dokumentation der Daten im Repository](#2-dokumentation-der-daten-im-repository)**
  * [2.1. Auswertung der Schwabenkinder-Datenbank](#21-auswertung-der-schwabenkinder-datenbank)
    * *[2.1.1. Übersicht über die Tabellen](#211-übersicht-über-die-tabellen)*
    * *[2.1.2. Übersicht über die Felder der Haupttabelle](#212-übersicht-über-die-felder-der-haupttabelle)*
  * [2.2. Übersicht über die anderen Auswertungen](#22-übersicht-über-die-anderen-auswertungen)
  * [2.3. Übersicht über die Grafiken](#23-übersicht-über-die-grafiken)
  * [2.4. Übersicht über die Karten, Polygone, Tracks und QGIS-Layer](#24-übersicht-über-die-karten-polygone-tracks-und-qgis-layer)
    * *[2.4.1. Polygone, Tracks und QGIS-Layer](#241-polygone-tracks-und-qgis-layer)*
    * *[2.4.2. Übersicht über die Karten](#242-übersicht-über-die-karten)*
  * [2.5. Übersicht über die Python-Scripte](#25-übersicht-über-die-python-scripte)


## 1. Ziel des Projekts

Die Freizeitillustrierte 'Die Gartenlaube' berichtete in einer Ausgabe von 1866 von einer seltsamen Begebenheit, die sich in einem Wirtshaus irgendwo zwischen Lindau und Bregenz ereignet hatte: *“Da saß eine Schaar rothwangiger Knaben und Mädchen in allen Altersclassen, vom siebenten bis zum fünfzehnten Lebensjahre, still ein Jedes in sich gekehrt [...]”* [^fn1] Die Kinder wurden anschließend in Ravensburg dem Hütekindermarkt zugeführt, wo sie unter den kritischen Augen der schwäbischen Bauern und Bäuerinnen auf ihre Leistungsfähigkeit überprüft und in ihre Dienste aufgenommen wurden. *“Es ist eben ein Stück Sclavenhandel, man mag sich abmühen, wie man will, die häßliche Sache mit milderem Auge zu betrachten.”*[^fn1] Szenen wie jene aus dem Jahr 1866 waren vor einem Jahrhundert Alltag im mittleren Alpenraum: stets im März verließen Kinder zwischen sieben und fünfzehn Jahren ihre Heimat in Österreich, Liechtenstein und der Schweiz, um in Süddeutschland landwirtschaftliche Arbeiten zu verrichten.

Genau jenes Phänomen, welches seit dem 17. Jahrhundert schriftlich belegt ist, habe ich Ende 2023 im Rahmen meiner Bachelorarbeit an der Universität Heidelberg bearbeitet. Das Herzstück der Arbeit war die erstmalige vollständige Auswertung der Schwabenkinder-Datenbank, die zwischen 2008 und 2012 durch den Zusammenschluss von Museen und Stadtarchive aus fünf Ländern im Rahmen des EU-Interreg IV-Projekts entstand. Jene Datenbank enthält 7.040 Schwabengänge von insgesamt 5.425 Kindern in einem Zeitraum von 1697 bis 1938, wobei solche zwischen den Jahren 1860 und 1920 über 85% der Datensätze ausmachen. Bei der Lektüre eines beliebigen Datensatzes erfährt man neben biographischen Details wie Name, Geschlecht, Diensteintrittsalter, Herkunftsort und -region auch Informationen zu den Arbeitseinsätzen in Oberschwaben. Dazu gehören Angaben über den Dienstbeginn bzw. -ende, den Einsatzort mit der dazugehörigen Gemeinde, den Namen des Dienstherrn und die Dienstbezeichnung. Zusätzlich sind teils Auskünfte über den Start und das Ende der Schulbefreiung enthalten[^fn2].

Sämtliche Geodaten zu Herkunfts- und Arbeitsorten sind jedoch nur in Textform enthalten, was eine Auswertung mittels Geoinformationssystemen (GIS) unmöglich macht. Um jedoch die geographische Verteilung sowie die kumulative Häufigkeit dessen in gewissen Regionen deutlich zu machen, wurden sämtliche Orte georeferenziert. Mithilfe methodischer Erkenntnisse der spatial history und der Geschichte von unten wurden in der Arbeit die Ergebnisse dieser Auswertung präsentiert und kritisch mit der Hinzunahme von vorhandenem Quellenmaterial und wissenschaftlichen Auswertungen eingeordnet. Mittels wirtschaftlicher, demographischer und topographischer Erkenntnisse wurden des Weiteren die Push- und Pullfaktoren der geographischen Verteilung offengelegt, die zu den Migrationsbewegungen geführt haben. Auch wird beleuchtet, wie die Kinder überhaupt von ihren Herkunfts- zu ihren Dienstorten gelangten. Aus diesen Erkenntnissen entstand am Ende eine Sozialtopographie, die das Schwabenkinderwesen auf systemischer Ebene erfasste.

Obwohl auch Daten zur Schweiz und Liechtenstein vorliegen, hat sich diese Arbeit auf Vorarlberg und Tirol fokussiert. Tirol wird dabei in seiner ursprünglichen historischen Form begriffen, das aus dem heutigen österreichischen Bundesland Tirol (Nord- und Osttirol) sowie der heutigen italienischen autonomen Region Trentino-Alto Adige (Südtirol und Trentino/Welschtirol) besteht. Da die Idee eines souveränen Südtirol erst in den 1920er-Jahren entstanden ist und von dort viele Schwabenkinder stammten, wird auch die Gegend südlich des Brenner beleuchtet. Das Ziel dieser Migration wird auf die Region Oberschwaben im heutigen Baden-Württemberg beschränkt. Auswanderungen nach Bayern wurden nicht in der Datenbank erfasst. Der Untersuchungszeitraum wird auf die Jahre von 1812 bis 1938 festgesetzt, was den ersten und letzten Eintrag der Datenbank widerspiegelt. Es gab zwar bereits vor 1812 eine lange Tradition dieser Art der Migration, jedoch ist die Quellenlage bis ins 19. Jahrhundert äußerst lückenhaft.


## 2. Dokumentation der Daten im Repository

Dieses Github-Repository enthält sämtliche Daten, die in dieser Arbeit erstellt wurden. Dieses Datenmaterial reicht von Datenauswertungen in Excel-Tabellen, allen mit QGIS erstellten Karten samt aller Polygone, Tracks und gpkg-Dateien. Auch sind sowohl die in der Arbeit verwendeten Grafiken, die die Datenauswertungen visualisieren, als auch alle Python-Scripte vorhanden, die für diese Arbeit erstellt wurden. Diese Dokumentation soll einen Überblick über die hier veröffentlichten Daten schaffen, damit diese, unter entsprechendem Nachweis, nachgenutzt werden können.

### 2.1. Auswertung der Schwabenkinder-Datenbank

Die Schwabenkinder-Datenbank ist als Excel-Tabelle unter dem Namen ***[schwabenkinder_datenbank_v3.xlsx](https://github.com/xeilian/schwabenkinder/blob/main/%23schwabenkinder_datenbank_v3.xlsx)*** herunterladbar. Diese enthält alle, über die [offizielle Seite](https://www.schwabenkinder.eu) des Interreg-Projektes abrufbaren Datensätze.

#### 2.1.1. Übersicht über die Tabellen

Die Datenbank enthält fünf Tabellen, die über ein komplexes Netz aus Formeln miteinander verbunden sind:
* *#Schwabenkinder-Datenbank* enthält Daten zu allen 7.040 Arbeitseinsätzen. Dies ist die Haupttabelle, die alle Daten enthält und auf die die anderen Tabellen referenzieren. Diese ist besonders für die Auswertung der Arbeitsorte von Nutzen.
* *Kinder* enthält die Liste aller Kinder, um die Gewichtung der Herkunftsorte bestimmen zu können. Durch Herausnahme mehrfacher Arbeitseinsätze eines Kindes, bleiben hier 5.425 eindeutige Einträge zu Kindern übrig
* *Herkunftsorte* listet die Anzahl der Herkunftsorte pro Kind und Dienst auf und enthält zusätzlich alle in der Haupttabelle gespeicherten Ortsinformationen.
* *Arbeitsorte (nach Gemeinden)* listet die Anzahl der Arbeitsorte pro Dienst (zusätzlich aufgeteilt auf alle Herkunftsregionen) auf. Diese Auswertung geht nach den damaligen Gemeinden in Oberschwaben und übernimmt alle Ortsinformationen aus der Haupttabelle.
* *Arbeitsorte (nach Orten)* macht das gleiche wie oben, nur wird hier die Anzahl der Arbeitsorte nach den einzelnen Gemeindebestandteilen (also Orten) ausgewertet.

#### 2.1.2. Übersicht über die Felder der Haupttabelle

| Spalte(n) | Feldname | Beschreibung |
| -------- | -------- | -------- |
| A | Kind-ID | die ID des Kindes, extrahiert durch die Nummer des Datensatzes auf der Webseite |
| B | Arbeit-ID | die ID des Arbeitseinsatzes, im CSV-Download der Webseite enthalten |
| C | Nachname | Vorname des Kindes |
| D | Vorname | Nachname des Kindes |
| E | Herkunft: Ort | Name des Herkunftsortes des Kindes |
| F | Herkunft: Region | Moderne Region des Herkunftsortes (z.B. Bundesland oder Kanton) |
| G | Herkunft: Ort (G-ID) | Geonames-ID des Herkunftsortes |
| H | Herkunft: Ort (Lat.) | Längengrad des Herkunftsortes |
| I | Herkunft: Ort (Lon.) | Breitengrad des Herkunftsortes |
| J | Herkunft: Gem. heute | Heutige Gemeinde des Herkunftsortes |
| K | Herkunft: Gem. heute (G-ID) | Geonames-ID der heutigen Gemeinde |
| L | Herkunft: Gem. heute (Lat.) | Längengrad der heutigen Gemeinde |
| M | Herkunft: Gem. heute (Lon.) | Breitengrad der heutigen Gemeinde |
| N | Herkunft: Bevölkerung 1880 (nur T/VB) | Bevölkerung des Herkunftsortes im Jahr 1880 (nur für Vorarlberg, heutiges Tirol und Südtirol) |
| O/P | Herkunft: Lat./Lon. Visualisierung | Es wurde nach Gemeinden ausgewertet. Da die Koordinaten der Gemeinden Mittelpunkte darstellen, wurden zur besseren Visualisierung die Koordinaten des Hauptortes verwendet. |
| Q | Herkunft: Kreis/Bezirk/Bezirksgemeinschaft | heutiger Kreis, Bezirk oder Bezirksgemeinschaft der Gemeinde |
| R | Tal | Tal des Herkunftsortes (nur für Vorarlberg und Tirol) |
| S | Herkunft: Kreis (G-ID) | Geonames-ID des heutigen Kreises et.al. |
| T | Herkunft: Kreis (Lat.) | Längengrad des heutigen Kreises et.al. |
| U | Herkunft: Kreis (Lon.) | Breitengrad des heutigen Kreises et.al. |
| V | Herkunft: Ort (Alternativ) | Alternativname des Herkunftsortes |
| W | Geschlecht | (angenommenes) Geschlecht des Kindes |
| X | Geburtsort | Geburtsort des Kindes (falls unterschiedlich zum Herkunftsort) |
| Y | Geburtsdatum | Geburtsdatum des Kindes |
| Z | Geburtsjahr | Geburtsjahr des Kindes (zur besseren Auswertung) |
| AA | Arbeit: Alter bei Beginn | Alter des Kindes bei dem jeweiligen Arbeitseinsatz |
| AB | Todestag | Todestag des Kindes |
| AC | Arbeit: Schulbefreiung Start | Beginn der Schulbefreiung für den Arbeitseinsatz |
| AD | Arbeit: Schulbefreiung Ende | Ende der Schulbefreiung für den Arbeitseinsatz |
| AE | Arbeit: Beruf (raw) | Art der Arbeit, wie ursprünglich in der Datenbank angegeben |
| AF | Arbeit: Beruf | Art der Arbeit nach eigener Kategorisierung |
| AG | Arbeit: Dienstantritt Jahr | Jahr des Dienstantritts des Arbeitseinsatzes |
| AH | Arbeit: Dienstantritt | Datum des Dienstantritts des Arbeitseinsatzes |
| AI | Arbeit: Dienstende Jahr | Jahr des Dienstendes des Arbeitseinsatzes |
| AJ | Arbeit: Dienstende | Datum des Dienstendes des Arbeitseinsatzes |
| AK | Arbeit: Dienstherr | Name des Dienstherrn |
| AL | Arbeit: Ort | Name des Arbeitsortes |
| AM | Arbeit: Gem. alt | Gemeinde des Arbeitsortes vor der Gemeindereform 1972/73 |
| AN | Arbeit: Gem. alt (Lat.) | Längengrad der damaligen Gemeinde |
| AO | Arbeit: Gem. alt (Lon.) | Breitengrad der damaligen Gemeinde |
| AP | Arbeit: Verwaltungseinheit alt | Alte Verwaltungseinheit des Arbeitsortes (bspw. Oberämter im Kngr. Württemberg) |
| AQ | Arbeit: Region alt | Region bzw. ehemaliger Staat des Arbeitsortes (bspw. Kngr. Württemberg) |
| AR | Arbeit: Gem. heute | Heutige Gemeinde des Arbeitsortes (nach der Gemeindereform 1972/73) |
| AS | Arbeit: Region | Heutige Region des Arbeitsortes (bspw. Baden-Württemberg) |
| AT | Arbeit: Gem. heute (G-ID) | Geonames-ID der heutigen Gemeinde |
| AU | Arbeit: Gem. heute (Lat.) | Längengrad der heutigen Gemeinde |
| AV | Arbeit: Gem. heute (Lon.) | Breitengrad der heutigen Gemeinde |
| AW | Arbeit: Kreis | Heutiger Kreis des Arbeitsortes |
| AX | Arbeit: Kreis (G-ID) | Geonames-ID des heutigen Kreises |
| AY | Arbeit: Kreis (Lat.) | Längengrad des heutigen Kreises |
| AZ | Arbeit: Kreis (Lon.) | Breitengrad des heutigen Kreises |
| BA | Arbeit: Ort (Alternativ) | Alternativname des Arbeitsortes |
| BB | Ehegatte Nachname | Vorname des Ehegatten |
| BC | Ehegatte Vorname | Nachname des Ehegatten |
| BD | Hochzeitstag | Hochzeitstag des Kindes |
| BE | Hochzeitsort | Hochzeitsort des Kindes |
| BF | Vater Name | Name des Vaters |
| BG | Vater Geburtstag | Geburtstag des Vaters |
| BH | Vater Beruf | Beruf des Vaters |
| BI | Mutter Name | Name der Mutter |
| BJ | Mutter Geburtstag | Geburtstag der Mutter |
| BK | Mutter Beruf | Beruf der Mutters |
| BL | Geschwister | Geschwister des Kindes |
| BM | Nachfahren | Nachfahren des Kindes |
| BN | Quellen Museum | Quellennachweis |
| BO | Kommentare öffentlich | Öffentlicher Kommentar der Datenbankersteller:innen |

### 2.2. Übersicht über die anderen Auswertungen

Neben der wohl wichtigsten Datei des Gits, der Auswertung der Schwabenkinder-Datenbank, werden im folgenden auch die anderen Auswertungen aufgelistet. Diese Dateien, die im Ordner ***[[GIS] Auswertungen](https://github.com/xeilian/schwabenkinder/tree/main/%5BGIS%5D%20Auswertungen)*** enthalten sind, werden nicht so detailreich dokumentiert, da es sich hierbei primär um Arbeitstabellen handelt, die nicht für eine Nachnutzung geeignet sind.
| Name der Datei | zur Nachnutzung geeignet? | Beschreibung |
| -- | -- | -- |
| schwabenkinder_anno_auswertung.xlsx | Nein | Hierbei handelt es sich um eine Arbeitstabelle für die Zeitungsauswertung, in der basierend auf Zeitungsberichten die Anzahl der Schwabenkinder pro Jahr notiert wurden. |
| schwabenkinder_bevölkerungsstatistik_1880.xlsx | Ja | Diese Tabelle enthält alle heutigen Gemeinden Tirol und Vorarlbergs, samt ihrer Regierungsbezirke, Gemeindecodes und der Bevölkerungszahlen der Jahre 1880 und 2001. Zusätzlich wurden Informationen zu Geoname-ID und Koordinaten übernommen. Zur Nachnutzung geeignet. |
| schwabenkinder_demographische_berechnungen_alt.xlsx | Nein | Arbeitstabelle zur Berechnung von Demographie, Bevölkerungsdichte, Geburtenrate sowie der Anzahl der Dörfer und Weiler pro Region (hier Vorarlberg, Oberinntal und Etschtal) |
| schwabenkinder_faessler_appenzell.xlsx | Ja | Auswertung von Innerrhoder Passregister in einer Studie von Floreana Fässler[^fn3]. Diese wurde als Vergleich der Daten der Datenbank verwendet. |
| schwabenkinder_pivot_grafiken.xlsx | Nein | Arbeitstabelle zur Erstellung von Grafiken über das Excel-interne Pivottool. | schwabenkinder_tagebuch_regina.xlsx | Nein | Arbeitstabelle zur Notiz der Orte in Regina Lamperts Autobiographie[^fn4]. Dadurch wurde anschließend eine eigene Karte erstellt. Die Tabelle enthält Daten zu Datum, Tageszeit, Art des Fortbewegungsmittel, den Orten sowie der Seitenangabe. |
| schwabenkinder_vergleiche.xlsx | Ja | Diese Datei enthält drei Auswertungen, die als Vergleiche von den Daten der Datenbank herbeigezogen wurden. Tabelle *VG Tirol, Uh. 1901-13* zeigt eine Auswertung von Otto Uhlig von Schuldispensen und Passregistern pro Herkunftsort für die Jahre 1901/04/05/09/13[^fn5]. Tabelle *VG Tirol, VB 1895* zeigt die Statistik des Tiroler Volksboten vom 25.04.1895, welche 220 Hütekindern zu den einzelnen Gemeinden Tirols zuordnete[^fn6]. Tabelle *VG VB, Uh. 1922-23* umfasst die Herkunftsorte von 161 Kindern aus den Jahren 1922 und 1923, die Uhlig mittels Schulakten ermittelte[^fn7]. |

Daneben gibt es in dem Ordner *CSV-Dateien* eine Reihe von CSV-Dateien, die die Daten der bereits genannten Auswertungen in ein Format konvertieren, das von QGIS gelesen werden kann. Ohne diese Karten hätte das Kartenmaterial dieser Arbeit nicht erstellt werden können.

### 2.3. Übersicht über die Grafiken

Die Grafiken, die für diese Arbeit erstellt wurden, sollen die Auswertungen der Daten aus der Datenbank anschaulich visualieren. Die Grafiken, die im Ordner ***[[GIS] Grafiken](https://github.com/xeilian/schwabenkinder/tree/main/%5BGIS%5D%20Grafiken)*** vorhanden sind, werden im folgenden in Gänze abgebildet. Beim Klicken auf eines der Bilder gelangt man auf den Speicherort, wo die Datei in höherer Auflösung betrachtet werden kann.

|  |  |  |
| -- | -- | -- |
| [![Grafik, Alter.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Alter.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Alter.png) <br> *Grafik, Alter* | [![Grafik, Alterspyramide.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Alterspyramide.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Alterspyramide.png) <br> *Grafik, Alterspyramide* | [![Grafik, Dienstbeginne und enden.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Dienstbeginne%20und%20enden.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Dienstbeginne%20und%20enden.png) <br> *Grafik, Dienstbeginne und enden* |
| [![Grafik, Dienste.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Dienste.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Dienste.png) <br> *Grafik, Dienste* | [![Grafik, Geschlecht.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Geschlecht.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Geschlecht.png) <br> *Grafik, Geschlecht* | [![Grafik, Hütekindermärkte.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20H%C3%BCtekinderm%C3%A4rkte.png?raw=true)](https://example.com/hütekindermärkte) <br> *Grafik, Hütekindermärkte* |
| [![Grafik, Zeitliche Verteilung.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Zeitliche%20Verteilung.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Zeitliche%20Verteilung.png) <br> *Grafik, Zeitliche Verteilung* | | |
| | | |

### 2.4. Übersicht über die Karten, Polygone, Tracks und QGIS-Layer

Da im Rahmen dieser Arbeit eine Datenbank mittels GIS-Methoden ausgewertet und visualiert wurde, lag es nahe, das Phänomen der Schwabenkinder auch mithilfe von Karten darzustellen. Für die Darstellung der Daten wurde das Open-Source-Programm [QGIS](https://www.qgis.org/) verwendet.

#### 2.4.1. Polygone, Tracks und QGIS-Layer

Um die in der CSV-Datei (s.o.) gespeicherten Auswertungen in übersichtlichen Karten darzustellen, braucht es Polygone und Tracks. Tracks sind Linien, während Polygone eine geographische Fläche darstellen. Ich brauchte eine Menge unterschiedlicher Polygone und Tracks, um meine Karten so zu gestalten, wie ich sie gerne haben möchte.

Tracks (wie etwa Täler und Bahnlinien) habe ich mithilfe des freien Tools [Overpass Turbo](https://overpass-turbo.eu/) extrahiert: Beispiel Arlbergbahn. Die Arlbergbahn hat in OpenStreetMap (OSM) die Relation 1623486. Diese kann herausgefunden werden, indem man die Bahnlinie in der Karte sucht und auf die rechte Maustaste klickt. Es öffnet sich ein kleines Menü, wo man dann auf “Objektabfrage” klicken muss. Es öffnet sich ein Seitenfenster, wo man die Bahn und anschließend ganz unten die Relation auswählen muss. Anschließend wurde mithilfe eines kurzen Skriptes in Overpass Turbo die Relation-ID in eine herunterladbare GPX-Datei umgewandelt. Manche Tracks (wie etwa Ländergrenzen) können in QGIS in Polygone umgewandelt werden. 

```
[out:xml][timeout:25];
// Relation ID 1623486
relation(1623486);
out meta;
>;
out skel qt;
```

Das Verzeichnis ***[[GIS] Tracks und Polygone](https://github.com/xeilian/schwabenkinder/tree/main/%5BGIS%5D%20Tracks%20und%20Polygone)*** enthält alle Tracks und Polygone, die für diese Arbeit benutzt wurden. Dies umfasst etwa Bahnstrecken aus Österreich und Deutschland, alle Herkunftsregionen (etwa Kantone, Landkreise, Ländergrenzen u.ä.) als auch die für die Arbeit benötigten Täler. 

Besonders historische Geodaten konnten jedoch nicht mittels Overpass Turbo extrahiert werden, da OSM schließlich nur aktuelle Daten besitzt. Hierfür mussten auf externe Shapefiles zurückgegriffen werden, etwa für die Verwaltungsbezirke und die historischen Staatsgrenzen im Deutschen Reich[^fn8]. Für die heutige Schweiz gilt ähnliches[^fn9].

Die fertigen Karten mit allen Auswertungen, Grenzen, Bahnlinien etc. wurden mit allen Einstellungen (etwa zu Textgrößen, Schriftarten etc.) in Geopackage-Dateien gespeichert. Diese erlauben eine sekundenschnelle Nachbildung der Karten in QGIS, da durch einen Import alle in der Datei hinterlegten Tracks, Polygone oder CSV-Dateien automatisch geöffnet werden. Dies erlaubt eine genauere Betrachtung der geographischen Verteilung der Orte, die eine statische Karte nicht erlaubt. Im Ordner ***[[GIS] QGIS-Layer](https://github.com/xeilian/schwabenkinder/tree/main/%5BGIS%5D%20QGIS-Layer)*** sind 12 .gpkg-Dateien vorhanden, die im folgenden aufgelistet werden sollen:

| Name der Datei | Beschreibung |
| -- | -- |
| layer_arbeit_bahnstrecken.gpkg | Die Bahnstrecken zu den Arbeitsorten |
| layer_arbeit_landkreis.gpkg | Geolayer der heutigen Landkreise der Arbeitsorte |
| layer_arbeit_regionen.gpkg | Geolayer der ehemaligen Staaten (mit Verwaltungseinheiten) der Arbeitsorte |
| layer_arbeitsorte.gpkg | Die Arbeitsorte nach damaligen Gemeinden, gewichtet nach der Zahl der Einsätze |
| layer_herkunft_bahnstrecken.gpkg | Die Bahnstrecken in den Herkunftsregionen |
| layer_herkunft_regionen_schweiz_fl.gpkg | Geolayer für die Schweiz und Liechtenstein |
| layer_herkunft_regionen_tirol_vorarlberg.gpkg | Geolayer für Tirol und Vorarlberg |
| layer_herkunft_täler.gpkg | Tracks der Täler und Polygone des Bregenzerwalds und Vinschgaus
| layer_herkunftsorte.gpkg | Die Herkunftsorte nach heutigen Gemeinden, gewichtet nach der Zahl der Kinder |
| layer_regina_jahr1.gpkg | Der Weg von Regina Lampert von Schnifis nach Berg im ersten Jahr |
| layer_vergleiche.gpkg | Die Vergleiche der Daten der Datenbank mit anderen Erhebungen (s.o.) |
| layer_wege.gpkg | Die Wege der Schwabenkinder von den Tirol/Vorlarlberg nach Oberschwaben mit den wichtigsten Orten und Pässen, als auch den Tälern |

#### 2.4.2. Übersicht über die Karten

| | | |
| -- | -- | -- |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit%2C%20Bahnlinien.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit,%20Bahnlinien.png?raw=true" alt="Arbeit, Bahnlinien" height="175"></a> <br> *Arbeit, Bahnlinien* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit%2C%20Landkreise.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit,%20Landkreise.png?raw=true" alt="Arbeit, Landkreise" height="175"></a> <br> *Arbeit, Landkreise* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit%2C%20Verkehrsaufkommen.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit,%20Verkehrsaufkommen.png?raw=true" alt="Arbeit, Verkehrsaufkommen" height="175"></a> <br> *Arbeit, Verkehrsaufkommen* |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeitsorte.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeitsorte.png?raw=true" alt="Arbeitsorte" height="175"></a> <br> *Arbeitsorte* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Grafik%2C%20Regina%20Lampert%2C%20Jahr%201.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Grafik,%20Regina%20Lampert,%20Jahr%201.png?raw=true" alt="Grafik, Regina Lampert, Jahr 1" height="175"></a> <br> *Grafik, Regina Lampert, Jahr 1* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Bahnlinien.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Bahnlinien.png?raw=true" alt="Herkunft, Bahnlinien" height="175"></a> <br> *Herkunft, Bahnlinien* |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Graub%C3%BCnden.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Graub%C3%BCnden.png?raw=true" alt="Herkunft, Graubünden" height="175"></a> <br> *Herkunft, Graubünden* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Nordtirol.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Nordtirol.png?raw=true" alt="Herkunft, Nordtirol" height="175"></a> <br> *Herkunft, Nordtirol* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20S%C3%BCdtirol.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20S%C3%BCdtirol.png?raw=true" alt="Herkunft, Südtirol" height="175"></a> <br> *Herkunft, Südtirol* |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20St.%20Gallen%2C%20Liechtenstein%20und%20Appenzell.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20St.%20Gallen,%20Liechtenstein%20und%20Appenzell.png?raw=true" alt="Herkunft, St. Gallen, Liecht., Appenzell" height="175"></a> <br> *Herkunft, St. Gallen, Liecht., Appenzell* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Trentino.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Trentino.png?raw=true" alt="Herkunft, Trentino" height="175"></a> <br> *Herkunft, Trentino* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Vorarlberg.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Vorarlberg.png?raw=true" alt="Herkunft, Vorarlberg" height="175"></a> <br> *Herkunft, Vorarlberg* |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Wege.jpg"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Wege.jpg?raw=true" alt="Herkunft, Wege" height="175"></a> <br> *Herkunft, Wege* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t%2C%20Tiroler%20Volksbote%201895.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t,%20Tiroler%20Volksbote%201895.png?raw=true" alt="Validität, Tiroler Volksbote 1895" height="175"></a> <br> *Validität, Tiroler Volksbote 1895* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t%2C%20Uhlig%20Tirol%201901-13.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t,%20Uhlig%20Tirol%201901-13.png?raw=true" alt="Validität, Uhlig Tirol 1901-13" height="175"></a> <br> *Validität, Uhlig Tirol 1901-13* |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t%2C%20Uhlig%20VB%201923.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t,%20Uhlig%20VB%201923.png?raw=true" alt="Validität, Uhlig VB 1923" height="175"></a> <br> *Validität, Uhlig VB 1923* |  |  |
| | | |

### 2.5. Übersicht über die Python-Scripte

Es folgen sämtliche Python-Scripte, die für diese Arbeit geschrieben wurden. Die Scripte, die sich im Ordner ***[[GIS] Python-Scripte](https://github.com/xeilian/schwabenkinder/tree/main/%5BGIS%5D%20Python-Scripte)*** sind historisch gewachsen. Es kann also nicht garantiert werden, dass diese beim ersten Ausführen funktionieren.

| Titel mit Link | Beschreibung |
| -- | -- |
| [[SK] #01 DB extrahieren und in XLSX kombinieren.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2301%20DB%20extrahieren%20und%20in%20XLSX%20kombinieren.py) | Dieses Script extrahiert die Datensätze aus der Original-Datenbank und kombiniert diese in eine Excel-Tabelle. |
| [[SK] #02 Geodaten aus Geonames extrahieren.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2302%20Geodaten%20aus%20Geonames%20extrahieren.py) | Dieses Script extrahiert Geodaten aus der Geonames-API. Der Input hierbei sind die Namen der Herkunfts- und Arbeitsorte. |
| [[SK] #03 Geonames-ID extrahieren [Erster Versuch].py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2303%20Geonames-ID%20extrahieren%20%5BErster%20Versuch%5D.py) | Dieses Script hat nicht die gewünschten Ergebnisse gezeigt, siehe Skript 6 und 7. Idee war es, die Geonames-ID via Geonames-API zu extrahieren. Der Input waren die Koordinaten. |
| [[SK] #04 Koordinaten extrahieren.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2304%20Koordinaten%20extrahieren.py) | Dieses Script soll die Koordinaten, die zu dem Zeitpunkt nicht extrahiert wurden, nachfügen. |
| [[SK] #05 Leere Zeilen auffüllen.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2305%20Leere%20Zeilen%20auff%C3%BCllen.py) | Dieses Script soll leere Zeilen im Excel-Dokument mit den fehlenden Daten nachfüllen. Leider hat dies in diesem Fall nicht funktioniert. |
| [[SK] #06 Geonames-ID extrahieren (für Herkunftsorte).py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2306%20Geonames-ID%20extrahieren%20(f%C3%BCr%20Herkunftsorte).py) | Dieses Script extrahiert die Geonames-ID für die Herkunftsorte via Geonames-API. Input sind der Ort, das Land und der ADM-Code in Geonames. |
| [[SK] #07 Geonames-ID extrahieren (für Arbeitsorte).py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2307%20Geonames-ID%20extrahieren%20(f%C3%BCr%20Arbeitsorte).py) | Das gleiche Vorgehen wie in Script 7, aber für die Arbeitsorte. |
| [[SK] #08 Wahrheitstest für Ortschaften.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2308%20Wahrheitstest%20f%C3%BCr%20Ortschaften.py) | Dieses Script prüft nach, ob die Geonames die Orte auch mit den Ortsnamen findet. Es gab bis dahin ein Problem, dass das Script stattdessen die administrativen Geonames-Einträge übernommen hat. Anschließend können Einträge solche mit den oberen Script wieder befüllt werden. |
| [[SK] #09 ADM-Daten extrahieren.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2309%20ADM-Daten%20extrahieren.py) | Dieses Script extrahiert sämtliche administrativen Informationen eines Ortes mit der Geonames-ID. Dies enthält Daten zu Land, Bundesland/Kanton, Regionen, Kreisen und Gemeinden. |
| [[SK] #10 Bevölkerungsstatistik, Geonames-ID und Koordinaten extrahieren.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2310%20Bev%C3%B6lkerungsstatistik%2C%20Geonames-ID%20und%20Koordinaten%20extrahieren.py) | Dieses Script extrahiert Geonames-ID und Koordinaten für die Bevölkerungsstatistik 1880 (siehe: Datei *schwabenkinder_bevölkerungsstatistik_1880.xlsx*). Mittels XVERWEIS-Funktion in Excel kann die Haupttabelle mit den Bevölkerungsdaten ergänzt. |

### 2.6. Sonstiges

#### 2.6.1. Zeitungsartikel

Das Repository enthält auch alle Zeitungsartikel, die in dieser Arbeit verwendet wurden. Diese wurden über die das Zeitungsportal ANNO der Österreichischen Nationalbank heruntergeladen[^fn10] und sind im Ordner ***[Zeitungsartikel](https://github.com/xeilian/schwabenkinder/tree/main/Zeitungsartikel)*** als JPGs abrufbar. Die Daten haben das Format *[Zeitungskürzel] Jahr-Monat-Tag, Seite*. Im folgenden befindet sich der Schlüssel der Zeitungskürzel:
| Zeitungskürzel | Name der Zeitung |
| -- | -- |
| BTV | Bote für Tirol und Vorarlberg |
| DP | Die Presse |
| IN | Innsbrucker Nachrichten |
| RZ | Ravensburger Zeitung |
| STW | Schwäbische Tagwacht |
| TS | Tiroler Stimmen |
| TVB | Tiroler Volksbote |
| VLZ | Vorarlberger Landezeitung |
| VT | Vorarlberger/Bregenzer Tagblatt |
| VV | Vorarlberger Volksblatt |
| WZ | Wiener Zeitung |

#### 2.6.2. Archiv

Unter ***[Archiv]*** befinden sich alle restlichen Arbeitstabellen sowie Ideen, die nicht umgesetzt werden können. 

* im Hauptverzeichnis:
  * *[SK] GPX-Dateien aus Komoot.zip:* Dieses ZIP enthält die GPX-Dateien, die als Teil des damaligen Interreg-Projektes auf Komoot veröffentlicht wurden.
  * *[SK] Rohdaten aus DB.zip:* Dieses ZIP enthält alle Einzel-CSV-Dateien, wie sie mit Script 1 von der Datenbank extrahiert wurden.
* Ordner 'Excel-Tabellen'
  * *schwabenkinder_datenbank_v0_raw.xls:* Das ist die Rohdatenbank, die sie von dem Script aus einen Einzelteilen zusammengesetzt wurde.
  * *schwabenkinder_datenbank_v1/v2.xlsx:* Zwei Zwischenzustände der Datenbank. Beide wurden zur Datensicherung angelegt.
  * *schwabenkinder_doc_admex[...].xlsx:* Diese Dateien sind Arbeitstabellen, die für die Extraktion von den administrativen Einträgen erstellt wurden.
  * *schwabenkinder_geonames[...].xlsx:* Dies sind auch Arbeitstabellen, die für die Extraktion der ursprünglichen Daten aus Geonames erstellt wurden.
  * *schwabenkinder_gephi[...].xlsx/.csv*: Abgebrochene Versuche mit Gephi, einem Datenanalyse-Tool. Leider waren die Ergebnisse aus Gephi nicht aussagekräftig und vor allen Dingen konfus.
* Ordner 'Kartenmaterial': Dieser Ordner enthält ursprüngliches Kartenmaterial, das durch QGIS-Layer ersetzt wurde.
* Ordner 'Versuche mit Mapbox': Wie der Name sagt, enthält der Ordner Dateien, die für die Visualisierung in Mapbox erstellt wurden. Leider musste dieses Projekt aus Zeitgründen (vorerst) fallen gelassen werden.


[^fn1]: [o.A.]: Ein Kinderhandel, in: Die Gartenlaube 4 (1866), S. 55. https://de.wikisource.org/wiki/Ein_Kinderhandel.

[^fn2]: Bauernhaus-Museum Wolfegg (Hrsg.): Die Schwabenkinder Datenbank, online: Schwabenkinder.eu, https://www.schwabenkinder.eu/de/Datenbank/datenbank-suche/ [22.11.2023].

[^fn3]: Fässler, Floreana: Appenzeller Schwabenkinder?, in: Innerrhoder Geschichtsfreund 1 (2013), S. 83–111.

[^fn4]: Lampert, Regina: Die Schwabengängerin. Erinnerungen einer jungen Magd aus Vorarlberg 1864-1874, Zürich 2022.

[^fn5]: Uhlig, Otto: Die Schwabenkinder aus Tirol und Vorarlberg (Tiroler Wirtschaftsstudien, Bd. 34), Innsbruck/Stuttgart 1983, S. 216/218.

[^fn6]:  [o.A.]: Der Hütkinderverein, in: Tiroler Volksbote (25.04.1895), S. 4; auch gefunden in: [o.A.]: Die Fahrt der Hütkinder und jugendlichen Arbeiter ins Schwabenland, in: Tiroler Stimmen (23.04.1895), S. 8.

[^fn7]: Uhlig, Schwabenkinder, S. 346.

[^fn8]: Historical GIS datafiles, online: Censusmosaic, https://censusmosaic.demog.berkeley.edu/data/historical-gis-files [12.12.2023].

[^fn9]: swissBOUNDARIES3D, online: Bundesamt für Landestopographie der Schweiz, https://swisstopo.admin.ch/de/geodata/landscape/boundaries3d.html [22.12.2023].

[^fn10]: ANNO Historische Zeitungen und Zeitschriften, online: Österreichische Nationalbibliothek, https://anno.onb.ac.at/ [05.11.2023].
