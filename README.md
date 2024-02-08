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

Die Schwabenkinder-Datenbank ist als Excel-Tabelle unter dem Namen *schwabenkinder_datenbank_v3.xlsx* herunterladbar. Diese enthält alle, über die [offizielle Seite](https://www.schwabenkinder.eu) des Interreg-Projektes abrufbaren Datensätze. Diese sind auf fünf Tabellen aufgeteilt, die über ein komplexes Netz aus Formeln miteinander verbunden sind:
* *#Schwabenkinder-Datenbank* enthält Daten zu allen 7.040 Arbeitseinsätzen. Diese ist besonders für die Auswertung der Arbeitsorte hilfreich.
* *Kinder* enthält die Liste aller Kinder, um die Gewichtung der Herkunftsorte bestimmen zu können. Durch Herausnahme mehrfacher Arbeitseinsätze eines Kindes, bleiben hier 5.425 eindeutige Einträge zu Kindern übrig
* *Herkunftsorte* listet die Anzahl der Herkunftsorte pro Kind und Dienst auf und enthält zusätzlich alle in der Haupttabelle gespeicherten Ortsinformationen.
* *Arbeitsorte (nach Gemeinden)* listet die Anzahl der Arbeitsorte pro Dienst (zusätzlich aufgeteilt auf alle Herkunftsregionen) auf. Diese Auswertung geht nach den damaligen Gemeinden in Oberschwaben und übernimmt alle Ortsinformationen aus der Haupttabelle.
* *Arbeitsorte (nach Orten)* macht das gleiche wie oben, nur wird hier die Anzahl der Arbeitsorte nach den einzelnen Gemeindebestandteilen (also Orten) ausgewertet.









[^fn1]: [o.A.]: Ein Kinderhandel, in: Die Gartenlaube 4 (1866), S. 55. https://de.wikisource.org/wiki/Ein_Kinderhandel.

[^fn2]: Bauernhaus-Museum Wolfegg (Hrsg.): Die Schwabenkinder Datenbank, online: Schwabenkinder.eu, https://www.schwabenkinder.eu/de/Datenbank/datenbank-suche/ [22.11.2023].
