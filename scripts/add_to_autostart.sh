#!/bin/bash

# Name der Desktop-Datei
AUTOSTART_FILE="$HOME/.config/autostart/iwi-informations-system.desktop"

# Erstelle den .desktop-Datei Inhalt
echo "[Desktop Entry]" > "$AUTOSTART_FILE"
echo "Type=Application" >> "$AUTOSTART_FILE"
echo "Exec=sh -c 'cd $HOME/Dokumente/iwi-informations-system/app && /usr/bin/python3 main.py'" >> "$AUTOSTART_FILE"
echo "Hidden=false" >> "$AUTOSTART_FILE"
echo "NoDisplay=false" >> "$AUTOSTART_FILE"
echo "X-GNOME-Autostart-enabled=true" >> "$AUTOSTART_FILE"
echo "Name=iwi-informations-system" >> "$AUTOSTART_FILE"
echo "Comment=Start the IWI Informationssystem" >> "$AUTOSTART_FILE"

# Mache die .desktop-Datei ausführbar
chmod +x "$AUTOSTART_FILE"

echo "Die Anwendung wurde zum Autostart hinzugefügt."
