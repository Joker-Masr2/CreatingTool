# =============================== (゜-゜)(。_。) ================================
from lib.down import *
from assets.features import *
def open_channel():
    url= "https://t.me/creatingtool"
    try:
        if os.name == "nt":
            subprocess.run(["cmd", "/c", "start", url])
        elif "ANDROID_ROOT" in os.environ:
            subprocess.run([
                "am", "start",
                "-a", "android.intent.action.VIEW",
                "-d", url
            ])
        else:
            subprocess.run(["xdg-open", url])
    except:
        print(f"{z}plz open: {y}https://t.me/creatingtool")
        time.sleep(4)
# =========== Clear Screen ===============
def clear_after_theme(theme_lines=14):
    sys.stdout.write(f"\033[{theme_lines + 1};1H\033[0J")
    sys.stdout.flush()

# ======== working ======
running = False
print_lock = threading.Lock()

def clear_line():
    cols = shutil.get_terminal_size().columns
    sys.stdout.write("\r" + " " * cols + "\r")

def safe_print(*args, **kwargs):
    with print_lock:
        clear_line()
        print(*args, **kwargs)

def working_animation(speed=0.5):
    word = "working..."
    i = 0

    while running:
        if print_lock.locked():
            time.sleep(0.05)
            continue

        with print_lock:
            letters = []
            for idx, c in enumerate(word):
                if idx == i:
                    letters.append(f"{r}{c.upper()}{l}")
                else:
                    letters.append(f"{y}{c.lower()}{l}")

            sys.stdout.write("\r" + "".join(letters))
            sys.stdout.flush()

        i = (i + 1) % len(word)
        time.sleep(speed)

    with print_lock:
        clear_line()

def start_working():
    global running
    running = True
    threading.Thread(target=working_animation, daemon=True).start()

def stop_working():
    global running
    running = False

# ================    Timer   ===================

#def countdown(seconds):
 #   while seconds > 0:
  #      mins, secs = divmod(seconds, 60)
   #     print(f"\r{y}Waiting:{z} {mins:02d}:{secs:02d} {y}(￣ｑ￣)ｚｚｚ", end="")
    #    time.sleep(1)
     #   seconds -= 1
#    print(f"\r{g} (⌒0⌒)／~~ Resuming work... {w} ")

def countdown(seconds):
    with Progress(transient=True) as progress:
        task = progress.add_task(f"{y}Waiting:{z} (￣ｑ￣)ｚｚｚ", total=seconds)
        while not progress.finished:
            mins, secs = divmod(seconds, 60)
            progress.update(
                task,
                description=f"{y}Waiting:{z} {mins:02d}:{secs:02d} {y}(￣ｑ￣)ｚｚｚ",
                advance=1
            )
            time.sleep(1)
            seconds -= 1
    console.print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",style="green")

# =================    Random name     ====================

def random_group_name(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# ==================      System     ======================

SYSTEM = platform.system()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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

    tree = Tree("🌩️ [bold magenta]ACCOUNTS[/bold magenta]")

    for acc in accounts:
        if acc == pined:
            tree.add(f"{y}■ Admin Exist (⌒∇⌒)ノ{l}")
        else:
            tree.add(acc)

    console.print(tree)
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
    exists = []
    username = get_current_user()
    if not username:
        cptl("⚠ No logged-in user found")
        return

    admin_id = load_admin_id()
    if admin_id:
        print(f"\n{y}Admin account already registered (*^o^)／＼(^-^*){w}")
    else:
        print(f"\n{r}(゜ー゜)(。_。) No admin account registered yet (゜ー゜)(。_。){w}")

    print(f"\n{g}Add new account{w}\n")

    with InputLogger() as logger:
        try:
            name = input("Account name: ").strip()
        except KeyboardInterrupt:
            return

        if not name:
            cptl("(￣￢￣) Invalid name")
            time.sleep(2)
            return

        ok, reason = add_account_and(username, increment=False)
        if not ok:
            cptl(f"(╥﹏╥) {reason}")
            time.sleep(2)
            return

        exists = list_accounts()
        for acc in exists:
            if acc == name:
                cptl("HaHa account already exists baby! (￣ー￣  )")
                time.sleep(5)
                return

        if name.lower() == "admin" and admin_exists():
            cptl("(￣ｑ￣)ｚｚｚ Admin account already exists")
            time.sleep(2)
            return

        session_path = os.path.join(SESS_DIR, name)

        try:
            with Client(session_path, api_id, api_hash) as app:
                me = app.get_me()
                phone = me.phone_number or "Unknown"

            if name.lower() == "admin":
                save_admin(me)
                console.print("(∩_∩;)P Admin registered successfully", style="green")
                time.sleep(2)

        except KeyboardInterrupt:
            cptl("(∋_∈) Registration cancelled")
            time.sleep(2)
            cleanup_account(name)
            return

        except Exception as e:
            print(f"┐(-。ー;)┌ Failed to add account: {e}")
            time.sleep(2)
            cleanup_account(name)
            return

        ok, reason = add_account_and(username, increment=True)
        if not ok:
            cleanup_account(name)
            cptl(f"(╥﹏╥) {reason}")
            time.sleep(2)
            return

        save_account_info(
            name=name,
            phone=phone,
            inputs=logger.data
        )

        console.print("Account added successfully ゜゜゜゜゜(^。^)。o0○", style="green")
        time.sleep(2)
#
def delete_account():
    try:
        accs = list_accounts()
        if not accs:
            print(f"{r}No accounts{w}")
            time.sleep(2)
            return
        tree = Tree("🌩️ [bold magenta]ACCOUNTS[/bold magenta]")
        for i, a in enumerate(accs, 1):
            tree.add(f"{i}){r} {a}{l}" if a == "admin" else f"{i}) {a}")
        console.print(tree)
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

            console.print(f"All accounts deleted ♪ヽ(´▽｀)/  ",style="green")
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
            console.print(f"Deleted {acc} φ(゜゜)ノ゜  ",style="green")
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
        console.print("\n[bold red]No accounts founded σ(^_^;)?[/bold red]")
        return
    print()
    console.print("Searching...",style="yellow")
    print()
    total_ds = 0
    tree = Tree("🌩️ [bold magenta]DS Groups Scanner[/bold magenta]")

    for acc in accs:
        if acc == "admin":
            continue

        try:
            app = Client(os.path.join(SESS_DIR, acc), api_id, api_hash)
            with app:
                dialogs = app.get_dialogs()
                ds_groups = [
                    d.chat.id
                    for d in dialogs
                    if getattr(d.chat, "title", None)
                    and d.chat.title.startswith("DS")
                ]

                count = len(ds_groups)
                total_ds += count

                acc_branch = tree.add(f"👤 [cyan]{acc}[/cyan]")

                acc_branch.add(f"📂 Groups Found: [bold green]{count}[/bold green]")

        except FloodWait as e:
            tree.add(f"[red]{acc} → FloodWait {e.value}s[/red]")
            time.sleep(e.value)

        except Exception as e:
            tree.add(f"[red]Error loading {acc}: {e}[/red]")

    console.print()
    console.print(tree)

    console.print(
        f"\n[yellow]Total DS groups across all accounts:[/yellow] "
        f"[bold green]{total_ds}[/bold green] (^。^)"
    )

    console.input("[magenta]Tap to go back:[/magenta] ")
# =================================================================================== #
