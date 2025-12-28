#!/bin/bash
set -e

DB=~/printer_data/maintenance_manager.db

echo "🔄 Running database migration..."

if [ ! -f "$DB" ]; then
  echo "ℹ No database found, nothing to migrate."
  exit 0
fi

# Placeholder for future migrations
echo "✔ Database schema is up to date"

exit 0
