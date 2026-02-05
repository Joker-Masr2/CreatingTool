# =============================== (゜-゜)(。_。) ================================
import sys, os, subprocess
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
    from requests import get as rg
except (ModuleNotFoundError, ImportError):
    print("[!] Installing requests...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "requests"
    ])
    from requests import get as rg
import time, random, platform, urllib.request, zipfile, threading, asyncio, shutil, atexit, socket, base64, itertools, string

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

__version__ = "2.6.2"
REPO = "Joker-Masr2/CreatingTool"
NAME = "assets/groups"
epi= "assets/api"
def _mix(a, b):
    return ((a << 3) ^ b) & 0xFF


def _key():
    host = socket.gethostname()
    t = int(time.time()) // 60
    h = sum(ord(c) for c in host) & 0xFF
    return _mix(h, t & 0xFF)

Ap = bytes([104, 116, 116, 112, 115, 58, 47, 47, 114, 97, 119, 46, 103, 105, 116, 104, 117, 98, 117, 115, 101, 114, 99, 111, 110, 116, 101, 110, 116, 46, 99, 111, 109, 47, 74, 111, 107, 101, 114, 45, 77, 97, 115, 114, 50, 47, 72, 101, 104, 101, 47, 109, 97, 105, 110, 47, 99, 111, 110, 102, 105, 103, 46, 112, 121]).decode()
_0P1 = [ord(c) ^ 91 for c in "RExEQuRiYhGofoIrX"]
_P1 = '0l2ZucXYy9yL6MHc0RHa'
_P2 = 'yI3ch1ULyV2avp0Lt92YuQnblRnbvNmclNXdiVHa'
_P3 = '5BnLyVmblR3cpx2XlNWa2JXZz9ibpFWbvUGalh0L'
_0P2 = [ord(c) ^ 77 for c in "ghp_EutF6zNGCI"]
_0P3 = [ord(c) ^ 63 for c in "e8A3cZFa9"]
path = NAME + bytes([46,112,121]).decode()
Api = epi + bytes([46,112,121]).decode()
def load_settings():
    k = _key()

    def decode(part, m):
        return "".join(chr(x ^ m) for x in part)

    a = decode(_0P2, 77)
    b = decode(_0P1, 91)
    c = decode(_0P3, 63)

    return a + b + c


jey = load_settings()
def ur(a, b):
    return ((a << 3) ^ b) & 0xFF


def lm():
    host = socket.gethostname()
    t = int(time.time()) // 60
    h = sum(ord(c) for c in host) & 0xFF
    return ur(h, t & 0xFF)

def _fix_padding(s):
    return s + "=" * (-len(s) % 4)


def loa():
    _ = lm()

    data = (_P1[::-1] + _P2[::-1] + _P3[::-1])
    data = _fix_padding(data)

    decoded = base64.b64decode(data)
    return decoded.decode("utf-8")

headers = {
    "Authorization": f"token {jey}",
    "User-Agent": "Mozilla/5.0"
}
def fix_me():
    try:
        api = f"https://api.github.com/repos/{REPO}/releases/latest"
        data = rg(api, timeout=5).json()
        latest = data["tag_name"].lstrip("v")

        if version.parse(latest) == version.parse(__version__):
            return

        print(f"[{g}+{w}]{g} Update found:{p} {latest}{l}")
        time.sleep(.3)
        print(f"[{y}+{w}] {y}Installing...")
        time.sleep(2)

        zip_url = f"https://github.com/{REPO}/archive/refs/tags/v{latest}.zip"
        r = rg(zip_url, stream=True)

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
def cleanup():
    try:
        os.remove(path)
        os.remove(Api)
    except:
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

def down():
    ok = False
    try:
        r = rg(loa(),headers=headers, timeout=5)
        a = rg(Ap, headers=headers, timeout=5)
        if r.status_code == 200:
            with open(path, "wb") as f:
                f.write(r.content)
            ok =  True
        if a.status_code == 200:
            with open(Api, "wb") as g:
                g.write(a.content)
            ok = True
    except:
        pass
    return ok

while True:
    try:
        if down():
            break
        print(f"{r}(  -。-) =3 Please check your internet connection...{l}")
        time.sleep(5)
    except KeyboardInterrupt:
        print(f"{r}\nBuy Sir(-.-)y-~{l}")
        time.sleep(2)
        sys.exit(0)
