# IWI Informationssystem

Willkommen zum **IWI Informationssystem**! Dieses Projekt ist eine Anwendung zur Anzeige von Bildern in einer Diashow, die auf den Konfigurationen basiert, die in JSON-Dateien definiert sind. Die Anwendung unterstützt das Laden von Bilddateien aus einem bestimmten Verzeichnis und ermöglicht die Konfiguration der Anzeigeparameter.

## Installation

Um das Projekt lokal auszuführen, folgen Sie diesen Schritten:

1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/K1ngGrim/iwi-informations-system.git
   cd iwi-informations-system
   ```

2. Installieren Sie die erforderlichen Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

3. Stellen Sie sicher, dass die erforderlichen Bilddateien im angegebenen Verzeichnis vorhanden sind.

## Konfiguration

Das IWI Informationssystem verwendet zwei JSON-Konfigurationsdateien, um die Anwendung zu steuern. 

### Hauptkonfiguration

**Datei:** `appconfig.json`

```json
{
  "name": "iwi-information-system",
  "version": "1.0",
  "override-config": true,
  "allowed-files": [
    ".png", ".jpg", ".jpeg", ".gif", ".bmp"
  ],
  "folder": "../res/advertising"
}
```

- **name**: Der Name des Systems.
- **version**: Die aktuelle Version der Anwendung.
- **override-config** (unused): Gibt an, ob die Konfiguration überschrieben werden soll, wenn neue Dateien hinzugefügt werden. 
- **allowed-files**: Eine Liste von zulässigen Bildformaten, die in der Diashow angezeigt werden können.
  - **Folgende Dateitypen** wurden bisher getestet: `.png`, `.jpg`
- **folder**: Der Pfad zum Verzeichnis, das die Bilddateien enthält.

### Bildkonfiguration

**Datei:** Wird automatisch beim erstmaligen Ausführen im Ordner `$folder` der `appconfig.json` erzeugt. 

```json
{
    "files": [
        {
            "name": "File_1.png",
            "duration": 30,
            "upload_date": "2024-10-01",
            "active": true
        },
        {
            "name": "File_2.png",
            "duration": 30,
            "upload_date": "2024-10-01",
            "active": true
        }
    ]
}
```

- **files**: Eine Liste von Objekten, die die zu zeigenden Bilder darstellen.
  - **name**: Der Name der Bilddatei.
  - **duration**: Die Anzeigedauer des Bildes in Sekunden.
  - **upload_date**: Das Datum, an dem das Bild hochgeladen wurde.
  - **active**: Ein Boolean-Wert, der angibt, ob das Bild aktiv und sichtbar ist.

### Automatisches Hinzufügen neuer Dateien

Wenn Sie neue Bilddateien im Verzeichnis, das in der Hauptkonfiguration angegeben ist (`$folder`), hinzufügen, wird die Anwendung automatisch neue Einträge in der entsprechenden Konfigurationsdatei erzeugen.
Diese neuen Bilder werden dann automatisch in die Diashow eingereiht, basierend auf der Anzeigedauer, die in der Konfiguration für jedes Bild angegeben ist.

## Verwendung

1. Stellen Sie sicher, dass die erforderlichen Konfigurationsdateien im richtigen Verzeichnis vorhanden sind.
2. Fügen Sie die gewünschten Bilddateien in das angegebene Verzeichnis (`$folder`) hinzu.
3. Starten Sie die Anwendung:
   ```bash
   python main.py
   ```
4. **Automatischer Start unter Linux:**

   Um das IWI Informationssystem beim Anmelden automatisch zu starten, führen Sie die folgenden Schritte aus:
   - **Ausführbar machen:** Stellen Sie sicher, dass das Skript `add_to_autostart.sh` im Verzeichnis `scripts` ausführbar ist:
     ```bash
     chmod +x scripts/add_to_autostart.sh
     ```

   - **Skript ausführen:** Führen Sie das Skript aus, um die `.desktop`-Datei im Autostart-Verzeichnis zu erstellen:
     ```bash
     ./scripts/add_to_autostart.sh
     ```

## Lizenz

Dieses Projekt ist unter der **GNU General Public License** (GPL) lizenziert. Weitere Informationen finden Sie in der `LICENSE`-Datei.

## Beitrag

Wenn Sie zur Verbesserung des IWI Informationssystems beitragen möchten, können Sie Änderungen vorschlagen oder Pull-Requests erstellen. Wir freuen uns über jede Unterstützung!

---

Vielen Dank, dass Sie das IWI Informationssystem verwenden! Bei Fragen oder Problemen können Sie sich gerne an die Entwickler wenden.