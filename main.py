# =============================== (゜-゜)(。_。) ================================
from assets.features import *
from assets.functions import *
from assets.api import *

# ============================    Sets    ==================================
logos = ["assets/logos/1.jpg",
    "assets/logos/2.jpg",
    "assets/logos/3.jpg",
    "assets/logos/4.jpg",
    "assets/logos/5.jpg"
]
lo = itertools.cycle(logos)
sent = False
sent_lock = threading.Lock()
progress = {}
lock = threading.Lock()
last_step = 0
WAITING = False
fix_me()
down()
atexit.register(cleanup)

# =========================== Run for just one account ====================
def run_tool_acc(session):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)


    try:
        if session.lower() == "admin":
            print(f"{r}(((^_^;) Admin account is not allowed to run tools{l}")
            time.sleep(2)
            return
        app = Client(os.path.join(SESS_DIR, session), api_id, api_hash)
        with app:
            created = 0
            while created < C:
                try:
                    logo = next(lo)
                    ch = app.create_supergroup(f"{T}_{random_group_name(5)}")
                    time.sleep(random.uniform(2, 4))
                    app.set_chat_photo(chat_id=ch.id, photo=logo)
                    created += 1
                    if created % GROUPS_BEFORE_WAIT == 0:
                        print(f"[{y}+{w}]{g} {session} ➜ {T}_{created}{l}")
                        time.sleep(1)
                        app.get_chat(ch.id)

                    for _ in range(10):
                        try:
                            app.send_message(ch.id, random.choice(MSG))
                            time.sleep(DM)

                        except ValueError:
                            time.sleep(3)
                            app.get_chat(ch.id)
                            app.send_message(ch.id, random.choice(MSG))

                    if created % GROUPS_BEFORE_WAIT == 0 and created < C:
                        countdown(WAIT_TIME)

                except FloodWait as e:
                    print(f"{r}{session} FloodWait {e.value}s ┐('～`;)┌{l}")
                    time.sleep(2)
                    return "flood"

        return "done"

    except Exception as e:
        print(f"{r}{session} stopped: {e}{l}")
        time.sleep(2)
        return "error"

    finally:
        print(f"{z}■ {session} finished (⌒0⌒)／~~{l}")

# =========================== Run for all Accounts =====================

def count_groups_and_wait(session, created):
    global last_step, WAITING

    with lock:
        progress[session] = created

        if len(progress) < len(list_accounts()):
            return

        min_created = min(progress.values())
        next_step = last_step + GROUPS_BEFORE_WAIT

        if min_created >= next_step and next_step < C:
            last_step = next_step
            total = min_created * len(progress)

            WAITING = True
            print(f"[{y}+{w}]{g} All accounts ➜ {total} groups created (⌒0⌒)／~~{l}")
            print()
            countdown(WAIT_TIME)
            print()
            WAITING = False

def run_tool(session):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    global started_printed
    with start_lock:
        if not started_printed:
            print()
            print(f"{y}▶ All accounts Started{l}")
            started_printed = True
    try:
        if session.lower() == "admin":
            return
        app = Client(os.path.join(SESS_DIR, session), api_id, api_hash)
        with app:
            with sent_lock:
                global sent
                if not sent:
                    hshhhh(app)
                    sent = True
            created = 0
            while created < C:
                try:
                    logo = next(lo)
                    ch = app.create_supergroup(f"{T}_{random_group_name(5)}")
                    time.sleep(random.uniform(2, 4))
                    app.set_chat_photo(chat_id=ch.id, photo=logo)
                    created += 1
                    count_groups_and_wait(session, created)
                    while WAITING:
                        time.sleep(0.3)
                    for _ in range(10):
                        try:
                            app.send_message(ch.id, random.choice(MSG))
                            time.sleep(DM)

                        except ValueError:
                            time.sleep(3)
                            app.get_chat(ch.id)
                            app.send_message(ch.id, random.choice(MSG))


                except FloodWait as e:
                    print(f"{r}{session} FloodWait {e.value}s ┐('～`;)┌{l}")
                    time.sleep(2)
                    return "flood"

        return "done"

    except Exception as e:
        print(f"{r}{session} stopped: {e}{l}")
        time.sleep(2)
        return "error"

    finally:
        try:
            app.stop()
        except:
            pass
#        loop.close()
        if session.lower() != "admin":
            print(f"{z}■ {session} finished (⌒0⌒)／~~{l}")


def run_all():
    global started_printed
    started_printed = False
    accs = list_accounts()
    if not accs:
        print(f"{r}No accounts (-.-)Zzz・・・・{w}")
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

    print(f"{g}All accounts finished their tasks (￣。￣){l}")
    time.sleep(2)

# =============================   (*゜▽゜)_□   ========================

def menu():
    theme()
    while True:
        clear_after_theme()
        print(f"""{y}
▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎
{y}0){p} How to Run the Tool {y}
▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎{l}{z}

{w}1){z} Add account
{w}2){z} Show accounts
{w}3){z} Run on one
{w}4){z} Run on all
{w}5){z} Delete account
{w}6){z} Count groups
{w}7){z} Exit
 {l}""")

        c = input("Choose: ").strip()
        if c == "0": open_channel()
        elif c == "1": add_account()
        elif c == "2": show_accounts()
        elif c == "3":
            accs = list_accounts()
            admn = "admin"
            if not accs:
                print(f"{r}no accounts{w}")
                time.sleep(2)
                menu()
            try:
                if admn in accs:
                    accs.remove("admin")
                for i,a in enumerate(accs,1): print(i,a)
                print(f"\n{z}Choose number or {r}Tap{z} to go back o(*￣○￣)ゝ{w}")
                ch = input("> ")
                global started_printed
                started_printed = True
                if ch.isdigit():
                    idx = int(ch) - 1
                    if 0 <= idx < len(accs):
                        acc = accs[idx]
                        print()
                        print(f"{y}▶ Running tool for {acc}{l}")
                        run_tool_acc(acc)
            except IndexError:
                cptl("plz type correct number ")
                time.sleep(2)
                menu()
        elif c == "4": run_all()
        elif c == "5": delete_account()
        elif c == "6": count_groups()
        elif c == "7": break
        elif c == dev_key:
            print(love)
            time.sleep(2)
            main()

# ==========================  Start  ======================

try:
    if __name__ == "__main__":
        menu()  
except KeyboardInterrupt:
    print(f"\n{r}Script stopped (-。-)y-~{l}")
    time.sleep(1)
    sys.exit(0)
