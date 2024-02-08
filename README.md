# Die Sozialtopographie der Schwabenkinder: Eine GIS-gestützte Untersuchung jugendlicher Arbeitsmigration aus Vorarlberg und Tirol nach Oberschwaben 1812-1938

*For an English version, see [here](https://github.com/xeilian/schwabenkinder/blob/main/README_en.md)*


## Ziel des Projekts

Die Freizeitillustrierte 'Die Gartenlaube' berichtete in einer Ausgabe von 1866 von einer seltsamen Begebenheit, die sich in einem Wirtshaus irgendwo zwischen Lindau und Bregenz ereignet hatte: *“Da saß eine Schaar rothwangiger Knaben und Mädchen in allen Altersclassen, vom siebenten bis zum fünfzehnten Lebensjahre, still ein Jedes in sich gekehrt [...]”* [^fn1] Die Kinder wurden anschließend in Ravensburg dem Hütekindermarkt zugeführt, wo sie unter den kritischen Augen der schwäbischen Bauern und Bäuerinnen auf ihre Leistungsfähigkeit überprüft und in ihre Dienste aufgenommen wurden. *“Es ist eben ein Stück Sclavenhandel, man mag sich abmühen, wie man will, die häßliche Sache mit milderem Auge zu betrachten.”*[^fn1] Szenen wie jene aus dem Jahr 1866 waren vor einem Jahrhundert Alltag im mittleren Alpenraum: stets im März verließen Kinder zwischen sieben und fünfzehn Jahren ihre Heimat in Österreich, Liechtenstein und der Schweiz, um in Süddeutschland landwirtschaftliche Arbeiten zu verrichten.

Genau jenes Phänomen, welches seit dem 17. Jahrhundert schriftlich belegt ist, habe ich Ende 2023 im Rahmen meiner Bachelorarbeit an der Universität Heidelberg bearbeitet. Das Herzstück der Arbeit war die erstmalige vollständige Auswertung der Schwabenkinder-Datenbank, die zwischen 2008 und 2012 durch den Zusammenschluss von Museen und Stadtarchive aus fünf Ländern im Rahmen des EU-Interreg IV-Projekts entstand. Jene Datenbank enthält 7.040 Schwabengänge von insgesamt 5.425 Kindern in einem Zeitraum von 1697 bis 1938, wobei solche zwischen den Jahren 1860 und 1920 über 85% der Datensätze ausmachen. Bei der Lektüre eines beliebigen Datensatzes erfährt man neben biographischen Details wie Name, Geschlecht, Diensteintrittsalter, Herkunftsort und -region auch Informationen zu den Arbeitseinsätzen in Oberschwaben. Dazu gehören Angaben über den Dienstbeginn bzw. -ende, den Einsatzort mit der dazugehörigen Gemeinde, den Namen des Dienstherrn und die Dienstbezeichnung. Zusätzlich sind teils Auskünfte über den Start und das Ende der Schulbefreiung enthalten[^fn2].

Sämtliche Geodaten zu Herkunfts- und Arbeitsorten sind jedoch nur in Textform enthalten, was eine Auswertung mittels Geoinformationssystemen (GIS) unmöglich macht. Um jedoch die geographische Verteilung sowie die kumulative Häufigkeit dessen in gewissen Regionen deutlich zu machen, wurden sämtliche Orte georeferenziert. Mithilfe methodischer Erkenntnisse der spatial history und der Geschichte von unten wurden in der Arbeit die Ergebnisse dieser Auswertung präsentiert und kritisch mit der Hinzunahme von vorhandenem Quellenmaterial und wissenschaftlichen Auswertungen eingeordnet. Mittels wirtschaftlicher, demographischer und topographischer Erkenntnisse wurden des Weiteren die Push- und Pullfaktoren der geographischen Verteilung offengelegt, die zu den Migrationsbewegungen geführt haben. Auch wird beleuchtet, wie die Kinder überhaupt von ihren Herkunfts- zu ihren Dienstorten gelangten. Aus diesen Erkenntnissen entstand am Ende eine Sozialtopographie, die das Schwabenkinderwesen auf systemischer Ebene erfasste.

Obwohl auch Daten zur Schweiz und Liechtenstein vorliegen, hat sich diese Arbeit auf Vorarlberg und Tirol fokussiert. Tirol wird dabei in seiner ursprünglichen historischen Form begriffen, das aus dem heutigen österreichischen Bundesland Tirol (Nord- und Osttirol) sowie der heutigen italienischen autonomen Region Trentino-Alto Adige (Südtirol und Trentino/Welschtirol) besteht. Da die Idee eines souveränen Südtirol erst in den 1920er-Jahren entstanden ist und von dort viele Schwabenkinder stammten, wird auch die Gegend südlich des Brenner beleuchtet. Das Ziel dieser Migration wird auf die Region Oberschwaben im heutigen Baden-Württemberg beschränkt. Auswanderungen nach Bayern wurden nicht in der Datenbank erfasst. Der Untersuchungszeitraum wird auf die Jahre von 1812 bis 1938 festgesetzt, was den ersten und letzten Eintrag der Datenbank widerspiegelt. Es gab zwar bereits vor 1812 eine lange Tradition dieser Art der Migration, jedoch ist die Quellenlage bis ins 19. Jahrhundert äußerst lückenhaft.


## Dokumentation der Daten im Repository

Dieses Github-Repository enthält sämtliche Daten, die in dieser Arbeit erstellt wurden. Dieses Datenmaterial reicht von Datenauswertungen in Excel-Tabellen, allen mit QGIS erstellten Karten samt aller Polygone, Tracks und gpkg-Dateien. Auch sind sowohl die in der Arbeit verwendeten Grafiken, die die Datenauswertungen visualisieren, als auch alle Python-Scripte vorhanden, die für diese Arbeit erstellt wurden. Diese Dokumentation soll einen Überblick über die hier veröffentlichten Daten schaffen, damit diese, unter entsprechendem Nachweis, nachgenutzt werden können.

### Auswertung der Schwabenkinder-Datenbank

Die Schwabenkinder-Datenbank ist als Excel-Tabelle unter dem Namen *schwabenkinder_datenbank_v3.xlsx* herunterladbar. Diese enthält alle, über die [offizielle Seite](https://www.schwabenkinder.eu) des Interreg-Projektes abrufbaren Datensätze.

#### Übersicht über die Tabellen

Die Datenbank enthält fünf Tabellen, die über ein komplexes Netz aus Formeln miteinander verbunden sind:
* *#Schwabenkinder-Datenbank* enthält Daten zu allen 7.040 Arbeitseinsätzen. Dies ist die Haupttabelle, die alle Daten enthält und auf die die anderen Tabellen referenzieren. Diese ist besonders für die Auswertung der Arbeitsorte von Nutzen.
* *Kinder* enthält die Liste aller Kinder, um die Gewichtung der Herkunftsorte bestimmen zu können. Durch Herausnahme mehrfacher Arbeitseinsätze eines Kindes, bleiben hier 5.425 eindeutige Einträge zu Kindern übrig
* *Herkunftsorte* listet die Anzahl der Herkunftsorte pro Kind und Dienst auf und enthält zusätzlich alle in der Haupttabelle gespeicherten Ortsinformationen.
* *Arbeitsorte (nach Gemeinden)* listet die Anzahl der Arbeitsorte pro Dienst (zusätzlich aufgeteilt auf alle Herkunftsregionen) auf. Diese Auswertung geht nach den damaligen Gemeinden in Oberschwaben und übernimmt alle Ortsinformationen aus der Haupttabelle.
* *Arbeitsorte (nach Orten)* macht das gleiche wie oben, nur wird hier die Anzahl der Arbeitsorte nach den einzelnen Gemeindebestandteilen (also Orten) ausgewertet.

#### Übersicht über die Felder der Haupttabelle

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

### Übersicht über die anderen Auswertungen

Neben der wohl wichtigsten Datei des Gits, der Auswertung der Schwabenkinder-Datenbank, werden im folgenden auch die anderen Auswertungen aufgelistet. Diese Dateien werden nicht so detailreich dokumentiert, da es sich hierbei primär um Arbeitstabellen handelt, die nicht für eine Nachnutzung geeignet sind.
| Name der Datei | zur Nachnutzung geeignet? | Beschreibung |
| -- | -- | -- |
| schwabenkinder_anno_auswertung.xlsx | Nein | Hierbei handelt es sich um eine Arbeitstabelle für die Zeitungsauswertung, in der basierend auf Zeitungsberichten die Anzahl der Schwabenkinder pro Jahr notiert wurden. |
| schwabenkinder_bevölkerungsstatistik_1880.xlsx | Ja | Diese Tabelle enthält alle heutigen Gemeinden Tirol und Vorarlbergs, samt ihrer Regierungsbezirke, Gemeindecodes und der Bevölkerungszahlen der Jahre 1880 und 2001. Zusätzlich wurden Informationen zu Geoname-ID und Koordinaten übernommen. Zur Nachnutzung geeignet. |
| schwabenkinder_demographische_berechnungen_alt.xlsx | Nein | Arbeitstabelle zur Berechnung von Demographie, Bevölkerungsdichte, Geburtenrate sowie der Anzahl der Dörfer und Weiler pro Region (hier Vorarlberg, Oberinntal und Etschtal) |
| schwabenkinder_faessler_appenzell.xlsx | Ja | Auswertung von Innerrhoder Passregister in einer Studie von Floreana Fässler[^fn3]. Diese wurde als Vergleich der Daten der Datenbank verwendet. |
| schwabenkinder_pivot_grafiken.xlsx | Nein | Arbeitstabelle zur Erstellung von Grafiken über das Excel-interne Pivottool. | schwabenkinder_tagebuch_regina.xlsx | Nein | Arbeitstabelle zur Notiz der Orte in Regina Lamperts Autobiographie[^fn4]. Dadurch wurde anschließend eine eigene Karte erstellt. Die Tabelle enthält Daten zu Datum, Tageszeit, Art des Fortbewegungsmittel, den Orten sowie der Seitenangabe. |
| schwabenkinder_vergleiche.xlsx | Ja | Diese Datei enthält drei Auswertungen, die als Vergleiche von den Daten der Datenbank herbeigezogen wurden. Tabelle *VG Tirol, Uh. 1901-13* zeigt eine Auswertung von Otto Uhlig von Schuldispensen und Passregistern pro Herkunftsort für die Jahre 1901/04/05/09/13[^fn5]. Tabelle *VG Tirol, VB 1895* zeigt die Statistik des Tiroler Volksboten vom 25.04.1895, welche 220 Hütekindern zu den einzelnen Gemeinden Tirols zuordnete[^fn6]. Tabelle *VG VB, Uh. 1922-23* umfasst die Herkunftsorte von 161 Kindern aus den Jahren 1922 und 1923, die Uhlig mittels Schulakten ermittelte[^fn7]. |

Daneben gibt es in dem Ordner *CSV-Dateien* eine Reihe von CSV-Dateien, die die Daten der bereits genannten Auswertungen in ein Format konvertieren, das von QGIS gelesen werden kann. Ohne diese Karten hätte das Kartenmaterial dieser Arbeit nicht erstellt werden können.











[^fn1]: [o.A.]: Ein Kinderhandel, in: Die Gartenlaube 4 (1866), S. 55. https://de.wikisource.org/wiki/Ein_Kinderhandel.

[^fn2]: Bauernhaus-Museum Wolfegg (Hrsg.): Die Schwabenkinder Datenbank, online: Schwabenkinder.eu, https://www.schwabenkinder.eu/de/Datenbank/datenbank-suche/ [22.11.2023].

[^fn3]: Fässler, Floreana: Appenzeller Schwabenkinder?, in: Innerrhoder Geschichtsfreund 1 (2013), S. 83–111.

[^fn4]: Lampert, Regina: Die Schwabengängerin. Erinnerungen einer jungen Magd aus Vorarlberg 1864-1874, Zürich 2022.

[^fn5]: Uhlig, Otto: Die Schwabenkinder aus Tirol und Vorarlberg (Tiroler Wirtschaftsstudien, Bd. 34), Innsbruck/Stuttgart 1983, S. 216/218.

[^fn6]:  [o.A.]: Der Hütkinderverein, in: Tiroler Volksbote (25.04.1895), S. 4; auch gefunden in: [o.A.]: Die Fahrt der Hütkinder und jugendlichen Arbeiter ins Schwabenland, in: Tiroler Stimmen (23.04.1895), S. 8.

[^fn7]: Uhlig, Schwabenkinder, S. 346.
