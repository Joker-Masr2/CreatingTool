from assets.features import *
#### SYSTEM
SYSTEM = platform.system()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
SESS_DIR = os.path.join(BASE_DIR, "sessions")
os.makedirs(SESS_DIR, exist_ok=True)

started_printed = False
start_lock = threading.Lock()
SINGLE_MODE = True
