"""stenoMini 한국어 시스템. KEYS의 순서는 사전 표기 순서입니다."""

KEYS = ("ㅅ-", "ㅁ-", "ㅈ-", "ㄴ-", "ㄷ-", "ㅂ-", "ㄱ-", "ㅎ-", "ㅇ-", "ㄹ-", "ㅗ-", "ㅏ-", "-ㅓ", "-ㅣ", "-*", "-ㅅ", "-ㄹ", "-ㅎ", "-ㅇ", "-ㅁ", "-ㄴ", "-ㅂ", "-ㄱ", "-ㄷ", "-ㅈ", "-ㅆ")
IMPLICIT_HYPHEN_KEYS = ("ㅗ-", "ㅏ-", "-ㅓ", "-ㅣ", "-*")
SUFFIX_KEYS = ()
NUMBER_KEY = None
NUMBERS = {}
UNDO_STROKE_STENO = "*"

ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    "Keyboard": {
        "ㅅ-": "q",
        "ㅁ-": "a",
        "ㅈ-": "w",
        "ㄴ-": "s",
        "ㄷ-": "e",
        "ㅂ-": "d",
        "ㄱ-": "r",
        "ㅎ-": "f",
        "ㅇ-": "t",
        "ㄹ-": "g",
        "ㅗ-": "c",
        "ㅏ-": "v",
        "-ㅓ": "n",
        "-ㅣ": "m",
        "-*": "y",
        "-ㅅ": "h",
        "-ㄹ": "u",
        "-ㅎ": "j",
        "-ㅇ": "i",
        "-ㅁ": "k",
        "-ㄴ": "o",
        "-ㅂ": "l",
        "-ㄱ": "p",
        "-ㄷ": ";",
        "-ㅈ": "[",
        "-ㅆ": "'",
        "arpeggiate": "space",
        "no-op": (),
    }
}

DICTIONARIES_ROOT = "asset:plover_stenoMini:dictionaries"
DEFAULT_DICTIONARIES = ("stenoMini_base.json", "stenoMini_brief.json")
