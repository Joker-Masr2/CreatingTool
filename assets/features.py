
# Imports
import sys, os, subprocess
from assets.features import *
try:
    from pyrogram import Client, filters, errors
    from pyrogram.errors import FloodWait
except (ModuleNotFoundError, ImportError):
    print("[!] Installing pyrogram...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "pyrogram", "tgcrypto"
    ])
    from pyrogram import Client, filters, errors
    from pyrogram.errors import FloodWait


try:
    from packaging import version
except (ModuleNotFoundError, ImportError):
    print("[!] Installing packaging...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "packaging"
    ])
    from packaging import version


try:
    import requests
except (ModuleNotFoundError, ImportError):
    print("[!] Installing requests...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "requests"
    ])
    import requests
import time, random, platform, urllib.request, zipfile, threading, asyncio, shutil

#### COLORS
w = "\033[1;97m"
g = "\033[1;92m"
y = "\033[1;93m"
z = "\033[1;96m"
r = "\033[1;91m"
b = "\033[1;94m"
p = "\033[1;91m\033[3m"
l = "\033[1;97m\033[0m"
##update
__version__ = "2.9.4"
REPO = "Joker-Masr2/CreatingTool"

def fix_me():
    try:
        api = f"https://api.github.com/repos/{REPO}/releases/latest"
        data = requests.get(api, timeout=5).json()
        latest = data["tag_name"].lstrip("v")
		
        if version.parse(latest) == version.parse(__version__):
            return

        print(f"[{g}+{w}]{g} Update found:{p} {latest}{l}")
        time.sleep(.3)
        print(f"[{y}+{w}] {y}Installing...")
        time.sleep(2)

        zip_url = f"https://github.com/{REPO}/archive/refs/tags/v{latest}.zip"
        r = requests.get(zip_url, stream=True)

        with open("update.zip", "wb") as f:
            for c in r.iter_content(1024):
                f.write(c)

        with zipfile.ZipFile("update.zip") as z:
            z.extractall("upd")

        folder = os.listdir("upd")[0]
        for i in os.listdir(f"upd/{folder}"):
            s = f"upd/{folder}/{i}"
            if os.path.isdir(s):
                shutil.copytree(s, i, dirs_exist_ok=True)
            else:
                shutil.copy2(s, i)

        shutil.rmtree("upd")
        os.remove("update.zip")

        restart()

    except Exception as e:
        print(f"[!] Update error: {e}")

def restart():
    os.execv(sys.executable, [sys.executable] + sys.argv)



#### Theme
def theme():
	os.system('clear')
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

#### Theme
def theme2():
        os.system('clear')
        print(f'''
{r}███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗ 
  ╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║
{w}███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║       ██║   ██║   ██║██║   ██║██║
╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║
{r}███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{r}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{r}Enjoy Boss...  {l}
{r}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{l}     ''')

