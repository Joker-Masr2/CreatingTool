# Imports
from assets.features import *
from assets.config import *
from system import *
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
    print(f"\r{g} Resuming work...  {w}      ")
#############
fix_me() ###########
#### RUN TOOL
progress = {}
lock = threading.Lock()
last_step = 0
def count_groups_and_wait(session, created):
    global last_step

    with lock:
        progress[session] = created

        if len(progress) < len(list_accounts()):
            return

        min_created = min(progress.values())
        next_step = last_step + GROUPS_BEFORE_WAIT

        if min_created >= next_step and next_step < C:
            last_step = next_step
            total = min_created * len(progress)
            print(f"[{y}+{w}]{g} All accounts ➜ {total} groups created{l}")
            print()
            countdown(WAIT_TIME)
            print()

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
        app = Client(os.path.join(SESS_DIR, session), api_id, api_hash)
        with app:
            created = 0
            while created < C:
                try:
                    ch = app.create_supergroup(f"{T}_{created+1}")
                    created += 1
                    if SINGLE_MODE and created % GROUPS_BEFORE_WAIT == 0 and created < C:
                        print(f"[{y}+{w}]{g} {created} groups created{l}")
                        print()
                        countdown(WAIT_TIME)
                        print()
                    count_groups_and_wait(session, created)

                    for _ in range(10):
                        try:
                            app.send_message(ch.id, random.choice(MSG))
                            time.sleep(DM)

                        except ValueError:
                            time.sleep(3)
                            app.get_chat(ch.id)
                            app.send_message(ch.id, random.choice(MSG))


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
        #loop.close()
        print(f"{z}■ {session} finished{l}")

## run all
def run_all():
    SINGLE_MODE = False
    global started_printed
    started_printed = False
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

## Menu
def menu():
    theme()
    while True:
        clear_after_theme()
        print(f"""
1){z} Add account {w}
2){z} Show accounts {w}
3){z} Run on one {w}
4){z} Run on all {w}
5){z} Delete account {w}
6){z} Count groups {w}
7){z} Exit {w}
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
                global started_printed
                started_printed = True
                if ch.isdigit():
                    idx = int(ch) - 1
                    if 0 <= idx < len(accs):
                        acc = accs[idx]
                        print()
                        print(f"{y}▶ Running tool for {acc}{l}")
                        SINGLE_MODE = True
                        run_tool(acc)
            except IndexError:
                cptl("plz type correct number ")
                time.sleep(2)
                menu()
        elif c == "4": run_all()
        elif c == "5": delete_account()
        elif c == "6": count_groups()
        elif c == "7": break
#### START
try:
    if __name__ == "__main__":
        menu()
except KeyboardInterrupt:
    print(f"\n{r}Script stopped safely{l}")
    time.sleep(1)
    sys.exit(0)
