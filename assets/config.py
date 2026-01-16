from system import *
from assets.features import *
#### BOT CONFIG
api_id = 7960533
api_hash = "e63bd5f68ee3666ebd05b04c6387b0bb"
###### Sets
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
## Count
def count_groups():
    accs = list_accounts()
    if not accs:
        print(f"{r}No accounts available{w}")
        return

    total_ds = 0

    for acc in accs:
        try:
            app = Client(os.path.join(SESS_DIR, acc), api_id, api_hash)
            with app:
                dialogs = app.get_dialogs()
                ds_groups = [
                    d.chat.id
                    for d in dialogs
                    if getattr(d.chat, "title", None) and d.chat.title.startswith("DS")
                ]
                print(f"{y}{acc}:{g} {len(ds_groups)} groups found{w}")
                total_ds += len(ds_groups)
        except FloodWait as e:
            print(f"{acc} FloodWait {e.value}s")
            time.sleep(e.value)
        except Exception as e:
            print(f"Error loading account {acc}: {e}")

    print(f"\n{y}Total DS groups across all accounts:{g} {total_ds}")
    input(f"{z}Tap to go back:{w} ")
