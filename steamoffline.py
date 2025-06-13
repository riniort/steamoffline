import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import ctypes
import sys

# Default Steam path
DEFAULT_STEAM_PATH = r"C:\Program Files (x86)\Steam\Steam.exe"
RULE_NAME = "Block_Steam_Internet"

# Admin check
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def show_admin_warning():
    ctypes.windll.user32.MessageBoxW(
        0,
        "This app must be run as Administrator to modify firewall rules.\n\nRight-click the script or .exe and choose 'Run as administrator'.",
        "Administrator Required",
        0x10  # MB_ICONWARNING
    )

if not is_admin():
    show_admin_warning()
    sys.exit()

# Firewall actions
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Command failed:\n{e}")

def get_steam_path():
    path = path_entry.get()
    if not os.path.isfile(path):
        messagebox.showerror("Error", "Invalid Steam.exe path.")
        return None
    return path

def block_steam():
    path = get_steam_path()
    if not path: return
    command = f'netsh advfirewall firewall add rule name="{RULE_NAME}" dir=out program="{path}" action=block enable=yes'
    run_command(command)
    messagebox.showinfo("Success", "Steam internet access blocked.")

def unblock_steam():
    path = get_steam_path()
    if not path: return
    command = f'netsh advfirewall firewall delete rule name="{RULE_NAME}" program="{path}"'
    run_command(command)
    messagebox.showinfo("Success", "Steam internet access unblocked.")

def reset_steam_rule():
    path = get_steam_path()
    if not path: return
    delete_cmd = f'netsh advfirewall firewall delete rule name="{RULE_NAME}" program="{path}"'
    add_cmd = f'netsh advfirewall firewall add rule name="{RULE_NAME}" dir=out program="{path}" action=block enable=yes'
    subprocess.run(delete_cmd, shell=True)
    run_command(add_cmd)
    messagebox.showinfo("Success", "Steam firewall rule reset.")

def browse_path():
    file_path = filedialog.askopenfilename(
        title="Select Steam.exe",
        filetypes=[("Executable files", "*.exe")],
        initialdir=os.path.dirname(DEFAULT_STEAM_PATH)
    )
    if file_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, file_path)

def open_firewall_settings():
    try:
        subprocess.Popen("wf.msc", shell=True)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open firewall settings:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Steam Internet Blocker")
root.geometry("460x270")

tk.Label(root, text="Steam.exe Path:", font=("Arial", 10)).pack(pady=(10, 0))

path_frame = tk.Frame(root)
path_frame.pack(pady=5)

path_entry = tk.Entry(path_frame, width=50)
path_entry.insert(0, DEFAULT_STEAM_PATH)
path_entry.pack(side=tk.LEFT, padx=(0, 5))

browse_btn = tk.Button(path_frame, text="Browse...", command=browse_path)
browse_btn.pack(side=tk.LEFT)

block_btn = tk.Button(root, text="Block Steam Internet", width=30, command=block_steam)
block_btn.pack(pady=5)

unblock_btn = tk.Button(root, text="Unblock Steam Internet", width=30, command=unblock_steam)
unblock_btn.pack(pady=5)

reset_btn = tk.Button(root, text="Reset Firewall Rule", width=30, command=reset_steam_rule)
reset_btn.pack(pady=5)

view_btn = tk.Button(root, text="View Firewall Rules", width=30, command=open_firewall_settings)
view_btn.pack(pady=10)

root.mainloop()
