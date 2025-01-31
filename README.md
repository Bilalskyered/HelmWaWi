# Motorradhelm-Suche (MVC-Pattern)

Dieses Projekt implementiert eine Helm-Suche im MVC-Pattern. Ihr erhaltet das Model bereits vorgegeben und schreibt selbst die Logik im Controller sowie die Terminal-Ein- und Ausgabe in der View.

## 📌 Projektstruktur

```
📂 HelmWaWi
├── 📂 Model
│   ├── __init__.py       # Initialisiert das Modul
│   ├── Helm.py           # Enthält die Helm-Klasse
│   ├── HelmBestand.py    # Enthält das Dictionary mit den Helmen
├── 📂 Controller
│   ├── __init__.py       # Initialisiert das Modul
│   ├── Logic.py          # Hier implementiert ihr die Logik zur Suche
├── 📂 View
│   ├── __init__.py       # Initialisiert das Modul
│   ├── Terminal.py       # Hier kommt die Ein- und Ausgabe für das Terminal hin
├── main.py               # Startpunkt des Programms
└── README.md             # Diese Anleitung
```

## 🚀 Setup und Installation

1. **Forkt das Repository** auf euren eigenen GitHub-Account.
2. **Clont das Repository** auf euren Rechner:
   ```sh
   git clone https://github.com/euer-benutzername/HelmWaWi.git
   ```
3. **Navigiert in das Projektverzeichnis:**
   ```sh
   cd HelmWaWi
   ```

## 🏗️ Eure Aufgaben

1. **Controller-Logik implementieren:**
   - Schreibt in `Controller/Logic.py` eine Funktion, die basierend auf den Eingaben des Nutzers die passenden Helme im Dictionary findet.
   - Diese Funktion soll die gefundenen Helme als `return`-Wert zurückgeben.

2. **View für Terminal-Eingabe/Ausgabe:**
   - Implementiert in `View/Terminal.py` eine Funktion zur Benutzereingabe (Größe, Preis etc.).
   - Ruft aus der View die entsprechende Methode im Controller auf.
   - Gebt die passenden Helme im Terminal aus.

3. **Hauptprogramm erstellen:**
   - In `main.py` ruft ihr die `View/Terminal.py` auf, um das Programm zu starten.

## ▶️ Programm starten

Das Programm wird über `main.py` gestartet:
```sh
python main.py
```

Viel Erfolg! 🚀
