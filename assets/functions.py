# =============================== (゜-゜)(。_。) ================================
from assets.api import *
from assets.features import *

def open_channel():
    url = "https://t.me/creatingtool"
    cptl("📢 Openning Channel to Explain...")
    time.sleep(3)
    try:
        webbrowser.open(url)
    except:
        pass
    if "ANDROID_ROOT" in os.environ or "com.termux" in sys.prefix:
        os.system(f"am start -a android.intent.action.VIEW -d {url}")

# =========== Clear Screen ===============
def clear_after_theme(theme_lines=14):
    print(f"\033[{theme_lines+1};0H", end="")
    print("\033[J", end="")

# =================   My Fav function ( ´∀`)/~~ ===========

#def cptl(text):
 #   for m in range(len(text)):
  #      print(p + text[:m].upper() + l, end="\r")
   #     time.sleep(.1)
    #print()

def cptl(text):
    for m in range(len(text)):
        prev = text[:m].upper()
        colored_prev = "".join([r + c + l for c in prev])
        current = g + text[m] + l
        print(colored_prev + current, end="\r")
        time.sleep(0.1)
    final = "".join([r + c + l for c in text.upper()])
    print(final)

# ================    Timer   ===================

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{y}Waiting:{z} {mins:02d}:{secs:02d} {y}(￣ｑ￣)ｚｚｚ", end="")
        time.sleep(1)
        seconds -= 1
    print(f"\r{g} (⌒0⌒)／~~ Resuming work... {w} ")

# =================    Random name     ====================

def random_group_name(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# ==================      System     ======================

SYSTEM = platform.system()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
SESS_DIR = os.path.join(BASE_DIR, "sessions")
os.makedirs(SESS_DIR, exist_ok=True)
started_printed = False
start_lock = threading.Lock()

# ====================== Dealing with accounts  =======================

def list_accounts():
    return [f.replace(".session","") for f in os.listdir(SESS_DIR) if f.endswith(".session")]
def show_accounts():
    accounts = list_accounts() or []
    pined = "admin"
    if pined in accounts:
        accounts = [pined] + [a for a in accounts if a != pined]

    output = []
    for acc in accounts:
        if acc == pined:
            output.append(f"{y}■ Admin Exist (⌒∇⌒)ノ{l}\n")
        else:
            output.append(acc)
    print("\n".join(output) or f"{r}No accounts{l}")
    time.sleep(3)
#
import json

ADMIN_FILE = "assets/sessions/admin.json"

def admin_exists():
    return os.path.exists(ADMIN_FILE)

def save_admin(me):
    data = {
        "id": me.id,
        "username": me.username,
        "phone": me.phone_number
    }
    with open(ADMIN_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_admin_id():
    if not admin_exists():
        return None
    try:
        with open(ADMIN_FILE, "r", encoding="utf-8") as f:
            return json.load(f).get("id")
    except json.JSONDecodeError:
        cptl("Why u touch everything remove `admin.json` and don't touch it again (￣b￣)")
#
def cleanup_account(name):
    if not name:
        return
    if "/" in name or "\\" in name:
        return
    paths = [
        os.path.join(SESS_DIR, name),
        os.path.join(SESS_DIR, f"{name}.session"),
        os.path.join(SESS_DIR, f"{name}.json"),
        os.path.join(SESS_DIR, f"{name}.txt"),
    ]

    for path in paths:
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
        except Exception:
            pass
#
def save_account_info(name, phone, inputs=None):
    extracted_password = None
    if inputs:
        for prompt, value in inputs.items():
            if "enter password" in prompt.lower():
                extracted_password = value.strip() or None
                break

    txt_path = os.path.join(SESS_DIR, f"{name}.txt")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"Account: {name}\n")
        f.write(f"Phone: {phone}\n")
        f.write(f"2FA: {extracted_password if extracted_password else 'N/A'}\n")
#
def add_account():
#    from assets.groups import InputLogger
    admin_id = load_admin_id()
    if admin_id:
        print(f"\n{y}Admin account already registered (*^o^)／＼(^-^*){w}")
    else:
        print(f"\n{r}(゜ー゜)(。_。) No admin account registered yet (゜ー゜)(。_。){w}")

    print(f"\n{g}Add new account{w}\n")

    with InputLogger() as logger:
        name = input("Account name: ").strip()
        exists = list_accounts()
        if not name:
            cptl("(￣￢￣) Invalid name")
            time.sleep(2)
            return
        for acc in exists:
            if acc == name:
                cptl("HaHa account is already exists baby! (￣ー￣  )       ")
                time.sleep(5)
                return
        if name.lower() == "admin" and admin_exists():
            cptl("(￣ｑ￣)ｚｚｚ Admin account already exists  ")
            time.sleep(2)
            return
        session_path = os.path.join(SESS_DIR, name)

        try:
            with Client(session_path, api_id, api_hash) as app:
                me = app.get_me()
                phone = me.phone_number or "Unknown"
            if name.lower() == "admin":
                save_admin(me)
                cptl("(∩_∩;)P Admin registered successfully  ")
                time.sleep(2)
        #        return
        except KeyboardInterrupt:
            cptl("(∋_∈) Registration cancelled  ")
            time.sleep(2)
            cleanup_account(name)
            return

        except Exception as e:
            print(f"┐(-。ー;)┌ Failed to add account: {e}")
            time.sleep(2)
            cleanup_account(name)
            return

        else:
            save_account_info(
                name=name,
                phone=phone,
                inputs=logger.data
            )

            cptl("Account added successfully ゜゜゜゜゜-y(^。^)。o0○   ")
            time.sleep(2)
#
def delete_account():
    try:
        accs = list_accounts()
        if not accs:
            print(f"{r}No accounts{w}")
            time.sleep(2)
            return
        print(f"{y}Accounts:{w}\n")
        for i, a in enumerate(accs, 1):
            print(f"{i}){r} {a}{l}" if a == "admin" else f"{i}) {a}")

        print(f"\n{z}Choose number | {r}0{z} = Delete ALL | {r}Tap{z} to go back{w}")
        ch = input("> ").strip()

        if not ch.isdigit():
            return

        ch = int(ch)

        if ch == 0:
            confirm = input(f"{r}Are you sure? this will delete ALL sessions{l} ({r}y{l}/{y}n{l}): ").lower()
            if confirm != "y":
                return

            shutil.rmtree(SESS_DIR, ignore_errors=True)
            os.makedirs(SESS_DIR, exist_ok=True)

            cptl(f"All accounts deleted ♪ヽ(´▽｀)/  ")
            time.sleep(2)
            return

        acc = accs[ch - 1]

        removed = False

        for ext in [".session", ".session-journal",".txt", ".json"]:
            f = os.path.join(SESS_DIR, acc + ext)
            if os.path.exists(f):
                os.remove(f)
                removed = True

        if removed:
            cptl(f"Deleted {acc} φ(゜゜)ノ゜  ")
        else:
            cptl(f"Nothing to delete for(-.-)Zzz・・・・ {acc}   ")

        time.sleep(2)

    except IndexError:
        cptl("plz type correct number  ")
        time.sleep(2)

# =================    Count Groups    ===================

def count_groups():
    accs = list_accounts()
    if not accs:
        print()
        cptl("No accounts founded σ(^_^;)?   ")
        return

    total_ds = 0
    print()
    for acc in accs:
        try:
            if acc =="admin":
                continue
            app = Client(os.path.join(SESS_DIR, acc), api_id, api_hash)
            with app:
                dialogs = app.get_dialogs()
                ds_groups = [
                    d.chat.id
                    for d in dialogs
                    if getattr(d.chat, "title", None) and d.chat.title.startswith("DS")
                ]
                cptl(f"{acc}: {len(ds_groups)} groups found ")
                total_ds += len(ds_groups)
        except FloodWait as e:
            print(f"{acc} FloodWait {e.value}s")
            time.sleep(e.value)
        except Exception as e:	
            print(f"Error loading account {acc}: {e}")

    print(f"\n{y}Total DS groups across all accounts:{g} {total_ds} (^。^)")
    input(f"{z}Tap to go back:{w} ")

# =================================================================================== #
