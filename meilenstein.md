# Meilenstein Studienarbeit 1 Gruppe G TIF20.5

Zum Ende der Studienarbeit befindet sich das Projekt auf folgendem Stand:

# Theoretische Vorarbeit

- "Analyse_und_Schwachstellen"
	- Eine Liste an möglichen Anforderungen an ein Wahlsystem wurde definiert
	- Das aktuelle System wurde im Hinblick auf diese Anforderungen untersucht
	- Eine Liste an Schwachstellen technischer und methodischer Natur wurde erstellt
- "Ausblick"
	- Eine Liste an möglichen zukünftigen Erweiterungen und theoretischen Betrachtungen wurde erstellt

# Komponenten des Wahlsystems

- Frontend
	- Wähler können Stimmen abgeben
	- Abgegebene Stimmen können verifiziert werden
	- Die Stimmen-Blockchain kann verifiziert werden
	- Nach Ende der Wahl können die Stimmen ausgezählt werden
	- Neue Konfigurationsdateien für Wahlen können erzeugt werden. Diese enthalten:
		- Startzeitpunkt der Stimmabgabe
		- Endzeitpunkt der Stimmabgabe
		- Anzahl der Wähler
		- Eine Liste der Wahloptionen
- Wahlserver
	- Eine Liste der Wahloptionen kann abgerufen werden
	- Stimmen können entgegengenommen und verschlüsselt werden
	- Stimmen können mehrfach zufällig zwischen Wahlservern hin- und hergeschickt werden, bevor sie an das Register gesendet werden
	- Stimmabgabe und Auszählung sind nur zeitlich begrenzt verfügbar
	- Konfigurationsinformationen werden aus einer Konfigurationsdatei eingelesen
- Register
	- Empfangene Stimmen werden auf einer Blockchain gespeichert
	- Die Blockchain kann abgerufen werden
- Setup-Skript
	- Authentifizierungsinformationen für Wähler können erzeugt und gespeichert werden
	- Administrator-Schlüssel kann erzeugt und gespeichert werden