#!/bin/bash

# Script to add the application to autostart in Fedora
APP_NAME="iwi-informations-system"
APP_DIR="/home/$(whoami)/iwi-informations-system/app"
AUTOSTART_DIR="$HOME/.config/autostart"
AUTOSTART_FILE="$AUTOSTART_DIR/${APP_NAME}.desktop"

# Create the autostart directory if it doesn't exist
mkdir -p "$AUTOSTART_DIR"

# Create the .desktop file
cat <<EOL > "$AUTOSTART_FILE"
[Desktop Entry]
Type=Application
Exec=/usr/bin/python3 $APP_DIR/main.py > /home/$(whoami)/iwi-informations-system/output.log 2>&1
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=$APP_NAME
Comment=Start the IWI Informationssystem
EOL

# Make the .desktop file executable
chmod +x "$AUTOSTART_FILE"

echo "Autostart entry created for $APP_NAME."
