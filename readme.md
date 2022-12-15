# Projekt Blockchain Voting TIF20

Gruppe G
Christoph Bieringer, Simon Schneider

Dieses Repository enthält Code, Dokumente etc. für die erste Studienarbeit von Gruppe G, TIF20.

# Über das Projekt

Im Rahmen dieser Studienarbeit wurde ein von einer Vorgängergruppe aus TIF19 übernommenenes, blockchain-basiertes E-Voting-System untersucht und erweitert.

# Aufbau des Projekts

Quellcode, Dockerfiles etc. befinden sich im Ordner "BlockchainTIF19AGruppeC".

Das Frontend befindet sich dort im Ordner "dhbw-blockchain-website".

Die Datenbank befindet sich dort im Ordner "dhbw-blockchain-mariadb".

Server, Setup-Skript etc. befinden sich dort im Ordner "dhbw-blockchain-encryption".
	- Die Wahlserver befinden sich dabei in den Dateien main.py, main1.py und main2.py.
	- Das Register befindet sich in register.py.
	- Das Setup-Skript zum Aufsetzen eine Wahl befindet sich in setup_election.py
	- Die Konfigurationsdatei befindet sich im Ordner "config" und trägt den Namen config.json.

Dokumentation befindet sich im Ordner "Dokumente".

Folien und Video für den Pitch befinden sich im Ordner "Video".

# First Start Guide
##Virtualenviroment Starten
### Virtualenv installieren
```bash
pip install virtualenv
```



## Wiederherstellen des MariaDB Docker Container
MariaDB Image mit Hilfe des Dockerfiles (/BlockchainTIF19AGruppeC/docker-compose-mariadb/Dockerfile-mariadb)
```bash
docker build . -t mariadb -f Dockerfile-mariadb
```
* * *
### Starte MariaDB Container aus Image
```bash
docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD='' -p 3306:3306 -d mariadb:latest 
```

### Kopiere auth_register.sql in Mariadb Container
```bash
sudo docker run --name mariadb -e MYSQL_ROOT_PASSWORD='' -p 3306:3306 -d mariadb:latest
```

* * *
### Verbindung zur MariaDB Container Shell aufbauen
```bash
docker exec  -it mariadb bash
```
### Anmelden in Mariadb mit 

```bash
mariadb -u root -p 
```
### Danach Passwort angeben
```SQL
CREATE DATABASE auth_register
```
### Mariadb verlassen mit ```exit```
* * *
### auth_register.sql in Container Kopieren
```bash
docker cp /path/to/auth_register.sql
```
### Datenbank aus auth_register.sql wiederherstellen
```bash
mariadb -u root -p auth_register < auth_register.sql
```
## Aufbau der Dokumentation

Eine Zusammenfassung der erreichten Ergebnisse zum Ende dieser Studienarbeit befindet sich im Dokument "Meilenstein.md".
Die restliche Dokumentation befindet sich (als Word- und PDF-Dateien) in "BlockchainTIF19AGruppeC/Dokumente".
	- "Systembeschreibung" enthält eine Beschreibung des E-Voting-Systems, wie es von der Vorgängergruppe hinterlassen wurde
	- "Analyse_und_Schwachstellen" enthält eine genauere Untersuchung des Systems, inklusive einer Auflistung verschiedener Schwächen und Mängel.
	- "Vorgenommene Änderungen" enthält eine Beschreibung der im Rahmen dieser Studienarbeit vorgenommenen Änderungen.
	- "Ausblick" enthält eine Übersicht über mögliche zukünftige Weiterentwicklungen und theoretische Betrachtungen.
	
Eine Präsentation über den Ablauf und die Ergebnisse der Studienarbeitet findet sich in Präsentation.pptx.
