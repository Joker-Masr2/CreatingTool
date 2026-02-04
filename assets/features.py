# =============================== (゜-゜)(。_。) ================================
import sys, os, time, random, platform, zipfile, threading, asyncio, shutil, atexit
import socket, base64, itertools, string, subprocess
from packaging import version
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import requests
from pathlib import Path

# =====================  the most import thing ＼(^o^)／ ===================
w = "\033[1;97m"
g = "\033[1;92m"
y = "\033[1;93m"
z = "\033[1;96m"
r = "\033[1;91m"
b = "\033[1;94m"
p = "\033[1;91m\033[3m"
l = "\033[1;97m\033[0m"

# ===================== My bad, sorry for this salad ＼(-_-) =================

__version__ = "3.0.1"
REPO = "Joker-Masr2/CreatingTool"
UPDATE_DIR = "updates" 

def check_update():
    try:
        api = f"https://api.github.com/repos/{REPO}/releases/latest"
        data = requests.get(api, timeout=5).json()
        assets = data.get("assets", [])
        exe_assets = [a for a in assets if a["name"].endswith(".exe")]

        for asset in exe_assets:
            name = asset["name"]
            url = asset["browser_download_url"]
            file_path = Path(UPDATE_DIR) / name

            if file_path.exists():
                print(f"{y}[!] EXE already downloaded. Open it here: {g}{file_path.resolve()}{l}")
            else:
                print(f"{y}[!] New EXE available: {g}{name}{l}")
                print(f"{z}[!] Downloading...{l}")
                r = requests.get(url, stream=True)
                with open(file_path, "wb") as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                print(f"{g}[+] EXE saved successfully at {file_path.resolve()}{l}")
                print(f"{y}[+] You can now open it to run the new version.{l}")

    except Exception as e:
        print(f"{z}[!] Update check failed: {e}{l}")


# =======================  Theme  =========================
def theme():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f'''
{z}███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗ {r}{__version__}{z}
  ╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
{w}███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║       ██║   ██║   ██║██║   ██║██║     
╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║     
{z}███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{z}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{z}𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:{r} 𝔇𝔞𝔯𝔨 𝔖𝔱𝔬𝔯𝔪  {l}
{z}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{y}Note:{r} Run the scrpit once in the day to be away from bans.
The tool will make 50 groups for each run.
                                                                                    
{l}	''')

