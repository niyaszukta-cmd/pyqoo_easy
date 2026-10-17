"""Pyqoo Easy question bank.

10 sets x 10 questions = 100 questions, each in English and Malayalam.

Every question has:
    id       unique id such as "s3q7"
    set      set number 1 to 10
    prompt   short text shown on screen {"en": ..., "ml": ...}
    say      text read aloud {"en": ..., "ml": ...}
    answer   option id of the right answer
    pool     option ids that can be used as wrong choices
    big      optional large item shown above the choices
    names    True if names must always show under the pictures

Have a native Malayalam speaker (ideally a special educator) proofread the
Malayalam wording before using it with learners.
"""

SETS = [
    {"id": 1, "icon": "🐱", "en": "Animals and birds", "ml": "മൃഗങ്ങളും പക്ഷികളും",
     "cap_en": "Find the animal", "cap_ml": "മൃഗത്തെ കണ്ടെത്താം"},
    {"id": 2, "icon": "🍌", "en": "Fruits and vegetables", "ml": "പഴങ്ങളും പച്ചക്കറികളും",
     "cap_en": "Find the food", "cap_ml": "ഭക്ഷണം കണ്ടെത്താം"},
    {"id": 3, "icon": "🏠", "en": "Words around me", "ml": "ചുറ്റുമുള്ള വാക്കുകൾ",
     "cap_en": "Read the word, tap the picture", "cap_ml": "വാക്ക് വായിച്ച് ചിത്രം തൊടൂ"},
    {"id": 4, "icon": "🎨", "en": "Colours", "ml": "നിറങ്ങൾ",
     "cap_en": "Find the colour", "cap_ml": "നിറം കണ്ടെത്താം"},
    {"id": 5, "icon": "🖐️", "en": "My body", "ml": "എന്റെ ശരീരം",
     "cap_en": "Parts of the body", "cap_ml": "ശരീരഭാഗങ്ങൾ"},
    {"id": 6, "icon": "🔢", "en": "Counting", "ml": "എണ്ണാം",
     "cap_en": "How many are there?", "cap_ml": "എത്ര ഉണ്ട്?"},
    {"id": 7, "icon": "🪙", "en": "Coins and notes", "ml": "നാണയങ്ങളും നോട്ടുകളും",
     "cap_en": "Know your money", "cap_ml": "പണം തിരിച്ചറിയാം"},
    {"id": 8, "icon": "🛒", "en": "Paying", "ml": "പണം കൊടുക്കാം",
     "cap_en": "Pick the coin to pay", "cap_ml": "കൊടുക്കാൻ നാണയം എടുക്കൂ"},
    {"id": 9, "icon": "☀️", "en": "My day", "ml": "എന്റെ ദിവസം",
     "cap_en": "What do we do now?", "cap_ml": "ഇനി എന്ത് ചെയ്യും?"},
    {"id": 10, "icon": "🚌", "en": "Roads and places", "ml": "വഴിയും സ്ഥലങ്ങളും",
     "cap_en": "Where do we go?", "cap_ml": "എവിടെ പോകാം?"},
]

OPTIONS = {}      # option id -> {"glyph", "en", "ml"}
QUESTIONS = []    # list of question dicts


def _add_option(oid, glyph, en, ml):
    OPTIONS[oid] = {"glyph": glyph, "en": en, "ml": ml}


def _add_question(set_id, n, prompt, say, answer, pool, big=None, names=False):
    QUESTIONS.append({
        "id": f"s{set_id}q{n}",
        "set": set_id,
        "prompt": prompt,
        "say": say,
        "answer": answer,
        "pool": [p for p in pool if p != answer],
        "big": big,
        "names": names,
    })


def _noun_set(set_id, items, prompt_en, prompt_ml, say_en, say_ml, show_word=False):
    """Tap-the-picture questions. Returns the option ids so extras can be added."""
    ids = []
    for key, glyph, en, ml in items:
        oid = f"{set_id}:{key}"
        _add_option(oid, glyph, en, ml)
        ids.append(oid)
    for n, (key, glyph, en, ml) in enumerate(items, 1):
        fmt = {"en": en.lower(), "ml": ml}
        _add_question(
            set_id, n,
            {"en": prompt_en.format(**fmt), "ml": prompt_ml.format(**fmt)},
            {"en": say_en.format(**fmt), "ml": say_ml.format(**fmt)},
            f"{set_id}:{key}", ids,
            big={"type": "word"} if show_word else None,
        )
    return ids


# ---------------------------------------------------------------- Set 1
_noun_set(1, [
    ("cat", "🐱", "Cat", "പൂച്ച"),
    ("dog", "🐶", "Dog", "നായ"),
    ("cow", "🐄", "Cow", "പശു"),
    ("elephant", "🐘", "Elephant", "ആന"),
    ("fish", "🐟", "Fish", "മീൻ"),
    ("bird", "🐦", "Bird", "പക്ഷി"),
    ("hen", "🐔", "Hen", "കോഴി"),
    ("goat", "🐐", "Goat", "ആട്"),
    ("monkey", "🐒", "Monkey", "കുരങ്ങ്"),
    ("frog", "🐸", "Frog", "തവള"),
], "Tap the {en}.", "{ml} എവിടെ?", "Tap the {en}.", "{ml}. {ml} എവിടെ? തൊടൂ.")

# ---------------------------------------------------------------- Set 2
_noun_set(2, [
    ("banana", "🍌", "Banana", "വാഴപ്പഴം"),
    ("mango", "🥭", "Mango", "മാങ്ങ"),
    ("apple", "🍎", "Apple", "ആപ്പിൾ"),
    ("coconut", "🥥", "Coconut", "തേങ്ങ"),
    ("orange", "🍊", "Orange", "ഓറഞ്ച്"),
    ("grapes", "🍇", "Grapes", "മുന്തിരി"),
    ("tomato", "🍅", "Tomato", "തക്കാളി"),
    ("carrot", "🥕", "Carrot", "കാരറ്റ്"),
    ("potato", "🥔", "Potato", "ഉരുളക്കിഴങ്ങ്"),
    ("pineapple", "🍍", "Pineapple", "കൈതച്ചക്ക"),
], "Tap the {en}.", "{ml} എവിടെ?", "Tap the {en}.", "{ml}. {ml} എവിടെ? തൊടൂ.")

# ---------------------------------------------------------------- Set 3 (word shown)
_noun_set(3, [
    ("house", "🏠", "House", "വീട്"),
    ("book", "📖", "Book", "പുസ്തകം"),
    ("pencil", "✏️", "Pencil", "പെൻസിൽ"),
    ("bag", "🎒", "Bag", "ബാഗ്"),
    ("chair", "🪑", "Chair", "കസേര"),
    ("bed", "🛏️", "Bed", "കട്ടിൽ"),
    ("clock", "⏰", "Clock", "ക്ലോക്ക്"),
    ("umbrella", "☂️", "Umbrella", "കുട"),
    ("cup", "☕", "Cup", "കപ്പ്"),
    ("key", "🔑", "Key", "താക്കോൽ"),
], "Which picture is this word?", "ഈ വാക്കിന്റെ ചിത്രം ഏതാണ്?",
   "Read the word. Tap the {en}.", "{ml}. {ml} എവിടെ? തൊടൂ.", show_word=True)

# ---------------------------------------------------------------- Set 4 (colours)
_colour_ids = _noun_set(4, [
    ("red", "🔴", "Red", "ചുവപ്പ്"),
    ("blue", "🔵", "Blue", "നീല"),
    ("green", "🟢", "Green", "പച്ച"),
    ("yellow", "🟡", "Yellow", "മഞ്ഞ"),
    ("orange", "🟠", "Orange", "ഓറഞ്ച്"),
    ("purple", "🟣", "Purple", "വയലറ്റ്"),
    ("brown", "🟤", "Brown", "തവിട്ട്"),
    ("black", "⚫", "Black", "കറുപ്പ്"),
    ("white", "⚪", "White", "വെള്ള"),
], "Tap the {en} one.", "{ml} നിറം എവിടെ?", "Tap the {en} one.", "{ml} നിറം എവിടെ? തൊടൂ.")
_add_question(
    4, 10,
    {"en": "What colour is a banana?", "ml": "വാഴപ്പഴത്തിന്റെ നിറം ഏത്?"},
    {"en": "What colour is a banana? Tap the colour.", "ml": "വാഴപ്പഴത്തിന്റെ നിറം ഏത്? തൊടൂ."},
    "4:yellow", _colour_ids, big={"type": "glyph", "glyph": "🍌"},
)

# ---------------------------------------------------------------- Set 5 (body)
_noun_set(5, [
    ("eye", "👁️", "Eye", "കണ്ണ്"),
    ("ear", "👂", "Ear", "ചെവി"),
    ("nose", "👃", "Nose", "മൂക്ക്"),
    ("mouth", "👄", "Mouth", "വായ"),
    ("hand", "✋", "Hand", "കൈ"),
    ("leg", "🦵", "Leg", "കാൽ"),
    ("foot", "🦶", "Foot", "പാദം"),
    ("tooth", "🦷", "Tooth", "പല്ല്"),
    ("tongue", "👅", "Tongue", "നാക്ക്"),
    ("heart", "❤️", "Heart", "ഹൃദയം"),
], "Tap the {en}.", "{ml} എവിടെ?", "Tap the {en}.", "{ml}. {ml} എവിടെ? തൊടൂ.")

# ---------------------------------------------------------------- Set 6 (counting)
_NUM_ML = ["", "ഒന്ന്", "രണ്ട്", "മൂന്ന്", "നാല്", "അഞ്ച്", "ആറ്", "ഏഴ്", "എട്ട്", "ഒമ്പത്", "പത്ത്"]
_COUNT_OBJECTS = ["🍎", "⭐", "🐟", "🎈", "🍌", "🐱", "🌸", "⚽", "🥭", "🐘"]
for _n in range(1, 11):
    _add_option(f"6:{_n}", str(_n), str(_n), _NUM_ML[_n])
for _n in range(1, 11):
    _add_question(
        6, _n,
        {"en": "How many are there?", "ml": "എത്ര ഉണ്ട്?"},
        {"en": "Count the pictures. How many are there?", "ml": "എണ്ണി നോക്കൂ. എത്ര ഉണ്ട്?"},
        f"6:{_n}", [f"6:{k}" for k in range(1, 11)],
        big={"type": "count", "glyph": _COUNT_OBJECTS[_n - 1], "n": _n},
    )

# ---------------------------------------------------------------- Set 7 (coins and notes)
_RS_EN = {1: "one", 2: "two", 5: "five", 10: "ten", 20: "twenty", 50: "fifty",
          100: "one hundred", 200: "two hundred", 500: "five hundred"}
_RS_ML = {1: "ഒരു", 2: "രണ്ട്", 5: "അഞ്ച്", 10: "പത്ത്", 20: "ഇരുപത്", 50: "അമ്പത്",
          100: "നൂറ്", 200: "ഇരുനൂറ്", 500: "അഞ്ഞൂറ്"}
_COINS = [1, 2, 5, 10]
_NOTES = [10, 20, 50, 100, 200, 500]
for _v in _COINS:
    _add_option(f"7:c{_v}", f"🪙 ₹{_v}", f"₹{_v} coin", f"₹{_v} നാണയം")
for _v in _NOTES:
    _add_option(f"7:n{_v}", f"💵 ₹{_v}", f"₹{_v} note", f"₹{_v} നോട്ട്")
_n = 0
for _v in _COINS:
    _n += 1
    _add_question(
        7, _n,
        {"en": f"Tap the ₹{_v} coin.", "ml": f"₹{_v} നാണയം എവിടെ?"},
        {"en": f"Tap the {_RS_EN[_v]} rupee coin.", "ml": f"{_RS_ML[_v]} രൂപ നാണയം എവിടെ? തൊടൂ."},
        f"7:c{_v}", [f"7:c{k}" for k in _COINS],
    )
for _v in _NOTES:
    _n += 1
    _add_question(
        7, _n,
        {"en": f"Tap the ₹{_v} note.", "ml": f"₹{_v} നോട്ട് എവിടെ?"},
        {"en": f"Tap the {_RS_EN[_v]} rupee note.", "ml": f"{_RS_ML[_v]} രൂപ നോട്ട് എവിടെ? തൊടൂ."},
        f"7:n{_v}", [f"7:n{k}" for k in _NOTES],
    )

# ---------------------------------------------------------------- Set 8 (paying)
for _v in _COINS:
    _add_option(f"8:{_v}", f"🪙 ₹{_v}", f"₹{_v} coin", f"₹{_v} നാണയം")
_SHOP = [
    ("🍬", "sweet", "മിഠായി", 1), ("✏️", "pencil", "പെൻസിൽ", 2),
    ("🍌", "banana", "വാഴപ്പഴം", 5), ("☕", "tea", "ചായ", 10),
    ("🎈", "balloon", "ബലൂൺ", 2), ("🍪", "biscuit", "ബിസ്കറ്റ്", 5),
    ("🍦", "ice cream", "ഐസ്ക്രീം", 10), ("🍋", "lemon", "നാരങ്ങ", 1),
    ("🥭", "mango", "മാങ്ങ", 10), ("🍭", "lollipop", "ലോലിപോപ്പ്", 2),
]
for _i, (_g, _en, _ml, _v) in enumerate(_SHOP, 1):
    _add_question(
        8, _i,
        {"en": f"The {_en} costs ₹{_v}. Pick the coin to pay.",
         "ml": f"{_ml} വില ₹{_v}. ഏത് നാണയം കൊടുക്കണം?"},
        {"en": f"The {_en} costs {_RS_EN[_v]} rupees. Tap the coin to pay.",
         "ml": f"{_ml} വില {_RS_ML[_v]} രൂപ. ഏത് നാണയം കൊടുക്കണം?"},
        f"8:{_v}", [f"8:{k}" for k in _COINS],
        big={"type": "price", "glyph": _g, "price": f"₹{_v}"},
    )

# ---------------------------------------------------------------- Set 9 (my day)
_ROUTINE = [
    ("brush", "🪥", "Brush teeth", "പല്ല് തേക്കാം",
     "Good morning! The toothbrush is ready. What do we do?", "സുപ്രഭാതം! ബ്രഷ് തയ്യാർ. നമ്മൾ എന്ത് ചെയ്യും?"),
    ("wash", "🧼", "Wash hands", "കൈ കഴുകാം",
     "The food is ready. What do we do first?", "ഭക്ഷണം തയ്യാറായി. ആദ്യം എന്ത് ചെയ്യണം?"),
    ("eat", "🍚", "Eat", "ഭക്ഷണം കഴിക്കാം",
     "Our hands are clean. What do we do now?", "കൈ വൃത്തിയായി. ഇനി എന്ത് ചെയ്യാം?"),
    ("bath", "🚿", "Take a bath", "കുളിക്കാം",
     "We played in the dust. What do we do?", "കളിച്ച് ദേഹം മുഴുവൻ പൊടി. എന്ത് ചെയ്യണം?"),
    ("school", "🎒", "Go to school", "സ്കൂളിൽ പോകാം",
     "It is a school day. Where do we go?", "ഇന്ന് സ്കൂൾ ഉണ്ട്. എവിടെ പോകണം?"),
    ("sleep", "🛏️", "Sleep", "ഉറങ്ങാം",
     "It is night and the moon is out. What do we do?", "രാത്രിയായി, ചന്ദ്രൻ വന്നു. എന്ത് ചെയ്യണം?"),
    ("play", "⚽", "Play", "കളിക്കാം",
     "School is over and the sun is out. What do we do for fun?", "സ്കൂൾ വിട്ടു, വെയിൽ ഉണ്ട്. രസത്തിന് എന്ത് ചെയ്യാം?"),
    ("drink", "💧", "Drink water", "വെള്ളം കുടിക്കാം",
     "We feel thirsty. What do we do?", "ദാഹിക്കുന്നു. എന്ത് ചെയ്യണം?"),
    ("read", "📖", "Read", "വായിക്കാം",
     "We have a story book in our hands. What do we do?", "കഥാ പുസ്തകം കയ്യിൽ ഉണ്ട്. എന്ത് ചെയ്യാം?"),
    ("dress", "👕", "Wear clothes", "വസ്ത്രം ധരിക്കാം",
     "We are going out. What do we put on?", "പുറത്ത് പോകണം. എന്ത് ധരിക്കണം?"),
]
for _k, _g, _en, _ml, _, _ in _ROUTINE:
    _add_option(f"9:{_k}", _g, _en, _ml)
for _i, (_k, _g, _en, _ml, _cue_en, _cue_ml) in enumerate(_ROUTINE, 1):
    _add_question(
        9, _i,
        {"en": _cue_en, "ml": _cue_ml}, {"en": _cue_en, "ml": _cue_ml},
        f"9:{_k}", [f"9:{r[0]}" for r in _ROUTINE], names=True,
    )

# ---------------------------------------------------------------- Set 10 (roads and places)
_noun_set(10, [
    ("bus", "🚌", "Bus", "ബസ്"),
    ("auto", "🛺", "Auto", "ഓട്ടോ"),
    ("train", "🚆", "Train", "ട്രെയിൻ"),
    ("bicycle", "🚲", "Bicycle", "സൈക്കിൾ"),
    ("boat", "🚤", "Boat", "ബോട്ട്"),
    ("hospital", "🏥", "Hospital", "ആശുപത്രി"),
    ("school", "🏫", "School", "സ്കൂൾ"),
    ("shop", "🏪", "Shop", "കട"),
    ("police", "👮", "Police", "പോലീസ്"),
    ("light", "🚦", "Traffic light", "ട്രാഫിക് ലൈറ്റ്"),
], "Tap the {en}.", "{ml} എവിടെ?", "Tap the {en}.", "{ml}. {ml} എവിടെ? തൊടൂ.")


# ---------------------------------------------------------------- helpers
QUESTION_BY_ID = {q["id"]: q for q in QUESTIONS}
SET_BY_ID = {s["id"]: s for s in SETS}


def questions_for(set_id):
    return [q for q in QUESTIONS if q["set"] == set_id]


# Fail early if the bank is not exactly 10 sets of 10.
assert len(QUESTIONS) == 100, f"expected 100 questions, found {len(QUESTIONS)}"
for _s in SETS:
    assert len(questions_for(_s["id"])) == 10, f"set {_s['id']} does not have 10 questions"
for _q in QUESTIONS:
    assert len(_q["pool"]) >= 3, f"{_q['id']} needs at least 3 wrong choices"
    assert _q["answer"] in OPTIONS and all(p in OPTIONS for p in _q["pool"])
