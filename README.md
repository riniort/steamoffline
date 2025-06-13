# SteamOffline

**SteamOffline** is a simple yet powerful tool that lets you **block or unblock Steam’s internet access** using Windows Firewall rules. Ideal for users who want to play games in offline mode without unwanted updates or syncs.

> ⚠️ **WARNING:** This app modifies your system firewall rules. Use with caution.  
> ⚠️ **Must be run as Administrator.**

---

## 🔐 Features

- ✅ One-click **block/unblock** for Steam internet access  
- ✅ Custom or default Steam.exe path support  
- ✅ Built-in **firewall rule reset**  
- ✅ Opens Windows Firewall UI for rule inspection  
- ✅ Lightweight GUI, no external libraries required  
- ✅ No background services or telemetry

---

## 💻 Usage Options

### 🟢 Option 1: Run as `.exe` (Recommended)
- Launch `steamoffline.exe` as **Administrator**
- Use the default or browse for your `Steam.exe` path
- Click the desired action:
  - **Block Steam Internet** – disables Steam's access to the internet
  - **Unblock Steam Internet** – restores access
  - **Reset Firewall Rule** – deletes and reapplies the block rule
  - **View Firewall Rules** – opens system firewall configuration

### 🐍 Option 2: Run with Python
- Requires Python 3.x installed
- Run `steamoffline.py` as **Administrator**

---

## 📌 Notes

- The firewall rule added is named: `Block_Steam_Internet`
- This app affects only the specified `Steam.exe` file
- All operations are local and reversible

---
