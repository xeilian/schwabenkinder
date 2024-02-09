# The Social Topography of the Swabian Children: A GIS-based Investigation of Adolescent Labor Migration from Vorarlberg and Tyrol to Upper Swabia 1812-1938

## Table of contents

* **[1. Project Objective](#1-project-objective)**
* **[2. Documentation of Data in the Repository](#2-documentation-of-data-in-the-repository)**
  * [2.1. Evaluation of the Schwabenkinder Database](#21-evaluation-of-the-schwabenkinder-database)
    * *[2.1.1. Overview of the Tables](#211-overview-of-the-tables)*
    * *[2.1.2. Overview of the Fields in the Main Table](#212-overview-of-the-fields-in-the-main-table)*
  * [2.2. Overview of the Other Evaluations](#22-overview-of-the-other-evaluations)
  * [2.3. Overview of the charts and graphs](#23-overview-of-the-charts-and-graphs)
  * [2.4. Overview of Maps, Polygons, Tracks, and QGIS Layers](#24-overview-of-maps-polygons-tracks-and-qgis-layers)
    * *[2.4.1. Polygons, Tracks, and QGIS Layers](#241-polygons-tracks-and-qgis-layers)*
    * *[2.4.2. Overview of the maps](#242-overview-of-the-maps)*
  * [2.5. Overview of the Python Scripts](#25-overview-of-the-python-scripts)
  * [2.6. Miscellaneous](#26-miscellaneous)
    * *[2.6.1. Newspaper Articles](#261-newspaper-articles)*
    * *[2.6.2. Archive](#262-archive)*


## 1. Project Objective
The illustrated magazine 'Die Gartenlaube' reported in an issue from 1866 about a peculiar incident that occurred in a tavern somewhere between Lindau and Bregenz: "There sat a group of red-cheeked boys and girls of all ages, from seven to fifteen years old, each quietly absorbed in themselves [...]"[^fn1] The children were subsequently taken to the Ravensburg child labor market, where they were assessed for their performance under the critical eyes of Swabian farmers and taken into their service. "It is indeed a form of slave trade, no matter how one tries to look at this ugly matter with a milder eye."[^fn1] Scenes like those from the year 1866 were everyday occurrences in the central Alpine region a century ago: every March, children between the ages of seven and fifteen left their homes in Austria, Liechtenstein, and Switzerland to work in agriculture in southern Germany.

Exactly this phenomenon, which has been documented in writing since the 17th century, was the subject of my bachelor's thesis at the University of Heidelberg in late 2023. The centerpiece of the thesis was the first complete evaluation of the Swabian Children Database, which was created between 2008 and 2012 through the collaboration of museums and city archives from five countries as part of the EU Interreg IV project[^fn2]. This database contains 7,040 Swabian journeys of a total of 5,425 children spanning from 1697 to 1938, with those between the years 1860 and 1920 accounting for over 85% of the records. When reading any given record, one learns not only biographical details such as name, gender, age at the time of service, place and region of origin but also information about work assignments in Upper Swabia. This includes details about the start and end of service, the place of deployment with the corresponding municipality, the name of the employer, and the job title. Additionally, some information about the start and end of school exemption is included.

However, all geospatial data on places of origin and work are only provided in text form, making analysis using Geographic Information Systems (GIS) impossible. Nevertheless, in order to illustrate the geographical distribution and cumulative frequency of these occurrences in certain regions, all locations were georeferenced. Using methodological insights from spatial history and history from below, the thesis presented the results of this analysis and critically contextualized them with the addition of existing source material and scholarly interpretations. Furthermore, through economic, demographic, and topographic insights, the push and pull factors of the geographical distribution that led to these migration movements were revealed. It also sheds light on how the children even managed to travel from their places of origin to their places of service. From these findings emerged a social topography that captured the Swabian child labor system at a systemic level.

Although data from Switzerland and Liechtenstein are also available, this work has focused on Vorarlberg and Tyrol. Tyrol is understood in its original historical form, consisting of the present-day Austrian state of Tyrol (North and East Tyrol) and the present-day Italian autonomous region of Trentino-Alto Adige (South Tyrol and Trentino/Welschtirol). Since the idea of a sovereign South Tyrol emerged only in the 1920s and many Swabian children originated from there, the area south of the Brenner Pass is also examined. The destination of this migration is limited to the region of Upper Swabia in present-day Baden-Württemberg. Migrations to Bavaria were not recorded in the database. The study period is set from 1812 to 1938, reflecting the first and last entry in the database. Although there was a long tradition of this type of migration before 1812, the source material for the 19th century is extremely sparse.

## 2. Documentation of Data in the Repository

This Github repository contains all the data created in this work. This data material ranges from data evaluations in Excel tables, all maps created with QGIS including all polygons, tracks, and gpkg files. Also included are both the graphics used in the work that visualize the data evaluations, as well as all Python scripts created for this work. This documentation aims to provide an overview of the data published here so that they can be reused with appropriate acknowledgment.

### 2.1. Evaluation of the Schwabenkinder Database

The Schwabenkinder Database is available as an Excel table under the name [schwabenkinder_datenbank_v3.xlsx](https://github.com/xeilian/schwabenkinder/blob/main/%23schwabenkinder_datenbank_v3.xlsx). This contains all datasets accessible via the [official website](https://www.schwabenkinder.eu) of the Interreg project.

#### 2.1.1. Overview of the Tables

The database contains five tables that are interconnected through a complex network of formulas:
* *#Schwabenkinder-Datenbank* contains data on all 7,040 work assignments. This is the main table that contains all the data and to which the other tables refer. This is particularly useful for evaluating the work locations.
* *Kinder* contains the list of all children to determine the weighting of the places of origin. By removing multiple work assignments of a child, there are 5,425 unique entries about children left here.
* *Herkunftsorte* lists the number of places of origin per child and service and additionally contains all location information stored in the main table.
* *Arbeitsorte (nach Gemeinden)* lists the number of work locations per service (additionally divided into all regions of origin). This evaluation is based on the former municipalities in Upper Swabia and includes all location information from the main table.
* *Arbeitsorte (nach Orten)* does the same as above, but here the number of work locations is evaluated according to the individual municipal components (i.e., places).

#### 2.1.2. Overview of the Fields in the Main Table

| Spalte(n) | Feldname | Beschreibung |
| -------- | -------- | -------- |
| A | Kind-ID | ID of the child, extracted by the dataset number on the website |
| B | Arbeit-ID | ID of the work assignment, included in the CSV download from the website |
| C | Nachname | Last name of the child |
| D | Vorname | First name of the child |
| E | Herkunft: Ort | Name of the child's place of origin |
| F | Herkunft: Region | Modern region of the place of origin (e.g., state or canton) |
| G | Herkunft: Ort (G-ID) | Geonames ID of the place of origin |
| H | Herkunft: Ort (Lat.) | Longitude of the place of origin |
| I | Herkunft: Ort (Lon.) | Latitude of the place of origin |
| J | Herkunft: Gem. heute | Current municipality of the place of origin |
| K | Herkunft: Gem. heute (G-ID) | Geonames ID of the current municipality |
| L | Herkunft: Gem. heute (Lat.) | Longitude of the current municipality |
| M | Herkunft: Gem. heute (Lon.) | Latitude of the current municipality |
| N | Herkunft: Bevölkerung 1880 (nur T/VB) | Population of the place of origin in 1880 (only for Vorarlberg, current Tyrol and South Tyrol) |
| O/P | Herkunft: Lat./Lon. Visualisierung | Municipality-based evaluation. Since the coordinates represent the centroids of the municipalities, the coordinates of the main place were used for better visualization. |
| Q | Herkunft: Kreis/Bezirk/Bezirksgemeinschaft | Current district of the municipality |
| R | Tal | Valley of the place of origin (only for Vorarlberg and Tyrol) |
| S | Herkunft: Kreis (G-ID) | Geonames ID of the current district, etc. |
| T | Herkunft: Kreis (Lat.) | Longitude of the current district, etc. |
| U | Herkunft: Kreis (Lon.) | Latitude of the current district, etc. |
| V | Herkunft: Ort (Alternativ) | Alternative name of the place of origin |
| W | Geschlecht | (Assumed) gender of the child |
| X | Geburtsort | Birthplace of the child (if different from the place of origin) |
| Y | Geburtsdatum | Birthdate of the child |
| Z | Geburtsjahr | Birth year of the child (for better evaluation) |
| AA | Arbeit: Alter bei Beginn | Age of the child at the start of the work assignment |
| AB | Todestag | Death date of the child |
| AC | Arbeit: Schulbefreiung Start | Start of school exemption for the work assignment |
| AD | Arbeit: Schulbefreiung Ende | End of school exemption for the work assignment |
| AE | Arbeit: Beruf (raw) | Type of work as originally stated in the database |
| AF | Arbeit: Beruf | Type of work based on own categorization |
| AG | Arbeit: Dienstantritt Jahr | Year of starting the work assignment |
| AH | Arbeit: Dienstantritt | Date of starting the work assignment |
| AI | Arbeit: Dienstende Jahr | Year of ending the work assignment |
| AJ | Arbeit: Dienstende | Date of ending the work assignment |
| AK | Arbeit: Dienstherr | Name of the employer |
| AL | Arbeit: Ort | Name of the workplace |
| AM | Arbeit: Gem. alt | Municipality of the workplace before the municipal reform 1972/73 |
| AN | Arbeit: Gem. alt (Lat.) | Longitude of the former municipality |
| AO | Arbeit: Gem. alt (Lon.) | Latitude of the former municipality |
| AP | Arbeit: Verwaltungseinheit alt | Former administrative unit of the workplace (e.g., upper districts in the Kingdom of Württemberg) |
| AQ | Arbeit: Region alt | Region or former state of the workplace (e.g., Kingdom of Württemberg) |
| AR | Arbeit: Gem. heute | Current municipality of the workplace (after the municipal reform 1972/73) |
| AS | Arbeit: Region | Current region of the workplace (e.g., Baden-Württemberg) |
| AT | Arbeit: Gem. heute (G-ID) | Geonames ID of the current municipality |
| AU | Arbeit: Gem. heute (Lat.) | Longitude of the current municipality |
| AV | Arbeit: Gem. heute (Lon.) | Latitude of the current municipality |
| AW | Arbeit: Kreis | Current district of the workplace |
| AX | Arbeit: Kreis (G-ID) | Geonames ID of the current district |
| AY | Arbeit: Kreis (Lat.) | Longitude of the current district |
| AZ | Arbeit: Kreis (Lon.) | Latitude of the current district |
| BA | Arbeit: Ort (Alternativ) | Alternative name of the workplace |
| BB | Ehegatte Nachname | Last name of the spouse |
| BC | Ehegatte Vorname | First name of the spouse |
| BD | Hochzeitstag | Wedding date of the child |
| BE | Hochzeitsort | Wedding place of the child |
| BF | Vater Name | Father's name |
| BG | Vater Geburtstag | Father's birthdate |
| BH | Vater Beruf | Father's profession |
| BI | Mutter Name | Mother's name |
| BJ | Mutter Geburtstag | Mother's birthdate |
| BK | Mutter Beruf | Mother's profession |
| BL | Geschwister | Siblings of the child |
| BM | Nachfahren | Descendants of the child |
| BN | Quellen Museum | Source reference |
| BO | Kommentare öffentlich | Public comment from the database creators |

### 2.2. Overview of the Other Evaluations

In addition to the arguably most important file in the repository, the analysis of the Swabian Children Database, the following other analyses are listed below. These files, contained in the folder ***[[GIS] Auswertungen](https://github.com/xeilian/schwabenkinder/tree/main/%5BGIS%5D%20Auswertungen)***, are not documented in as much detail since they primarily consist of working tables that are not suitable for reuse.

| File Name | Suitable for Reuse? | Description |
| -- | -- | -- |
| schwabenkinder_anno_auswertung.xlsx | No | This is a work table for the newspaper analysis, where the number of Swabian children per year was noted based on newspaper reports. |
| schwabenkinder_bevölkerungsstatistik_1880.xlsx | Yes | This table contains all present-day municipalities in Tyrol and Vorarlberg, along with their administrative districts, municipality codes, and population figures for the years 1880 and 2001. Additionally, information on Geoname ID and coordinates has been included. Suitable for reuse.
| schwabenkinder_demographische_berechnungen_alt.xlsx | No | This is a working table for calculating demography, population density, birth rate, and the number of villages and hamlets per region (specifically Vorarlberg, Upper Inn Valley, and Adige Valley). |
| schwabenkinder_faessler_appenzell.xlsx | Yes | Evaluation of Appenzell Inner Rhodes pass registers in a study by Floreana Fässler[^fn3]. This was used as a comparison of data from the database. |
| schwabenkinder_pivot_grafiken.xlsx | No | Working table for creating graphics using Excel's built-in pivot tool. |
| schwabenkinder_tagebuch_regina.xlsx | No | Working table for noting places in Regina Lampert's autobiography[^fn4]. This was then used to create a custom map. The table includes data on date, time of day, mode of transportation, places, and page number. |
| schwabenkinder_vergleiche.xlsx | Yes | This file contains three evaluations that were used as comparisons from the database data. Table *VG Tirol, Uh. 1901-13* shows an evaluation by Otto Uhlig of school exemptions and pass registers per place of origin for the years 1901/04/05/09/13[^fn5]. Table *VG Tirol, VB 1895* shows the statistics from the Tyrolean People's Messenger of April 25, 1895, which assigned 220 hat children to the individual municipalities of Tyrol[^fn6]. Table *VG VB, Uh. 1922-23* covers the places of origin of 161 children from the years 1922 and 1923, which Uhlig determined using school records[^fn7]. |

In addition to these, there are several CSV files in the *CSV-Dateien* folder that convert the data from the aforementioned analyses into a format readable by QGIS. Without these maps, the cartographic material for this work could not have been created.

### 2.3. Overview of the charts and graphs

The charts and graphs created for this work aim to visually illustrate the analyses of the data from the database. The graphics contained in the folder ***[[GIS] Grafiken](https://github.com/xeilian/schwabenkinder/tree/main/%5BGIS%5D%20Grafiken)*** are displayed in their entirety below. Clicking on any of the images will take you to their location where the file can be viewed in higher resolution.

| <--> | <--> | <--> |
| -- | -- | -- |
| [![Grafik, Alter.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Alter.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Alter.png) <br> *Chart, Age* | [![Grafik, Alterspyramide.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Alterspyramide.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Alterspyramide.png) <br> *Chart, Age pyramid* | [![Grafik, Dienstbeginne und enden.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Dienstbeginne%20und%20enden.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Dienstbeginne%20und%20enden.png) <br> *Graph, Start and End of the service* |
| [![Grafik, Dienste.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Dienste.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Dienste.png) <br> *Chart, Type of service* | [![Grafik, Geschlecht.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Geschlecht.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Geschlecht.png) <br> *Chart, gender* | [![Grafik, Hütekindermärkte.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20H%C3%BCtekinderm%C3%A4rkte.png?raw=true)](https://example.com/hütekindermärkte) <br> *Graph, child labor markets* |
| [![Grafik, Zeitliche Verteilung.png](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Zeitliche%20Verteilung.png?raw=true)](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Grafiken/Grafik%2C%20Zeitliche%20Verteilung.png) <br> *Graph, temporal distribution* | | |
| | | |

### 2.4. Overview of Maps, Polygons, Tracks, and QGIS Layers

Within the scope of this work, a database was analyzed and visualized using GIS methods, making it natural to represent the phenomenon of the Swabian Children using maps. The open-source program [QGIS](https://www.qgis.org/) was utilized for data visualization.

#### 2.4.1. Polygons, Tracks, and QGIS Layers

To represent the evaluations stored in the CSV file (above) on clear maps, polygons and tracks are required. Tracks represent lines, while polygons represent geographic areas. I needed a variety of different polygons and tracks to design my maps as I desired.

Tracks (such as valleys and railway lines) were extracted using the free tool [Overpass Turbo](https://overpass-turbo.eu/): Example Arlberg Railway. The Arlberg Railway has relation ID 1623486. This can be found by searching for the railway line on the map and right-clicking. A small menu will appear, where you need to click on "Object query". A side window will open, where you must select the railway and then the relation at the very bottom. Subsequently, a short script was used in Overpass Turbo to convert the relation ID into a downloadable GPX file. Some tracks (such as national borders) can be converted into polygons in QGIS.

The directory ***[[GIS] Tracks und Polygone](https://github.com/xeilian/schwabenkinder/tree/main/%5BGIS%5D%20Tracks%20und%20Polygone)*** contains all tracks and polygons used for this work. This includes railway lines from Austria and Germany, all regions of origin (such as cantons, districts, national borders, etc.), as well as the valleys required for the work.

However, historical geodata could not be extracted using Overpass Turbo, as OSM only contains current data. For this purpose, external shapefiles had to be used, such as those for administrative districts and historical state borders in the German Empire[^fn8]. Similar considerations apply to present-day Switzerland[^fn9].

The finished maps with all evaluations, borders, railway lines, etc., were saved in GeoPackage files with all settings (such as text sizes, fonts, etc.). These files allow for the rapid reproduction of the maps in QGIS, as all tracks, polygons, or CSV files stored in the file are automatically opened upon import. This allows for a more detailed examination of the geographical distribution of places, which a static map does not allow. In the directory ***[[GIS] QGIS-Layer](https://github.com/xeilian/schwabenkinder/tree/main/%5BGIS%5D%20QGIS-Layer)***, there are 12 .gpkg files listed below:

| File Name | Description |
| -- | -- |
| layer_arbeit_bahnstrecken.gpkg | Railway lines to the work locations |
| layer_arbeit_landkreis.gpkg | Geolayer of the current districts of the work locations |
| layer_arbeit_regionen.gpkg | Geolayer of the former states (with administrative units) of the work locations |
| layer_arbeitsorte.gpkg | The work locations according to the former municipalities, weighted by the number of deployments |
| layer_herkunft_bahnstrecken.gpkg | Railway lines in the regions of origin |
| layer_herkunft_regionen_schweiz_fl.gpkg | Geolayer for Switzerland and Liechtenstein |
| layer_herkunft_regionen_tirol_vorarlberg.gpkg | Geolayer for Tyrol and Vorarlberg |
| layer_herkunft_täler.gpkg | Tracks of the valleys and polygons of the Bregenz Forest and Vinschgau
| layer_herkunftsorte.gpkg | The places of origin according to current municipalities, weighted by the number of children |
| layer_regina_jahr1.gpkg | The path of Regina Lampert from Schnifis to Berg in the first year |
| layer_vergleiche.gpkg | The comparisons of the database data with other surveys (above) |
| layer_wege.gpkg | The paths of the Swabian Children from Tyrol/Vorarlberg to Upper Swabia with the most important locations and passes, as well as the valleys |

#### 2.4.2. Overview of the maps

| | | |
| -- | -- | -- |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit%2C%20Bahnlinien.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit,%20Bahnlinien.png?raw=true" alt="Arbeit, Bahnlinien" height="175"></a> <br> *Work, Railway lines* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit%2C%20Landkreise.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit,%20Landkreise.png?raw=true" alt="Arbeit, Landkreise" height="175"></a> <br> *Work, Modern-day districs* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit%2C%20Verkehrsaufkommen.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeit,%20Verkehrsaufkommen.png?raw=true" alt="Arbeit, Verkehrsaufkommen" height="175"></a> <br> *Work, Traffic volume* |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeitsorte.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Arbeitsorte.png?raw=true" alt="Arbeitsorte" height="175"></a> <br> *Workplaces* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Grafik%2C%20Regina%20Lampert%2C%20Jahr%201.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Grafik,%20Regina%20Lampert,%20Jahr%201.png?raw=true" alt="Grafik, Regina Lampert, Jahr 1" height="175"></a> <br> *Way of Regina Lampert, Year 1* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Bahnlinien.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Bahnlinien.png?raw=true" alt="Herkunft, Bahnlinien" height="175"></a> <br> *Origin regions, railway lines* |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Graub%C3%BCnden.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Graub%C3%BCnden.png?raw=true" alt="Herkunft, Graubünden" height="175"></a> <br> *Origin regions, Graubünden* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Nordtirol.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Nordtirol.png?raw=true" alt="Herkunft, Nordtirol" height="175"></a> <br> *Origin regions, Northern Tyrol* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20S%C3%BCdtirol.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20S%C3%BCdtirol.png?raw=true" alt="Herkunft, Südtirol" height="175"></a> <br> *Origin regions, South Tyrol* |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20St.%20Gallen%2C%20Liechtenstein%20und%20Appenzell.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20St.%20Gallen,%20Liechtenstein%20und%20Appenzell.png?raw=true" alt="Origin regions, St. Gallen, Liecht., Appenzell" height="175"></a> <br> *Herkunft, St. Gallen, Liecht., Appenzell* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Trentino.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Trentino.png?raw=true" alt="Herkunft, Trentino" height="175"></a> <br> *Origin regions, Trentino* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Vorarlberg.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Vorarlberg.png?raw=true" alt="Herkunft, Vorarlberg" height="175"></a> <br> *Origin regions, Vorarlberg* |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft%2C%20Wege.jpg"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Herkunft,%20Wege.jpg?raw=true" alt="Herkunft, Wege" height="175"></a> <br> *Origin regions, Ways* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t%2C%20Tiroler%20Volksbote%201895.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t,%20Tiroler%20Volksbote%201895.png?raw=true" alt="Validität, Tiroler Volksbote 1895" height="175"></a> <br> *Validity, Tiroler Volksbote 1895* | <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t%2C%20Uhlig%20Tirol%201901-13.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t,%20Uhlig%20Tirol%201901-13.png?raw=true" alt="Validität, Uhlig Tirol 1901-13" height="175"></a> <br> *Validity, Uhlig Tirol 1901-13* |
| <a href="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t%2C%20Uhlig%20VB%201923.png"><img src="https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Karten/Validit%C3%A4t,%20Uhlig%20VB%201923.png?raw=true" alt="Validität, Uhlig VB 1923" height="175"></a> <br> *Validity, Uhlig VB 1923* |  |  |
| | | |

### 2.5. Overview of the Python Scripts

Below are all the Python scripts written for this work. The scripts located in the folder ***[[GIS] Python-Scripte](https://github.com/xeilian/schwabenkinder/tree/main/%5BGIS%5D%20Python-Scripte)*** have evolved over time. Therefore, it cannot be guaranteed that they will function properly upon initial execution.

| Title with Link | Description |
| -- | -- |
| [[SK] #01 DB extrahieren und in XLSX kombinieren.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2301%20DB%20extrahieren%20und%20in%20XLSX%20kombinieren.py) | This script extracts the records from the original database and combines them into an Excel spreadsheet. |
| [[SK] #02 Geodaten aus Geonames extrahieren.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2302%20Geodaten%20aus%20Geonames%20extrahieren.py) | This script extracts geodata from the Geonames API. The input consists of the names of the places of origin and work. |
| [[SK] #03 Geonames-ID extrahieren [Erster Versuch].py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2303%20Geonames-ID%20extrahieren%20%5BErster%20Versuch%5D.py) | This script did not yield the desired results, see scripts 6 and 7. The idea was to extract the Geonames ID via the Geonames API. The input was the coordinates. |
| [[SK] #04 Koordinaten extrahieren.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2304%20Koordinaten%20extrahieren.py) | This script is intended to add coordinates that were not extracted at the time. |
| [[SK] #05 Leere Zeilen auffüllen.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2305%20Leere%20Zeilen%20auff%C3%BCllen.py) | This script is supposed to fill in empty rows in the Excel document with missing data. Unfortunately, this did not work in this case. |
| [[SK] #06 Geonames-ID extrahieren (für Herkunftsorte).py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2306%20Geonames-ID%20extrahieren%20(f%C3%BCr%20Herkunftsorte).py) | This script extracts the Geonames ID for the places of origin via the Geonames API. The input consists of the place, the country, and the ADM code in Geonames. |
| [[SK] #07 Geonames-ID extrahieren (für Arbeitsorte).py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2307%20Geonames-ID%20extrahieren%20(f%C3%BCr%20Arbeitsorte).py) | The same procedure as in script 7, but for the workplaces. |
| [[SK] #08 Wahrheitstest für Ortschaften.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2308%20Wahrheitstest%20f%C3%BCr%20Ortschaften.py) | This script checks whether Geonames also finds the places with the place names. Up to that point, there was a problem that the script instead took over the administrative Geonames entries. Entries can then be refilled with the above scripts. |
| [[SK] #09 ADM-Daten extrahieren.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2309%20ADM-Daten%20extrahieren.py) | This script extracts all administrative information of a location with the Geonames ID. This includes data on country, state/province, regions, counties, and municipalities. |
| [[SK] #10 Bevölkerungsstatistik, Geonames-ID und Koordinaten extrahieren.py](https://github.com/xeilian/schwabenkinder/blob/main/%5BGIS%5D%20Python-Scripte/%5BSK%5D%20%2310%20Bev%C3%B6lkerungsstatistik%2C%20Geonames-ID%20und%20Koordinaten%20extrahieren.py) | This script extracts Geonames ID and coordinates for the population statistics of 1880 (see: file *schwabenkinder_bevölkerungsstatistik_1880.xlsx*). The main table can be supplemented with population data using the XLOOKUP function in Excel. |




### 2.6. Miscellaneous

#### 2.6.1. Newspaper Articles

The repository also contains all newspaper articles used in this work. These were downloaded via the ANNO newspaper portal of the Austrian National Bank[^fn10] and can be accessed as JPGs in the folder ***[Zeitungsartikel](https://github.com/xeilian/schwabenkinder/tree/main/Zeitungsartikel)***. The data follows the format *[Newspaper Abbreviation] Year-Month-Day, Page*. Below is the key to the newspaper abbreviations:

| Newspaper Abbreviation | Newspaper Name |
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

#### 2.6.2. Archive

Under ***[[Archiv]](https://github.com/xeilian/schwabenkinder/tree/main/%5BArchiv%5D)*** are all remaining worktables and ideas that could not be implemented.

- In the main directory:
  - *[SK] GPX-Dateien aus Komoot.zip:* This ZIP contains the GPX files published on Komoot as part of the former Interreg project.
  - *[SK] Rohdaten aus DB.zip:* This ZIP contains all individual CSV files as extracted from the database with script 1.
- Folder 'Excel-Tabellen'
  - *schwabenkinder_datenbank_v0_raw.xls:* This is the raw database composed of the individual pieces from the script.
  - *schwabenkinder_datenbank_v1/v2.xlsx:* Two intermediate states of the database. Both were created for data backup.
  - *schwabenkinder_doc_admex[...].xlsx:* These files are worktables created for the extraction of administrative entries.
  - *schwabenkinder_geonames[...].xlsx:* These are also worktables created for the extraction of original data from Geonames.
  - *schwabenkinder_gephi[...].xlsx/.csv:* Abandoned attempts with Gephi, a data analysis tool. Unfortunately, the results from Gephi were not useful and, above all, confusing.
- Folder 'Kartenmaterial': This folder contains original map material that was replaced by QGIS layers.
- Folder 'Versuche mit Mapbox': As the name suggests, the folder contains files created for visualization in Mapbox. Unfortunately, this project had to be (temporarily) abandoned due to time constraints.


[^fn1]: [o.A.]: Ein Kinderhandel, in: Die Gartenlaube 4 (1866), S. 55. https://de.wikisource.org/wiki/Ein_Kinderhandel.

[^fn2]: Bauernhaus-Museum Wolfegg (Ed.): The Swabian Children Database, online: Schwabenkinder.eu, https://www.schwabenkinder.eu/de/Datenbank/datenbank-suche/ [22.11.2023].

[^fn3]: Fässler, Floreana: Appenzeller Schwabenkinder?, in: Innerrhoder Geschichtsfreund 1 (2013), S. 83–111.

[^fn4]: Lampert, Regina: Die Schwabengängerin. Erinnerungen einer jungen Magd aus Vorarlberg 1864-1874, Zürich 2022.

[^fn5]: Uhlig, Otto: Die Schwabenkinder aus Tirol und Vorarlberg (Tiroler Wirtschaftsstudien, Bd. 34), Innsbruck/Stuttgart 1983, S. 216/218.

[^fn6]:  [o.A.]: Der Hütkinderverein, in: Tiroler Volksbote (25.04.1895), S. 4; auch gefunden in: [o.A.]: Die Fahrt der Hütkinder und jugendlichen Arbeiter ins Schwabenland, in: Tiroler Stimmen (23.04.1895), S. 8.

[^fn7]: Uhlig, Schwabenkinder, S. 346.

[^fn8]: Historical GIS datafiles, online: Censusmosaic, https://censusmosaic.demog.berkeley.edu/data/historical-gis-files [12.12.2023].

[^fn9]: swissBOUNDARIES3D, online: Bundesamt für Landestopographie der Schweiz, https://swisstopo.admin.ch/de/geodata/landscape/boundaries3d.html [22.12.2023].

[^fn10]: ANNO Historische Zeitungen und Zeitschriften, online: Österreichische Nationalbibliothek, https://anno.onb.ac.at/ [05.11.2023].

