#!/bin/bash
set -e

echo "🧹 Uninstalling Printer Maintenance Manager..."

BASE=~/printer_data
PLUGIN_DIR=$BASE/printer_maintenance_manager
DB_FILE=$BASE/maintenance_manager.db

if [ -d "$PLUGIN_DIR" ]; then
  rm -rf "$PLUGIN_DIR"
  echo "✔ Plugin files removed"
fi

CONF=$BASE/config/moonraker.conf

if grep -q printer_maintenance_manager "$CONF"; then
  sed -i.bak '/printer_maintenance_manager/d' "$CONF"
  echo "✔ Moonraker config cleaned"
fi

echo "ℹ Database NOT removed:"
echo "   $DB_FILE"
echo "   (remove manually if desired)"

sudo systemctl restart moonraker

echo "✅ Uninstall completed"
