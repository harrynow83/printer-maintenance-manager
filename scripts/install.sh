#!/bin/bash
set -e

echo "🛠️ Installing Printer Maintenance Manager..."

BASE=~/printer_data
PLUGIN=$BASE/printer_maintenance_manager

mkdir -p $PLUGIN
cp -r printer_maintenance_manager/* $PLUGIN

pip3 install -r requirements.txt

CONF=$BASE/config/moonraker.conf

if ! grep -q printer_maintenance_manager "$CONF"; then
cat <<EOF >> $CONF

[printer_maintenance_manager printer]
EOF
fi

sudo systemctl restart moonraker

echo "✅ Installation complete"
