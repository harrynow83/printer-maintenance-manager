# User Guide — Printer Maintenance Manager

Printer Maintenance Manager helps you track printer usage
and reminds you when maintenance is required.

## What does it track?

- ⏱️ Total print hours
- ⚡ Total power-on hours
- 🧼 Maintenance intervals

All data is stored persistently and survives reboots.

## Dashboard Widget

The plugin adds a **Maintenance widget** to the Mainsail dashboard.

It shows:
- Print hours
- Power hours
- Pending maintenance tasks

When maintenance is required, a warning will be shown.

## Resetting Maintenance

After performing maintenance:

1. Open the Dashboard
2. Find the Maintenance widget
3. Click the ✔ icon next to the task

This resets the maintenance counter.

## Alerts

If alerts are enabled (Telegram), you will receive a notification
when maintenance is due.

## Data Safety

- Data is stored locally
- No cloud connection
- No external tracking

## Troubleshooting

If the widget does not appear:
- Reload Mainsail
- Check Moonraker is running
- Verify plugin installation
