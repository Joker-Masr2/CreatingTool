# Imports
import sys, os, subprocess

try:
    from pyrogram import Client
    from pyrogram.errors import FloodWait
except (ModuleNotFoundError, ImportError):
    print("[!] Installing pyrogram...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "pyrogram", "tgcrypto"
    ])
    from pyrogram import Client
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
__version__ = "2.3"
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

fix_me()
# Good
def clear_after_theme(theme_lines=14):
    print(f"\033[{theme_lines+1};0H", end="")
    print("\033[J", end="")

def cptl(text):
    for m in range(len(text)):
        print(p + text[:m].upper() + l, end="\r")
        time.sleep(.1)
    print()
## Timer
def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\rWaiting: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
   # print("\r✅ Resuming work...        ")

#### SYSTEM
SYSTEM = platform.system()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
SESS_DIR = os.path.join(BASE_DIR, "sessions")
os.makedirs(SESS_DIR, exist_ok=True)

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



#### BOT CONFIG
api_id = 7960533
api_hash = "e63bd5f68ee3666ebd05b04c6387b0bb"

C = 50
T = "DS"
DM = 1
GROUPS_BEFORE_WAIT = 10
WAIT_TIME = 600

MSG = [
    "هلو 🙋‍♂️","هلا والله 🤍","عايز فلوسسس",
    "هعععع ✨","شخباركم؟","حي الله الموجودين",
    "متواجد؟","نورتونا 🌹"
]

#### ACCOUNTS
def list_accounts():
    return [f.replace(".session","") for f in os.listdir(SESS_DIR) if f.endswith(".session")]

def add_account():
    print(f"\n{z}Type name or {r}Tap{z} to go back{w}")
    name = input("Account name: ").strip()
    if not name: return
    with Client(os.path.join(SESS_DIR, name), api_id, api_hash):
        print(f"{g}Account added{l}")
        time.sleep(2)
def delete_account():
    try:
        accs = list_accounts()
        if not accs:
            print(f"{r}No accounts{w}")
            time.sleep(2)
            return

        for i,a in enumerate(accs,1):
            print(i,a)
        print(f"\n{z}Choose number or {r}Tap{z} to go back{w}")
        ch = input("> ")
        if not ch.isdigit(): return
        acc = accs[int(ch)-1]
        for ext in [".session",".session-journal"]:
            f = os.path.join(SESS_DIR, acc+ext)
            if os.path.exists(f):
                os.remove(f)
        print(f"{g}Deleted {acc}{l}")
        time.sleep(2)
    except IndexError:
        cptl("plz type correct number ")
        time.sleep(2)
#### RUN TOOL
def run_tool(session):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    print(f"{y}▶ {session} Started{l}")

    try:
        app = Client(os.path.join(SESS_DIR, session), api_id, api_hash)
        with app:
            created = 0
            while created < C:
                try:
                    ch = app.create_supergroup(f"{T}_{created+1}")
                    created += 1
                    print(f"[{y}+{w}]{g} {session} ➜ {T}_{created}{l}")

                    for _ in range(10):
                        app.send_message(ch.id, random.choice(MSG))
                        time.sleep(DM)

                    if created % GROUPS_BEFORE_WAIT == 0:
#                        cptl(f"{y}waiting 10 min{l}")
                        countdown(WAIT_TIME)

                except FloodWait as e:
                    print(f"{r}{session} FloodWait {e.value}s{l}")
                    time.sleep(2)
                    return "flood"

        return "done"

    except Exception as e:
        print(f"{r}{session} stopped: {e}{l}")
        time.sleep(2)
        return "error"

    finally:
        loop.close()
        print(f"{z}■ {session} finished{l}")
#        time.sleep(2)
## run all
def run_all():
    accs = list_accounts()
    if not accs:
        print(f"{r}No accounts{w}")
        time.sleep(2)
        return

    results = []
    threads = []

    def worker(acc):
        res = run_tool(acc)
        results.append(res)

    for acc in accs:
        t = threading.Thread(target=worker, args=(acc,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    if all(r in ("flood", "error") for r in results):
        print(f"{r}All accounts stopped due to problems{l}")
        time.sleep(2)
        return

    print(f"{g}All accounts finished their tasks{l}")
    time.sleep(2)

#### MENU
def menu():
    while True:
  #      fix_me()
        clear_after_theme()
#        theme()
        print(f"""
1){z} Add account {w}
2){z} Show accounts {w}
3){z} Run on one {w}
4){z} Run on all {w}
5){z} Delete account {w}
6){z} Exit {w}
""")
        c = input("Choose: ").strip()

        if c == "1": add_account()
        elif c == "2":

            print("\n".join(list_accounts()) or "\033[1;91mNo accounts")
            time.sleep(2)
        elif c == "3":
            accs = list_accounts()
            if not accs: 
                print(f"{r}no accounts{w}")
                time.sleep(2)
                menu()
            try:
                for i,a in enumerate(accs,1): print(i,a)
                print(f"\n{z}Choose number or {r}Tap{z} to go back{w}")
                ch = input("> ")
                if ch.isdigit():
                    run_tool(accs[int(ch)-1])
            except IndexError:
                cptl("plz type correct number ")
                time.sleep(2)
                menu()
        elif c == "4": run_all()
        elif c == "5": delete_account()
        elif c == "6": break

#### START
try:
    theme()
    menu()
except KeyboardInterrupt:
    print(f"\n{r}Script stopped safely{l}")
    sys.exit(0)


