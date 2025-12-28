# 🧼 Printer Maintenance Manager

A Moonraker plugin that **tracks printer usage** and **manages scheduled maintenance**
for Klipper-based 3D printers.

## 🖥️ Supported Systems

- Raspberry Pi (recommended)
- Klipper
- Moonraker
- Mainsail or Fluidd

---

## 📦 What It Does

The plugin automatically:
1. Tracks how long your printer is powered on
2. Tracks how long it is actively printing
3. Compares usage against maintenance intervals
4. Warns you when maintenance is due
5. Lets you reset maintenance after service

---

## 🧩 Dashboard Widget

The plugin exposes a Moonraker API endpoint that can be added
as a **Custom API Widget** in:

- ✅ Mainsail (full support, reset button included)
- ✅ Fluidd (read-only view)

---

## 🔔 Alerts (Optional)

Telegram alerts notify you when maintenance is required.

Alerts are:
- Optional
- Retry-safe
- Non-blocking (never crash the printer)

---

## Installation
```bash
git clone https://github.com/harrynow83/printer-maintenance-manager
cd printer-maintenance-manager
./scripts/install.sh


