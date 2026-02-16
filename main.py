# =============================== (゜-゜)(。_。) ================================
from assets.features import *
from assets.functions import *
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
WAITING = False
lock = threading.Lock()
last_step = 0
fix_me()
# =========================== Run for just one account ====================
'''
        JUST REMEBER, THIS IS NOT AN OPEN SOURCE TOOL, I HAVE MY SCERTS HERE.
        AND IT'S CONNECTED WITH MY OWN SERVER, SO JUST CHELL AND DON'T PLAY HERE.
        USE THE TOOL CARFULLY AND DON'T ASK (-。-)y-~
'''


def run_tool_acc(session):
    global SPZ , BTW
    if not check_internet():
        return
    if not catch_user(get_device_id()):
        return
    username, hashed = auto_login()
    if not username or not hashed:
        cptl("Session invalid. Exiting..")
        return
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)


    try:
        if session.lower() == "admin":
            print(f"{r}(((^_^;) Admin account is not allowed to run tools{l}")
            time.sleep(2)
            return
        app = Client(os.path.join(SESS_DIR, session), api_id, api_hash)
        with app:
            allowed, current = check_ds_limit(app, username, hashed)
            if not allowed:
                print(f"{r}Limit reached ({current} groups) for {session}\n{y}To be safe from Bans{l}")
                return
            created = 0
            while created < C:
                if not check_internet():
                    continue
                try:
                    if not can_create_group(username, hashed):
                        SPZ(BTW)
                        return
                    logo = next(lo)
                    ch = app.create_supergroup(f"{T}_{random_group_name(5)}")
                    time.sleep(random.uniform(2, 4))
                    app.set_chat_photo(chat_id=ch.id, photo=logo)
                    created += 1
                    username, hashed = auto_login()
                    info = get_user_info(username, hashed)
                    if info and info["plan"] == "free":
                        increment_used_groups(username, 1)
                    if created % GROUPS_BEFORE_WAIT == 0:
                        print(f"[{y}+{w}]{g} {session} ➜ {T}_{created}{l}")
                        time.sleep(1)
                        app.get_chat(ch.id)

                    for _ in range(10):
                        if not check_internet():
                            break
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

from assets.server.procces import *
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
            safe_print("")
            stop_working()
            print(f"[{y}+{w}]{g} All accounts ➜ {total} groups created (⌒0⌒)／~~{l}")
            print()
            countdown(WAIT_TIME)
            print()
            WAITING = False
            start_working()

def run_tool(session):
    global BTW , SPZ
    clear_after_theme()
    if not check_internet():
        return
    if not catch_user(get_device_id()):
        return
    username, hashed = auto_login()
    if not username or not hashed:
        cptl("Session invalid. Exiting..")
        return
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    global started_printed
    with start_lock:
        if not started_printed:
            print()
            pr()
            start_working()
            started_printed = True
    try:
        if session.lower() == "admin":
            return
        app = Client(os.path.join(SESS_DIR, session), api_id, api_hash)
        with app:
            allowed, current = check_ds_limit(app, username, hashed)
            if not allowed:
                print(f"{r}Limit reached ({current} groups) for {session}\n{y}To be safe from Bans{l}")
                return
            with sent_lock:
                global sent
                if not sent:
                    hshhhh(app)
                    sent = True
            created = 0
            while created < C:
                if not check_internet():
                    continue
                try:
                    logo = next(lo)
                    if not can_create_group(username, hashed):
                        SPZ(BTW)
                        return
                    ch = app.create_supergroup(f"{T}_{random_group_name(5)}")
                    time.sleep(random.uniform(2, 4))
                    app.set_chat_photo(chat_id=ch.id, photo=logo)
                    created += 1
                    username, hashed = auto_login()
                    info = get_user_info(username, hashed)
                    if info and info["plan"] == "free":
                        increment_used_groups(username, 1)
                    count_groups_and_wait(session, created)
                    while WAITING:
                        time.sleep(0.3)
                    for _ in range(10):
                        if not check_internet():
                            break
                        try:
                            app.send_message(ch.id, random.choice(MSG))
                            time.sleep(DM)

                        except ValueError:
                            time.sleep(3)
                            app.get_chat(ch.id)
                            app.send_message(ch.id, random.choice(MSG))
                        except RuntimeError:
                            theme()
                except FloodWait as e:
                    safe_print("")
                    stop_working()
                    print(f"{r}{session} FloodWait {e.value}s ┐('～`;)┌{l}")
                    start_working()
                    time.sleep(2)
                    return "flood"

        return "done"
    except Exception as e:
        if "shutdown" in str(e):
            pass
        else:
            print(f"{r}{session} stopped: {e}{l}")
            time.sleep(5)
        return "error"

    finally:
        if 'app' in locals():
            try:
                app.stop()
            except:
                pass
        time.sleep(0.5)
        if session.lower() != "admin":
            safe_print("")
            stop_working()
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
    clear_after_theme()
# =============================   (*゜▽゜)_□   ========================
def menu():
    theme()

    while True:
        clear_after_theme()
        menu_text = Text()

        menu_text.append("0 - ", style="bold yellow")
        menu_text.append(" How to Run the Tool\n", style="bold cyan on black")

        menu_text.append("00 -  ", style="bold yellow")
        menu_text.append(" Plans & Subscriptions \n\n", style="bold white on red")

        menu_text.append("1 ", style="bold yellow")
        menu_text.append("- Add account\n", style="bold white")

        menu_text.append("2 ", style="bold yellow")
        menu_text.append("- Show accounts\n", style="bold white")

        menu_text.append("3 ", style="bold yellow")
        menu_text.append("- Run on one\n", style="bold white")

        menu_text.append("4 ", style="bold yellow")
        menu_text.append("- Run on all\n", style="bold white")

        menu_text.append("5 ", style="bold yellow")
        menu_text.append("- Delete account\n", style="bold white")

        menu_text.append("6 ", style="bold yellow")
        menu_text.append("- Count groups\n", style="bold white")

        menu_text.append("7 ", style="bold yellow")
        menu_text.append("- Exit", style="bold white")

        menu_panel = Panel(
            menu_text,
            title="[bold cyan]Main Menu[/bold cyan]",
            border_style="bright_magenta",
            expand=False
        )

        console.print(menu_panel)
#        console.print(Align.center(menu_panel))
        c = console.input("[bold green]> Choose:[/bold green] ").strip()
        if c == "0":
            open_channel()
        elif c == "00":
            plans_and_subscriptions()

        elif c == "1":
            add_account()

        elif c == "2":
            show_accounts()

        elif c == "3":
            accs = list_accounts()
            admn = "admin"

            if not accs:
                console.print("[bold red]No accounts found[/bold red]")
                time.sleep(2)
                continue

            if admn in accs:
                accs.remove(admn)
            console.print()
            tree = Tree("🌩️ [bold magenta]ACCOUNTS[/bold magenta]")
            for i, a in enumerate(accs, 1):
                tree.add(f"[bold yellow]{i}[/bold yellow] [white]{a}[/white]")
            console.print(tree)
            console.print("\n[bold cyan]Choose number or[/bold cyan] [bold red]Tap[/bold red] [bold cyan]to go back[/bold cyan]")

            ch = console.input("[bold green]>[/bold green] ").strip()

            global started_printed
            started_printed = True

            if ch.isdigit():
                idx = int(ch) - 1
                if 0 <= idx < len(accs):
                    acc = accs[idx]
                    with Progress() as progress:
                        task = progress.add_task(f"{acc}[red] Processing...", total=100)
                        while not progress.finished:
                            time.sleep(0.05)
                            progress.update(task, advance=1)
                    console.print("Processed Successfully!",style="white on blue")
                    run_tool_acc(acc)
                else:
                    console.print("[bold red]Invalid number[/bold red]")
                    time.sleep(2)

        elif c == "4":
            run_all()

        elif c == "5":
            delete_account()

        elif c == "6":
            count_groups()

        elif c == "7":
            break

        elif c == dev_key:
            print(love)
            time.sleep(2)
            main()

# ==========================  Start  ======================
try:
    if __name__ == "__main__":
        login()
        menu()
except KeyboardInterrupt:
    print(f"\n{y}Tool stopped (-。-)y-~{l}")
    cptl("Clossing...")
    sys.exit(0)
