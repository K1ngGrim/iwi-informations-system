#!/bin/bash

# Pfad zum Python-Skript
SCRIPT_PATH="/home/$USER/iwi-informations-system/main.py"

# Überprüfen, wo sich python3 befindet
PYTHON_PATH=$(which python3)

# Erstellen Sie die .desktop-Datei
AUTOSTART_FILE="$HOME/.config/autostart/iwi-informations-system.desktop"

echo "[Desktop Entry]" > "$AUTOSTART_FILE"
echo "Type=Application" >> "$AUTOSTART_FILE"
echo "Exec=$PYTHON_PATH $SCRIPT_PATH" >> "$AUTOSTART_FILE"
echo "Hidden=false" >> "$AUTOSTART_FILE"
echo "NoDisplay=false" >> "$AUTOSTART_FILE"
echo "X-GNOME-Autostart-enabled=true" >> "$AUTOSTART_FILE"
echo "Name[I]=iwi-informations-system" >> "$AUTOSTART_FILE"
echo "Name=iwi-informations-system" >> "$AUTOSTART_FILE"
echo "Comment=Start the IWI Informationssystem" >> "$AUTOSTART_FILE"

echo "Das Skript wurde zum Autostart hinzugefügt."
