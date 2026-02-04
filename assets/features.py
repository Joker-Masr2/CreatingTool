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

# ========== ======= ===================== 
def cptll(text, stop_event, speed=0.2):
    ln = len(text)

    while not stop_event.is_set():
        for i in range(ln):
            if stop_event.is_set():
                break

            out = ""
            for j, ch in enumerate(text):
                if j == i:
                    out += g + ch.upper() + l 
                elif j < i:
                    out += r + ch.lower() + l
                else:
                    out += ch.lower()

            print(out, end="\r")
            time.sleep(speed)

    print(" " * (ln + 10), end="\r")

# ===================== My bad, sorry for this salad ＼(-_-) =================

__version__ = "3.0.0"
REPO = "Joker-Masr2/CreatingTool"
UPDATE_DIR = "updates" 

def check_update():
    try:
        Path(UPDATE_DIR).mkdir(exist_ok=True)

        api = f"https://api.github.com/repos/{REPO}/releases/latest"
        data = requests.get(api, timeout=5).json()

        latest = data.get("tag_name")
        if latest == __version__:
            return

        for asset in data.get("assets", []):
            if not asset["name"].endswith(".exe"):
                continue

            path = Path(UPDATE_DIR) / asset["name"]

            if path.exists():
                print(f"[{y}!{l}]{z} Update already downloaded {l}")
                print(f"[{y}>{l}] {y}Path:{z} {path.resolve()} {l}")
                time.sleep(5)
                os.startfile(path.parent)
                return

            print(f"[{y}!{l}]{z} New version available:{g} {latest}{l}")

            stop_event = threading.Event()
            anim = threading.Thread(
                target=cptll,
                args=("Downloading...", stop_event)
            )
            anim.start()

            resp = requests.get(asset["browser_download_url"], stream=True)
            with open(path, "wb") as f:
                for c in resp.iter_content(1024):
                    if c:
                        f.write(c)

            stop_event.set()
            anim.join()

            print(f"[{y}+{l}]{g} Update downloaded successfully {l}")
            print(f"[{y}>{l}] {y}Path:{z} {path.resolve()} {l}")

            time.sleep(5)
            os.startfile(path.parent)
            return

    except Exception:
        pass

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

