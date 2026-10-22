# Pyqoo Easy: gentle, picture-first learning support (English + Malayalam). SINGLE FILE: app.py + requirements.txt
import hashlib as _hl
import os as _os
import sys as _sys
import types as _types

_SOURCES = {}
_SOURCES['items_a'] = r'''
# Picture word banks, part A.  Each line: emoji|English|Malayalam (spoken, everyday word)
A = {}

A["animals"] = """
🐶|Dog|പട്ടി
🐱|Cat|പൂച്ച
🐄|Cow|പശു
🐐|Goat|ആട്
🐘|Elephant|ആന
🐅|Tiger|കടുവ
🦁|Lion|സിംഹം
🐒|Monkey|കുരങ്ങ്
🐴|Horse|കുതിര
🐑|Sheep|ചെമ്മരിയാട്
🐇|Rabbit|മുയൽ
🐭|Mouse|എലി
🐍|Snake|പാമ്പ്
🐸|Frog|തവള
🐢|Turtle|ആമ
🐟|Fish|മീൻ
🐃|Buffalo|എരുമ
🐖|Pig|പന്നി
🦌|Deer|മാൻ
🐻|Bear|കരടി
🐊|Crocodile|മുതല
🦒|Giraffe|ജിറാഫ്
🐫|Camel|ഒട്ടകം
🐿️|Squirrel|അണ്ണാൻ
"""

A["birds"] = """
🐔|Hen|കോഴി
🦆|Duck|താറാവ്
🦜|Parrot|തത്ത
🦚|Peacock|മയിൽ
🦅|Eagle|പരുന്ത്
🦉|Owl|മൂങ്ങ
🐦|Bird|കിളി
🕊️|Dove|പ്രാവ്
🐝|Bee|തേനീച്ച
🦋|Butterfly|ചിത്രശലഭം
🐜|Ant|ഉറുമ്പ്
🐛|Caterpillar|പുഴു
🐌|Snail|ഒച്ച്
🕷️|Spider|ചിലന്തി
🦟|Mosquito|കൊതുക്
🦀|Crab|ഞണ്ട്
🐙|Octopus|നീരാളി
🐬|Dolphin|ഡോൾഫിൻ
🐳|Whale|തിമിംഗലം
"""

A["fruits"] = """
🍎|Apple|ആപ്പിൾ
🍌|Banana|പഴം
🥭|Mango|മാങ്ങ
🍊|Orange|ഓറഞ്ച്
🍇|Grapes|മുന്തിരി
🍉|Watermelon|തണ്ണിമത്തൻ
🍍|Pineapple|കൈതച്ചക്ക
🥥|Coconut|തേങ്ങ
🍋|Lemon|നാരങ്ങ
🍓|Strawberry|സ്ട്രോബെറി
🍐|Pear|പിയർ
🍑|Peach|പീച്ച്
🍒|Cherry|ചെറി
🥝|Kiwi|കിവി
"""

A["vegetables"] = """
🥕|Carrot|കാരറ്റ്
🥔|Potato|ഉരുളക്കിഴങ്ങ്
🍅|Tomato|തക്കാളി
🧅|Onion|ഉള്ളി
🍆|Brinjal|വഴുതനങ്ങ
🌽|Corn|ചോളം
🥒|Cucumber|വെള്ളരിക്ക
🥦|Broccoli|ബ്രോക്കോളി
🌶️|Chilli|മുളക്
🧄|Garlic|വെളുത്തുള്ളി
🍄|Mushroom|കൂൺ
🥬|Leafy greens|ഇലക്കറി
🫑|Capsicum|കാപ്സിക്കം
🥜|Groundnut|കപ്പലണ്ടി
"""

A["food"] = """
🍚|Rice|ചോറ്
🍞|Bread|ബ്രെഡ്
🥛|Milk|പാല്
🥚|Egg|മുട്ട
🍕|Pizza|പിസ്സ
🍔|Burger|ബർഗർ
🍪|Biscuit|ബിസ്കറ്റ്
🍫|Chocolate|ചോക്ലേറ്റ്
🍦|Ice cream|ഐസ്ക്രീം
🎂|Cake|കേക്ക്
🍬|Sweet|മിഠായി
🍯|Honey|തേൻ
🧀|Cheese|ചീസ്
🍜|Noodles|നൂഡിൽസ്
🫓|Chapathi|ചപ്പാത്തി
🍲|Curry|കറി
🍟|Chips|ചിപ്സ്
🧃|Juice|ജ്യൂസ്
☕|Tea|ചായ
💧|Water|വെള്ളം
"""

A["colours"] = """
🔴|Red|ചുവപ്പ്
🔵|Blue|നീല
🟢|Green|പച്ച
🟡|Yellow|മഞ്ഞ
🟠|Orange colour|ഓറഞ്ച്
🟣|Purple|വയലറ്റ്
🟤|Brown|തവിട്ട്
⚫|Black|കറുപ്പ്
⚪|White|വെള്ള
🩷|Pink|പിങ്ക്
"""

A["shapes"] = """
⭕|Circle|വൃത്തം
🟦|Square|ചതുരം
🔺|Triangle|ത്രികോണം
⭐|Star|നക്ഷത്രം
❤️|Heart|ഹൃദയം
🔶|Diamond|ഡയമണ്ട്
"""
'''

_SOURCES['items_b'] = r'''
# Picture word banks, part B.  emoji|English|Malayalam
B = {}

B["body"] = """
👁️|Eye|കണ്ണ്
👃|Nose|മൂക്ക്
👄|Mouth|വായ
👂|Ear|ചെവി
✋|Hand|കൈ
🦶|Foot|കാല്
🦷|Tooth|പല്ല്
👅|Tongue|നാക്ക്
🦴|Bone|എല്ല്
🧠|Brain|തലച്ചോറ്
"""

B["people"] = """
👩|Mother|അമ്മ
👨|Father|അച്ഛൻ
👧|Girl|പെൺകുട്ടി
👦|Boy|ആൺകുട്ടി
👵|Grandmother|അമ്മൂമ്മ
👴|Grandfather|അപ്പൂപ്പൻ
👶|Baby|കുഞ്ഞ്
"""

B["helpers"] = """
👮|Police officer|പോലീസ്
👩‍⚕️|Doctor|ഡോക്ടർ
👩‍🏫|Teacher|ടീച്ചർ
👨‍🍳|Cook|പാചകക്കാരൻ
👨‍🌾|Farmer|കർഷകൻ
🧑‍🚒|Fire fighter|ഫയർമാൻ
👨‍✈️|Pilot|പൈലറ്റ്
🧑‍🔧|Mechanic|മെക്കാനിക്
👷|Builder|പണിക്കാരൻ
🧑‍🎓|Student|വിദ്യാർത്ഥി
"""

B["clothes"] = """
👕|Shirt|ഷർട്ട്
👖|Pants|പാന്റ്
👗|Dress|ഉടുപ്പ്
👟|Shoe|ഷൂ
🧦|Socks|സോക്സ്
🧢|Cap|തൊപ്പി
🧥|Coat|കോട്ട്
👓|Glasses|കണ്ണട
🎒|Bag|ബാഗ്
☂️|Umbrella|കുട
🩴|Slippers|ചെരുപ്പ്
"""

B["home"] = """
🛏️|Bed|കട്ടിൽ
🪑|Chair|കസേര
🚪|Door|വാതിൽ
🪟|Window|ജനൽ
🛋️|Sofa|സോഫ
🪥|Toothbrush|ബ്രഷ്
🧼|Soap|സോപ്പ്
🍽️|Plate|പ്ലേറ്റ്
🥄|Spoon|സ്പൂൺ
🔑|Key|താക്കോൽ
💡|Light bulb|ബൾബ്
📺|TV|ടിവി
🕰️|Clock|ക്ലോക്ക്
🪞|Mirror|കണ്ണാടി
🧹|Broom|ചൂല്
📱|Phone|ഫോൺ
🪣|Bucket|ബക്കറ്റ്
🔦|Torch|ടോർച്ച്
"""

B["school"] = """
✏️|Pencil|പെൻസിൽ
📖|Book|പുസ്തകം
🖊️|Pen|പേന
📏|Ruler|സ്കെയിൽ
✂️|Scissors|കത്രിക
🖍️|Crayon|ക്രയോൺ
📓|Notebook|നോട്ടുബുക്ക്
🏫|School|സ്കൂൾ
🌍|Globe|ഭൂഗോളം
🔔|Bell|മണി
"""

B["vehicles"] = """
🚗|Car|കാർ
🚌|Bus|ബസ്
🚲|Cycle|സൈക്കിൾ
🏍️|Bike|ബൈക്ക്
🚂|Train|ട്രെയിൻ
✈️|Aeroplane|വിമാനം
🚢|Ship|കപ്പൽ
🚁|Helicopter|ഹെലികോപ്റ്റർ
🛺|Auto|ഓട്ടോ
🚑|Ambulance|ആംബുലൻസ്
🚒|Fire engine|ഫയർ എഞ്ചിൻ
🚜|Tractor|ട്രാക്ടർ
🛶|Boat|വള്ളം
🚚|Lorry|ലോറി
"""

B["nature"] = """
☀️|Sun|സൂര്യൻ
🌙|Moon|ചന്ദ്രൻ
☁️|Cloud|മേഘം
🌧️|Rain|മഴ
🌈|Rainbow|മഴവില്ല്
🌳|Tree|മരം
🌸|Flower|പൂവ്
🔥|Fire|തീ
💨|Wind|കാറ്റ്
⛰️|Mountain|മല
🌊|Wave|തിര
🌴|Coconut tree|തെങ്ങ്
🍃|Leaf|ഇല
⚡|Lightning|ഇടിമിന്നൽ
"""

B["places"] = """
🏠|House|വീട്
🏥|Hospital|ആശുപത്രി
🏪|Shop|കട
🛕|Temple|അമ്പലം
⛪|Church|ചർച്ച്
🕌|Mosque|മസ്ജിദ്
🏦|Bank|ബാങ്ക്
🌳|Park|പാർക്ക്
⛽|Petrol pump|പെട്രോൾ പമ്പ്
🚉|Railway station|റെയിൽവേ സ്റ്റേഷൻ
🏨|Hotel|ഹോട്ടൽ
🌾|Paddy field|പാടം
🏖️|Beach|കടപ്പുറം
"""

B["feelings"] = """
😀|Happy|സന്തോഷം
😢|Sad|സങ്കടം
😡|Angry|ദേഷ്യം
😨|Scared|പേടി
😴|Sleepy|ഉറക്കം
😲|Surprised|അത്ഭുതം
🤒|Sick|സുഖമില്ല
🥱|Tired|ക്ഷീണം
"""

B["actions"] = """
🏃|Running|ഓടുന്നു
🚶|Walking|നടക്കുന്നു
🛌|Sleeping|ഉറങ്ങുന്നു
🏊|Swimming|നീന്തുന്നു
🚴|Cycling|സൈക്കിൾ ചവിട്ടുന്നു
💃|Dancing|ഡാൻസ് ചെയ്യുന്നു
🎤|Singing|പാടുന്നു
📖|Reading|വായിക്കുന്നു
✍️|Writing|എഴുതുന്നു
🛁|Bathing|കുളിക്കുന്നു
🍴|Eating|കഴിക്കുന്നു
🥤|Drinking|കുടിക്കുന്നു
"""
'''

_SOURCES['items_c'] = r'''
# Picture word banks, part C: letters, plus life-skill and sign banks.
C = {}

# English letters: letter|picture emoji|word   (format: emoji|English word|Malayalam word, key = letter)
C["abc"] = """
🍎|Apple|ആപ്പിൾ|A
⚽|Ball|പന്ത്|B
🐱|Cat|പൂച്ച|C
🐶|Dog|പട്ടി|D
🥚|Egg|മുട്ട|E
🐟|Fish|മീൻ|F
🐐|Goat|ആട്|G
🐔|Hen|കോഴി|H
🍦|Ice cream|ഐസ്ക്രീം|I
🧃|Juice|ജ്യൂസ്|J
🪁|Kite|പട്ടം|K
🦁|Lion|സിംഹം|L
🥭|Mango|മാങ്ങ|M
🪺|Nest|കൂട്|N
🍊|Orange|ഓറഞ്ച്|O
🦜|Parrot|തത്ത|P
👸|Queen|റാണി|Q
🐇|Rabbit|മുയൽ|R
☀️|Sun|സൂര്യൻ|S
🌳|Tree|മരം|T
☂️|Umbrella|കുട|U
🎻|Violin|വയലിൻ|V
⌚|Watch|വാച്ച്|W
🎹|Xylophone|സൈലോഫോൺ|X
🪀|Yo-yo|യോ-യോ|Y
🦓|Zebra|സീബ്ര|Z
"""

# Malayalam letters: emoji|English word|Malayalam word|letter
C["mal"] = """
👩|Mother|അമ്മ|അ
🐘|Elephant|ആന|ആ
🍃|Leaf|ഇല|ഇ
🐜|Ant|ഉറുമ്പ്|ഉ
🐭|Mouse|എലി|എ
🐫|Camel|ഒട്ടകം|ഒ
🐅|Tiger|കടുവ|ക
🦜|Parrot|തത്ത|ത
🦚|Peacock|മയിൽ|മ
🐄|Cow|പശു|പ
🏠|House|വീട്|വ
"""
'''

_SOURCES['life_a'] = r'''
# Hand-written life-skill questions, part A: safety, signs, daily routine.
# Each question: (big_emoji, English question, Malayalam question, [(emoji, English, Malayalam) x3-4], right_index, English why, Malayalam why)
LIFE_A = {}

LIFE_A["safety"] = [
    ("🚦", "The traffic light is red. What do we do?", "സിഗ്നൽ ചുവപ്പാണ്. നമ്മൾ എന്ത് ചെയ്യണം?",
     [("✋", "Stop", "നിൽക്കണം"), ("🏃", "Run", "ഓടണം"), ("🚶", "Walk fast", "വേഗം നടക്കണം")], 0, "Red means stop.", "ചുവപ്പ് കണ്ടാൽ നിൽക്കണം."),
    ("🚦", "The light is green. What do we do?", "സിഗ്നൽ പച്ചയാണ്. എന്ത് ചെയ്യാം?",
     [("🚶", "Go, after looking both sides", "ഇരുവശവും നോക്കി പോകാം"), ("✋", "Stop forever", "ഒരിക്കലും പോകരുത്"), ("🛌", "Sleep", "ഉറങ്ങാം")], 0, "Green means go, but look both ways first.", "പച്ച കണ്ടാൽ പോകാം, പക്ഷേ ആദ്യം ഇരുവശവും നോക്കണം."),
    ("🛣️", "Where do we cross the road?", "റോഡ് എവിടെ വച്ചാണ് മുറിച്ചുകടക്കേണ്ടത്?",
     [("🚸", "At the zebra crossing", "സീബ്ര ക്രോസിങ്ങിൽ"), ("🚗", "Between cars", "വണ്ടികൾക്കിടയിൽ കൂടി"), ("🌀", "At a bend", "വളവിൽ വച്ച്")], 0, "The zebra crossing is the safe place.", "സീബ്ര ക്രോസിങ്ങാണ് സുരക്ഷിതമായ സ്ഥലം."),
    ("🔥", "Who can touch the fire in the kitchen?", "അടുക്കളയിലെ തീയിൽ ആർക്കാണ് തൊടാൻ പറ്റുക?",
     [("🧒", "Me", "ഞാൻ"), ("👩", "A grown-up", "വലിയവർ"), ("🐶", "The dog", "പട്ടി")], 1, "Only grown-ups handle fire. It burns.", "തീ വലിയവർ മാത്രമേ തൊടാവൂ. അത് പൊള്ളും."),
    ("💊", "You find some tablets on the table. What do you do?", "മേശപ്പുറത്ത് കുറച്ച് ഗുളികകൾ കണ്ടു. എന്ത് ചെയ്യും?",
     [("😋", "Eat them", "കഴിക്കും"), ("👩", "Tell a grown-up", "വലിയവരോട് പറയും"), ("🗑️", "Throw them", "കളയും")], 1, "Never eat medicine on your own. Tell a grown-up.", "ഗുളിക തനിയെ കഴിക്കരുത്. വലിയവരോട് പറയണം."),
    ("🧑‍🦱", "A stranger offers you sweets and says come with me. What do you do?", "അറിയാത്ത ഒരാൾ മിഠായി തന്ന് കൂടെ വരാൻ പറഞ്ഞു. എന്ത് ചെയ്യും?",
     [("🚶", "Go with him", "കൂടെ പോകും"), ("🏃", "Say no, go to a trusted grown-up", "വേണ്ടെന്ന് പറഞ്ഞ് വീട്ടുകാരുടെ അടുത്തേക്ക് പോകും"), ("🍬", "Take the sweet", "മിഠായി വാങ്ങും")], 1, "Say no and go to someone you trust.", "വേണ്ടെന്ന് പറഞ്ഞ് വിശ്വാസമുള്ളവരുടെ അടുത്തേക്ക് പോകണം."),
    ("🌊", "You are near deep water. What is safe?", "ആഴമുള്ള വെള്ളത്തിന്റെ അടുത്താണ്. എന്താണ് സുരക്ഷിതം?",
     [("🏊", "Jump in alone", "തനിയെ ചാടും"), ("👨‍👩‍👧", "Stay with a grown-up", "വലിയവരുടെ കൂടെ നിൽക്കും"), ("🏃", "Run on the edge", "അരികിൽ കൂടി ഓടും")], 1, "Stay with a grown-up near water.", "വെള്ളത്തിനടുത്ത് വലിയവരുടെ കൂടെ നിൽക്കണം."),
    ("🔌", "You see a plug socket. What do you do?", "ഒരു പ്ലഗ് സോക്കറ്റ് കണ്ടു. എന്ത് ചെയ്യും?",
     [("☝️", "Poke it with a finger", "വിരൽ ഇടും"), ("🙅", "Do not touch it", "തൊടില്ല"), ("🔧", "Put a key in", "താക്കോൽ ഇടും")], 1, "Electricity is dangerous. Do not touch sockets.", "കറന്റ് അപകടമാണ്. സോക്കറ്റിൽ തൊടരുത്."),
    ("🚗", "In a car, what do we wear?", "കാറിൽ പോകുമ്പോൾ എന്താണ് ധരിക്കേണ്ടത്?",
     [("💺", "Seat belt", "സീറ്റ് ബെൽറ്റ്"), ("🧢", "A cap", "തൊപ്പി"), ("🧤", "Gloves", "കയ്യുറ")], 0, "A seat belt keeps us safe.", "സീറ്റ് ബെൽറ്റ് നമ്മളെ സുരക്ഷിതരാക്കും."),
    ("🏍️", "On a bike, what must we wear on the head?", "ബൈക്കിൽ പോകുമ്പോൾ തലയിൽ എന്ത് വയ്ക്കണം?",
     [("🪖", "Helmet", "ഹെൽമെറ്റ്"), ("🧢", "Cap", "തൊപ്പി"), ("👓", "Glasses", "കണ്ണട")], 0, "A helmet protects the head.", "ഹെൽമെറ്റ് തലയെ സംരക്ഷിക്കും."),
    ("😰", "You are lost in a shop. What do you do?", "കടയിൽ വച്ച് വഴി തെറ്റി. എന്ത് ചെയ്യും?",
     [("🏃", "Run outside", "പുറത്തേക്ക് ഓടും"), ("🧍", "Stay and ask a shop worker for help", "അവിടെത്തന്നെ നിന്ന് കടയിലെ ആളോട് സഹായം ചോദിക്കും"), ("😭", "Hide", "ഒളിച്ചിരിക്കും")], 1, "Stay still and ask a helper for help.", "അവിടെത്തന്നെ നിന്ന് സഹായം ചോദിക്കണം."),
    ("📞", "Which number do we call for an ambulance in India?", "ആംബുലൻസിന് ഏത് നമ്പറിലാണ് വിളിക്കേണ്ടത്?",
     [("1️⃣", "108", "108"), ("2️⃣", "420", "420"), ("3️⃣", "555", "555")], 0, "108 is the ambulance number.", "ആംബുലൻസിന്റെ നമ്പർ 108 ആണ്."),
    ("🔪", "A knife is on the table. Who should use it?", "മേശപ്പുറത്ത് ഒരു കത്തിയുണ്ട്. ആരാണ് ഉപയോഗിക്കേണ്ടത്?",
     [("👶", "Baby", "കുഞ്ഞ്"), ("👩", "A grown-up", "വലിയവർ"), ("🧒", "Me alone", "ഞാൻ തനിയെ")], 1, "Sharp things are for grown-ups.", "മൂർച്ചയുള്ളവ വലിയവർ ഉപയോഗിക്കണം."),
    ("🐕", "A strange dog is barking at you. What do you do?", "ഒരു അപരിചിത പട്ടി കുരയ്ക്കുന്നു. എന്ത് ചെയ്യും?",
     [("🏃", "Throw a stone", "കല്ലെറിയും"), ("🧍", "Stay calm and walk away slowly", "പേടിക്കാതെ പതുക്കെ മാറിപ്പോകും"), ("😱", "Scream and run", "അലറി ഓടും")], 1, "Stay calm, do not tease it, walk away slowly.", "ശാന്തമായി നിന്ന് പതുക്കെ മാറിപ്പോകണം."),
    ("🌧️", "There is lightning outside. Where is it safe?", "പുറത്ത് ഇടിമിന്നലുണ്ട്. എവിടെ നിൽക്കുന്നതാണ് സുരക്ഷിതം?",
     [("🏠", "Inside the house", "വീടിനകത്ത്"), ("🌳", "Under a big tree", "വലിയ മരത്തിന്റെ ചുവട്ടിൽ"), ("🏞️", "In an open field", "തുറന്ന പാടത്ത്")], 0, "Stay inside during lightning.", "ഇടിമിന്നലുള്ളപ്പോൾ വീടിനകത്ത് നിൽക്കണം."),
]

LIFE_A["signs"] = [
    ("🛑", "What does this sign say?", "ഈ അടയാളം എന്താണ് പറയുന്നത്?",
     [("✋", "Stop", "നിൽക്കൂ"), ("🏃", "Go fast", "വേഗം പോകൂ"), ("🎉", "Party", "പാർട്ടി")], 0, "A red octagon means stop.", "ചുവന്ന അഷ്ടഭുജം 'നിൽക്കൂ' എന്നാണ്."),
    ("🚭", "What does this sign say?", "ഈ അടയാളം എന്താണ് പറയുന്നത്?",
     [("🚬", "Smoke here", "ഇവിടെ പുകവലിക്കാം"), ("🙅", "No smoking", "പുകവലി പാടില്ല"), ("🍽️", "Eat here", "ഇവിടെ കഴിക്കാം")], 1, "No smoking.", "പുകവലി പാടില്ല."),
    ("🚸", "This sign shows children walking. What should drivers do?", "ഈ അടയാളം കുട്ടികൾ നടക്കുന്നത് കാണിക്കുന്നു. ഡ്രൈവർ എന്ത് ചെയ്യണം?",
     [("🐢", "Go slowly", "പതുക്കെ പോകണം"), ("🏎️", "Go fast", "വേഗത്തിൽ പോകണം"), ("📣", "Honk loudly", "ഉറക്കെ ഹോൺ അടിക്കണം")], 0, "Slow down near children.", "കുട്ടികളുടെ അടുത്ത് വേഗത കുറയ്ക്കണം."),
    ("🚻", "Where do you see this sign?", "ഈ അടയാളം എവിടെയാണ് കാണുക?",
     [("🍳", "Kitchen", "അടുക്കള"), ("🚽", "Toilet", "ടോയ്‌ലറ്റ്"), ("🛏️", "Bedroom", "കിടപ്പുമുറി")], 1, "This sign shows the toilets.", "ഇത് ടോയ്‌ലറ്റിന്റെ അടയാളമാണ്."),
    ("⚠️", "A yellow triangle with ! means what?", "മഞ്ഞ ത്രികോണത്തിലെ ! എന്താണ് അർത്ഥമാക്കുന്നത്?",
     [("⚠️", "Be careful", "സൂക്ഷിക്കൂ"), ("🎁", "Gift", "സമ്മാനം"), ("🍕", "Food", "ഭക്ഷണം")], 0, "It is a warning sign.", "ഇത് മുന്നറിയിപ്പ് അടയാളമാണ്."),
    ("🆘", "What does SOS or a red cross mean?", "SOS അല്ലെങ്കിൽ ചുവന്ന ക്രോസ് എന്താണ് അർത്ഥമാക്കുന്നത്?",
     [("🩺", "Help or first aid", "സഹായം അല്ലെങ്കിൽ പ്രഥമശുശ്രൂഷ"), ("🎮", "Games", "കളികൾ"), ("🛍️", "Shopping", "ഷോപ്പിങ്")], 0, "Red cross means help for the hurt.", "ചുവന്ന ക്രോസ് സഹായത്തിന്റെ അടയാളമാണ്."),
    ("➡️", "The arrow points right. Which way do we go?", "അമ്പടയാളം വലത്തോട്ടാണ്. ഏത് വഴിക്ക് പോകണം?",
     [("⬅️", "Left", "ഇടത്തോട്ട്"), ("➡️", "Right", "വലത്തോട്ട്"), ("⬆️", "Straight", "നേരെ")], 1, "Follow the arrow to the right.", "അമ്പടയാളം പോലെ വലത്തോട്ട് പോകണം."),
    ("🚫", "A red circle with a line across means?", "വരയുള്ള ചുവന്ന വൃത്തം എന്താണ് അർത്ഥമാക്കുന്നത്?",
     [("🚫", "Not allowed", "അനുവദനീയമല്ല"), ("✅", "Allowed", "അനുവദനീയം"), ("🎈", "Balloon", "ബലൂൺ")], 0, "It means not allowed.", "ഇത് 'പാടില്ല' എന്നാണ്."),
]

LIFE_A["routine"] = [
    ("🌅", "You wake up in the morning. What do you do first?", "രാവിലെ ഉണർന്നു. ആദ്യം എന്ത് ചെയ്യും?",
     [("🪥", "Brush teeth", "പല്ല് തേയ്ക്കും"), ("📺", "Watch TV", "ടിവി കാണും"), ("🛌", "Sleep again", "വീണ്ടും ഉറങ്ങും")], 0, "Brush your teeth first.", "ആദ്യം പല്ല് തേയ്ക്കണം."),
    ("🍛", "What do we do before eating?", "ഭക്ഷണം കഴിക്കുന്നതിന് മുമ്പ് എന്ത് ചെയ്യണം?",
     [("🧼", "Wash hands", "കൈ കഴുകണം"), ("🏃", "Run around", "ഓടണം"), ("🎮", "Play a game", "കളിക്കണം")], 0, "Wash your hands with soap.", "സോപ്പിട്ട് കൈ കഴുകണം."),
    ("🚽", "What do we do after using the toilet?", "ടോയ്‌ലറ്റിൽ പോയിക്കഴിഞ്ഞാൽ എന്ത് ചെയ്യണം?",
     [("🧼", "Wash hands with soap", "സോപ്പിട്ട് കൈ കഴുകണം"), ("🍪", "Eat a biscuit", "ബിസ്കറ്റ് കഴിക്കണം"), ("🎒", "Pack the bag", "ബാഗ് എടുക്കണം")], 0, "Always wash hands after the toilet.", "ടോയ്‌ലറ്റിൽ പോയാൽ എപ്പോഴും കൈ കഴുകണം."),
    ("🌙", "At night, before bed, what do we do?", "രാത്രി ഉറങ്ങുന്നതിന് മുമ്പ് എന്ത് ചെയ്യണം?",
     [("🪥", "Brush teeth", "പല്ല് തേയ്ക്കണം"), ("☕", "Drink strong tea", "ചായ കുടിക്കണം"), ("🏏", "Play cricket", "ക്രിക്കറ്റ് കളിക്കണം")], 0, "Brush teeth before bed.", "ഉറങ്ങുന്നതിന് മുമ്പ് പല്ല് തേയ്ക്കണം."),
    ("🌧️", "It is raining and you go out. What do you take?", "മഴയത്ത് പുറത്ത് പോകുമ്പോൾ എന്താണ് എടുക്കേണ്ടത്?",
     [("☂️", "Umbrella", "കുട"), ("🧣", "Scarf", "ഷാൾ"), ("🕶️", "Sunglasses", "കൂളിംഗ് ഗ്ലാസ്")], 0, "An umbrella keeps us dry.", "കുട നനയാതെ കാക്കും."),
    ("🥵", "It is very hot. What should we drink?", "നല്ല ചൂടാണ്. എന്താണ് കുടിക്കേണ്ടത്?",
     [("💧", "Water", "വെള്ളം"), ("🔥", "Hot oil", "ചൂടുള്ള എണ്ണ"), ("🧴", "Shampoo", "ഷാംപൂ")], 0, "Drink water when it is hot.", "ചൂടുള്ളപ്പോൾ വെള്ളം കുടിക്കണം."),
    ("🛁", "Which one do we use for a bath?", "കുളിക്കാൻ എന്താണ് ഉപയോഗിക്കുക?",
     [("🧼", "Soap and water", "സോപ്പും വെള്ളവും"), ("🍫", "Chocolate", "ചോക്ലേറ്റ്"), ("📖", "Book", "പുസ്തകം")], 0, "Soap and water clean us.", "സോപ്പും വെള്ളവും കൊണ്ട് വൃത്തിയാകാം."),
    ("🗑️", "Where does the waste paper go?", "പഴയ കടലാസ് എവിടെയാണ് ഇടേണ്ടത്?",
     [("🗑️", "In the dustbin", "ചവറ്റുകുട്ടയിൽ"), ("🛣️", "On the road", "റോഡിൽ"), ("🛏️", "On the bed", "കട്ടിലിൽ")], 0, "Put waste in the dustbin.", "ചവറ് ചവറ്റുകുട്ടയിൽ ഇടണം."),
    ("🎒", "What do we take to school?", "സ്കൂളിൽ പോകുമ്പോൾ എന്ത് കൊണ്ടുപോകും?",
     [("🎒", "School bag", "സ്കൂൾ ബാഗ്"), ("🛏️", "Bed", "കട്ടിൽ"), ("🛋️", "Sofa", "സോഫ")], 0, "We carry books in a school bag.", "പുസ്തകങ്ങൾ സ്കൂൾ ബാഗിലാണ് കൊണ്ടുപോകുക."),
    ("🍎", "Which food is good for our body?", "ശരീരത്തിന് നല്ല ഭക്ഷണം ഏതാണ്?",
     [("🍎", "Fruits", "പഴങ്ങൾ"), ("🍬", "Only sweets", "മിഠായി മാത്രം"), ("🍟", "Only chips", "ചിപ്സ് മാത്രം")], 0, "Fruits and vegetables make us strong.", "പഴങ്ങളും പച്ചക്കറികളും നമ്മളെ ആരോഗ്യമുള്ളവരാക്കും."),
    ("👕", "Your shirt is dirty. What do you do?", "ഷർട്ട് അഴുക്കായി. എന്ത് ചെയ്യും?",
     [("🧺", "Put it in the wash basket", "അലക്കാൻ ഇടും"), ("🛏️", "Hide it under the bed", "കട്ടിലിനടിയിൽ ഒളിപ്പിക്കും"), ("🔥", "Burn it", "കത്തിക്കും")], 0, "Dirty clothes go to be washed.", "അഴുക്കായ തുണി അലക്കാൻ ഇടണം."),
    ("✂️", "Your nails are long. What do we do?", "നഖം നീണ്ടുപോയി. എന്ത് ചെയ്യും?",
     [("✂️", "Cut them with a grown-up's help", "വലിയവരുടെ സഹായത്തോടെ വെട്ടും"), ("🦷", "Bite them", "കടിക്കും"), ("🙈", "Ignore", "ശ്രദ്ധിക്കില്ല")], 0, "Short clean nails keep germs away.", "ചെറിയ വൃത്തിയുള്ള നഖം രോഗാണുക്കളെ അകറ്റും."),
    ("😷", "You are sneezing. What do you do?", "തുമ്മൽ വരുന്നു. എന്ത് ചെയ്യും?",
     [("🤧", "Cover with a hanky or elbow", "തൂവാല കൊണ്ടോ കൈമുട്ട് കൊണ്ടോ മൂടും"), ("😤", "Sneeze on friends", "കൂട്ടുകാരുടെ മേൽ തുമ്മും"), ("🏃", "Run", "ഓടും")], 0, "Cover your sneeze to protect others.", "തുമ്മുമ്പോൾ മൂടിയാൽ മറ്റുള്ളവർക്ക് രോഗം പകരില്ല."),
]
'''

_SOURCES['life_b'] = r'''
# Hand-written life-skill questions, part B: manners and feelings, money, time, opposites.
LIFE_B = {}

LIFE_B["manners"] = [
    ("🙏", "Someone gives you a gift. What do you say?", "ആരെങ്കിലും സമ്മാനം തന്നു. എന്ത് പറയും?",
     [("😊", "Thank you", "നന്ദി"), ("😠", "Go away", "പോ അവിടുന്ന്"), ("🤐", "Nothing", "ഒന്നും പറയില്ല")], 0, "We say thank you.", "നന്ദി പറയണം."),
    ("🌞", "You meet your teacher in the morning. What do you say?", "രാവിലെ ടീച്ചറെ കണ്ടു. എന്ത് പറയും?",
     [("👋", "Good morning", "ഗുഡ് മോണിംഗ്"), ("🙈", "Nothing", "ഒന്നും പറയില്ല"), ("😝", "Make a face", "കോക്രി കാണിക്കും")], 0, "Greet with a smile.", "ചിരിച്ചുകൊണ്ട് ഗുഡ് മോണിംഗ് പറയണം."),
    ("🧸", "Your friend wants to play with your toy. What do you do?", "കൂട്ടുകാരൻ നിന്റെ കളിപ്പാട്ടം കൊണ്ട് കളിക്കണമെന്ന് പറഞ്ഞു. എന്ത് ചെയ്യും?",
     [("🤝", "Share it", "പങ്കുവയ്ക്കും"), ("😤", "Hide it", "ഒളിപ്പിക്കും"), ("👊", "Hit him", "അടിക്കും")], 0, "Sharing makes friends.", "പങ്കുവച്ചാൽ കൂട്ടുകാരെ കിട്ടും."),
    ("😢", "Your friend is crying. What do you do?", "കൂട്ടുകാരൻ കരയുന്നു. എന്ത് ചെയ്യും?",
     [("🤗", "Say 'what happened?' and be kind", "'എന്ത് പറ്റി?' എന്ന് ചോദിച്ച് സ്നേഹത്തോടെ പെരുമാറും"), ("😆", "Laugh at him", "കളിയാക്കി ചിരിക്കും"), ("🚶", "Walk away", "നടന്നു പോകും")], 0, "Be kind when someone is sad.", "ആരെങ്കിലും സങ്കടപ്പെടുമ്പോൾ സ്നേഹത്തോടെ പെരുമാറണം."),
    ("🙋", "You want to ask the teacher something. What do you do?", "ടീച്ചറോട് എന്തെങ്കിലും ചോദിക്കണം. എന്ത് ചെയ്യും?",
     [("✋", "Raise your hand", "കൈ പൊക്കും"), ("📣", "Shout", "അലറി വിളിക്കും"), ("🏃", "Run to her", "ഓടിച്ചെല്ലും")], 0, "Raise your hand and wait.", "കൈ പൊക്കി കാത്തിരിക്കണം."),
    ("🚌", "In a bus, an old person has no seat. What do you do?", "ബസ്സിൽ ഒരു മുത്തശ്ശന് ഇരിക്കാൻ സീറ്റില്ല. എന്ത് ചെയ്യും?",
     [("💺", "Offer my seat", "എന്റെ സീറ്റ് കൊടുക്കും"), ("📱", "Look at the phone", "ഫോണിൽ നോക്കിയിരിക്കും"), ("😴", "Pretend to sleep", "ഉറങ്ങുന്നതായി നടിക്കും")], 0, "We help older people.", "പ്രായമായവരെ നമ്മൾ സഹായിക്കണം."),
    ("🙇", "You bump into someone by mistake. What do you say?", "അറിയാതെ ആരെയെങ്കിലും തട്ടി. എന്ത് പറയും?",
     [("🙏", "Sorry", "ക്ഷമിക്കണം"), ("😠", "Move away", "മാറി നിൽക്ക്"), ("🤐", "Nothing", "ഒന്നും പറയില്ല")], 0, "Say sorry.", "ക്ഷമ ചോദിക്കണം."),
    ("🎒", "You find a pencil box on the floor. What do you do?", "നിലത്ത് ഒരു പെൻസിൽ ബോക്സ് കിട്ടി. എന്ത് ചെയ്യും?",
     [("🧑‍🏫", "Give it to the teacher", "ടീച്ചർക്ക് കൊടുക്കും"), ("🎒", "Keep it", "എടുത്തുവയ്ക്കും"), ("🗑️", "Throw it", "കളയും")], 0, "Return what is not yours.", "നമ്മുടേതല്ലാത്തത് തിരിച്ചു കൊടുക്കണം."),
    ("🤫", "The class is quiet and someone is reading. What do you do?", "ക്ലാസ് ശാന്തമാണ്, ഒരാൾ വായിക്കുന്നു. എന്ത് ചെയ്യും?",
     [("🤫", "Keep quiet", "ശബ്ദമുണ്ടാക്കാതിരിക്കും"), ("📣", "Shout", "ഉറക്കെ വിളിക്കും"), ("🥁", "Beat a drum", "ഡ്രം അടിക്കും")], 0, "Be quiet so others can read.", "മറ്റുള്ളവർക്ക് വായിക്കാൻ ശബ്ദമുണ്ടാക്കാതിരിക്കണം."),
    ("🍽️", "Before you eat, what can you say or do?", "ഭക്ഷണത്തിന് മുമ്പ് എന്ത് ചെയ്യാം?",
     [("🧼", "Wash hands and sit nicely", "കൈ കഴുകി നന്നായി ഇരിക്കാം"), ("🏃", "Run around", "ഓടി നടക്കാം"), ("🎮", "Play games", "കളിക്കാം")], 0, "Wash hands and sit down to eat.", "കൈ കഴുകി ഇരുന്ന് കഴിക്കണം."),
]

LIFE_B["feelsit"] = [
    ("🎂", "It is your birthday. How do you feel?", "ഇന്ന് നിന്റെ പിറന്നാളാണ്. എന്ത് തോന്നും?",
     [("😀", "Happy", "സന്തോഷം"), ("😢", "Sad", "സങ്കടം"), ("😡", "Angry", "ദേഷ്യം")], 0, "Birthdays make us happy.", "പിറന്നാൾ സന്തോഷമാണ്."),
    ("🧸", "Your toy broke. How do you feel?", "കളിപ്പാട്ടം പൊട്ടിപ്പോയി. എന്ത് തോന്നും?",
     [("😀", "Happy", "സന്തോഷം"), ("😢", "Sad", "സങ്കടം"), ("😴", "Sleepy", "ഉറക്കം")], 1, "It is okay to feel sad. A grown-up can help.", "സങ്കടം തോന്നുന്നത് സാരമില്ല. വലിയവർ സഹായിക്കും."),
    ("🌑", "It is dark and you hear a loud noise. How do you feel?", "ഇരുട്ടത്ത് വലിയ ശബ്ദം കേട്ടു. എന്ത് തോന്നും?",
     [("😨", "Scared", "പേടി"), ("😀", "Happy", "സന്തോഷം"), ("😋", "Hungry", "വിശപ്പ്")], 0, "Feeling scared is okay. Go to a grown-up.", "പേടി തോന്നുന്നത് സാരമില്ല. വലിയവരുടെ അടുത്ത് പോകാം."),
    ("😡", "You feel very angry. What can you do?", "വല്ലാതെ ദേഷ്യം വരുന്നു. എന്ത് ചെയ്യാം?",
     [("🌬️", "Take slow deep breaths", "പതുക്കെ ദീർഘശ്വാസം എടുക്കാം"), ("👊", "Hit someone", "ആരെയെങ്കിലും അടിക്കാം"), ("🔨", "Break things", "സാധനങ്ങൾ പൊട്ടിക്കാം")], 0, "Slow breaths calm the body.", "പതുക്കെ ശ്വാസമെടുത്താൽ ശാന്തമാകും."),
    ("🤒", "You have a fever. What do you tell mother?", "പനിയാണ്. അമ്മയോട് എന്ത് പറയും?",
     [("🗣️", "I am not well", "എനിക്ക് സുഖമില്ല"), ("🤐", "Nothing", "ഒന്നും പറയില്ല"), ("🏃", "Go and play", "കളിക്കാൻ പോകും")], 0, "Tell a grown-up when you feel ill.", "സുഖമില്ലെങ്കിൽ വലിയവരോട് പറയണം."),
    ("🍽️", "Your tummy is rumbling. How do you feel?", "വയറ്റിൽ കാളുന്നു. എന്ത് തോന്നും?",
     [("😋", "Hungry", "വിശക്കുന്നു"), ("😴", "Sleepy", "ഉറക്കം വരുന്നു"), ("😨", "Scared", "പേടി")], 0, "Tummy rumbles mean hungry.", "വയറ് കാളുന്നത് വിശപ്പ് കൊണ്ടാണ്."),
    ("🥳", "You won a small prize. How do you feel?", "ഒരു ചെറിയ സമ്മാനം കിട്ടി. എന്ത് തോന്നും?",
     [("😀", "Proud and happy", "അഭിമാനവും സന്തോഷവും"), ("😢", "Sad", "സങ്കടം"), ("😡", "Angry", "ദേഷ്യം")], 0, "Winning feels great.", "സമ്മാനം കിട്ടുന്നത് സന്തോഷമാണ്."),
    ("🛌", "It is night and your eyes are closing. How do you feel?", "രാത്രിയായി, കണ്ണ് അടഞ്ഞുപോകുന്നു. എന്ത് തോന്നും?",
     [("😴", "Sleepy", "ഉറക്കം"), ("😲", "Surprised", "അത്ഭുതം"), ("😡", "Angry", "ദേഷ്യം")], 0, "Time to sleep.", "ഉറങ്ങാൻ സമയമായി."),
]

LIFE_B["money"] = [
    ("🪙", "Which one is a coin?", "ഇതിൽ ഏതാണ് നാണയം?",
     [("🪙", "Coin", "നാണയം"), ("📖", "Book", "പുസ്തകം"), ("🍎", "Apple", "ആപ്പിൾ")], 0, "A coin is round and metal.", "നാണയം വൃത്താകൃതിയിൽ ലോഹം കൊണ്ടുള്ളതാണ്."),
    ("💵", "Which one is a note?", "ഇതിൽ ഏതാണ് നോട്ട്?",
     [("🗒️", "Paper", "കടലാസ്"), ("💵", "Money note", "പണത്തിന്റെ നോട്ട്"), ("🍞", "Bread", "ബ്രെഡ്")], 1, "Money notes are paper money.", "നോട്ട് പണമാണ്."),
    ("🏪", "Where do we buy bread and biscuits?", "ബ്രെഡും ബിസ്കറ്റും എവിടെ നിന്ന് വാങ്ങും?",
     [("🏪", "Shop", "കടയിൽ നിന്ന്"), ("🏥", "Hospital", "ആശുപത്രിയിൽ നിന്ന്"), ("🏫", "School", "സ്കൂളിൽ നിന്ന്")], 0, "We buy from a shop.", "കടയിൽ നിന്നാണ് വാങ്ങുന്നത്."),
    ("🍫", "You want a chocolate. What do you give the shopkeeper?", "ചോക്ലേറ്റ് വേണം. കടക്കാരന് എന്ത് കൊടുക്കും?",
     [("💵", "Money", "പണം"), ("🪨", "A stone", "കല്ല്"), ("🍂", "Dry leaves", "ഉണങ്ങിയ ഇല")], 0, "We pay money for things.", "സാധനത്തിന് പണം കൊടുക്കണം."),
    ("🐷", "Where do we save our coins?", "നാണയങ്ങൾ എവിടെ സൂക്ഷിക്കും?",
     [("🐷", "Piggy bank", "കുടുക്ക"), ("🗑️", "Dustbin", "ചവറ്റുകുട്ട"), ("🌊", "River", "പുഴ")], 0, "A piggy bank keeps coins safe.", "കുടുക്കയിൽ നാണയം സുരക്ഷിതമായിരിക്കും."),
    ("🔢", "A toffee costs 2 rupees. You have 5 rupees. Can you buy it?", "ഒരു മിഠായിക്ക് 2 രൂപയാണ്. നിന്റെ കയ്യിൽ 5 രൂപയുണ്ട്. വാങ്ങാൻ പറ്റുമോ?",
     [("✅", "Yes", "പറ്റും"), ("❌", "No", "പറ്റില്ല"), ("🤷", "Cannot say", "അറിയില്ല")], 0, "5 is more than 2, so yes.", "5, 2-നേക്കാൾ കൂടുതലാണ്, അതുകൊണ്ട് പറ്റും."),
    ("🔢", "A pencil costs 5 rupees. You have 2 rupees. Can you buy it?", "ഒരു പെൻസിലിന് 5 രൂപയാണ്. നിന്റെ കയ്യിൽ 2 രൂപയേ ഉള്ളൂ. വാങ്ങാൻ പറ്റുമോ?",
     [("✅", "Yes", "പറ്റും"), ("❌", "No, not enough", "പറ്റില്ല, തികയില്ല"), ("🤷", "Cannot say", "അറിയില്ല")], 1, "2 is less than 5, so not enough.", "2, 5-നേക്കാൾ കുറവാണ്, അതുകൊണ്ട് തികയില്ല."),
    ("💰", "You found money on the road. What do you do?", "റോഡിൽ നിന്ന് പണം കിട്ടി. എന്ത് ചെയ്യും?",
     [("👩", "Give it to a grown-up", "വലിയവരെ ഏൽപ്പിക്കും"), ("🛍️", "Keep and spend it", "എടുത്ത് ചെലവാക്കും"), ("🏃", "Run away", "ഓടിപ്പോകും")], 0, "Tell a grown-up so the owner can be found.", "വലിയവരോട് പറഞ്ഞാൽ ഉടമയെ കണ്ടെത്താം."),
    ("🏧", "Who keeps our money safe for us?", "നമ്മുടെ പണം സൂക്ഷിക്കാൻ ആരാണ് സഹായിക്കുന്നത്?",
     [("🏦", "Bank", "ബാങ്ക്"), ("🏖️", "Beach", "കടപ്പുറം"), ("🌳", "Park", "പാർക്ക്")], 0, "A bank keeps money safe.", "ബാങ്ക് പണം സുരക്ഷിതമായി സൂക്ഷിക്കും."),
    ("🛒", "You need milk. Which do you buy?", "പാല് വേണം. ഏതാണ് വാങ്ങുക?",
     [("🥛", "Milk packet", "പാൽ പാക്കറ്റ്"), ("🧼", "Soap", "സോപ്പ്"), ("🪥", "Brush", "ബ്രഷ്")], 0, "Milk packet is for milk.", "പാൽ പാക്കറ്റ് ആണ് പാലിന്."),
]

LIFE_B["time"] = [
    ("🌅", "When does the sun come up?", "സൂര്യൻ എപ്പോഴാണ് ഉദിക്കുന്നത്?",
     [("🌅", "Morning", "രാവിലെ"), ("🌙", "Night", "രാത്രി"), ("🌆", "Evening", "വൈകുന്നേരം")], 0, "The sun rises in the morning.", "രാവിലെയാണ് സൂര്യൻ ഉദിക്കുന്നത്."),
    ("🌙", "When do we see the moon and stars?", "ചന്ദ്രനെയും നക്ഷത്രങ്ങളെയും എപ്പോൾ കാണാം?",
     [("☀️", "Noon", "ഉച്ചയ്ക്ക്"), ("🌙", "Night", "രാത്രി"), ("🌅", "Morning", "രാവിലെ")], 1, "We see them at night.", "രാത്രിയിലാണ് കാണുക."),
    ("🍽️", "We eat lunch at ...", "ഉച്ചഭക്ഷണം കഴിക്കുന്നത് ...",
     [("🌞", "Noon", "ഉച്ചയ്ക്ക്"), ("🌙", "Midnight", "അർദ്ധരാത്രി"), ("🌅", "Sunrise", "സൂര്യോദയത്തിന്")], 0, "Lunch is at noon.", "ഉച്ചയ്ക്കാണ് ലഞ്ച്."),
    ("📅", "How many days are in a week?", "ഒരു ആഴ്ചയിൽ എത്ര ദിവസമുണ്ട്?",
     [("7️⃣", "7", "7"), ("5️⃣", "5", "5"), ("🔟", "10", "10")], 0, "A week has 7 days.", "ഒരു ആഴ്ചയിൽ 7 ദിവസം."),
    ("📅", "Which day comes after Monday?", "തിങ്കളാഴ്ചയ്ക്ക് ശേഷം ഏത് ദിവസം?",
     [("2️⃣", "Tuesday", "ചൊവ്വ"), ("🕐", "Sunday", "ഞായർ"), ("🎉", "Friday", "വെള്ളി")], 0, "Tuesday follows Monday.", "തിങ്കൾ കഴിഞ്ഞാൽ ചൊവ്വ."),
    ("🏫", "Which day do many schools have a holiday?", "മിക്ക സ്കൂളുകൾക്കും ഏത് ദിവസമാണ് അവധി?",
     [("🏖️", "Sunday", "ഞായർ"), ("📚", "Monday", "തിങ്കൾ"), ("📚", "Wednesday", "ബുധൻ")], 0, "Sunday is a holiday.", "ഞായറാഴ്ച അവധിയാണ്."),
    ("🕰️", "What does a clock tell us?", "ക്ലോക്ക് എന്താണ് പറഞ്ഞുതരുന്നത്?",
     [("⏰", "The time", "സമയം"), ("🌡️", "The weather", "കാലാവസ്ഥ"), ("🎨", "Colours", "നിറങ്ങൾ")], 0, "A clock shows the time.", "ക്ലോക്ക് സമയം കാണിക്കുന്നു."),
    ("🌆", "The sun goes down and the sky is orange. It is ...", "സൂര്യൻ അസ്തമിക്കുന്നു, ആകാശം ഓറഞ്ച് നിറം. ഇത് ...",
     [("🌆", "Evening", "വൈകുന്നേരം"), ("🌅", "Morning", "രാവിലെ"), ("☀️", "Noon", "ഉച്ച")], 0, "Sunset is in the evening.", "അസ്തമയം വൈകുന്നേരമാണ്."),
]

LIFE_B["opposites"] = [
    ("⬆️", "What is the opposite of UP?", "മുകളിൽ എന്നതിന്റെ എതിരായത് ഏത്?",
     [("⬇️", "Down", "താഴെ"), ("➡️", "Right", "വലത്"), ("⬆️", "Up", "മുകളിൽ")], 0, "Up and down are opposites.", "മുകളിൽ, താഴെ എതിരാണ്."),
    ("🐘", "An elephant is big. What is a mouse?", "ആന വലുതാണ്. എലി എങ്ങനെയാണ്?",
     [("🐭", "Small", "ചെറുത്"), ("🏔️", "Huge", "വലിയത്"), ("🌈", "Colourful", "നിറമുള്ളത്")], 0, "Big and small are opposites.", "വലുത്, ചെറുത് എതിരാണ്."),
    ("☀️", "Day is bright. What is night?", "പകൽ വെളിച്ചമാണ്. രാത്രി എങ്ങനെ?",
     [("🌑", "Dark", "ഇരുട്ട്"), ("🔥", "Hot", "ചൂട്"), ("💦", "Wet", "നനവ്")], 0, "Light and dark are opposites.", "വെളിച്ചം, ഇരുട്ട് എതിരാണ്."),
    ("🔥", "Fire is hot. What is ice?", "തീ ചൂടാണ്. ഐസ് എങ്ങനെ?",
     [("🧊", "Cold", "തണുപ്പ്"), ("🔥", "Hot", "ചൂട്"), ("🍬", "Sweet", "മധുരം")], 0, "Hot and cold are opposites.", "ചൂട്, തണുപ്പ് എതിരാണ്."),
    ("🐢", "A tortoise is slow. What is a rabbit?", "ആമ പതുക്കെയാണ്. മുയൽ എങ്ങനെ?",
     [("🐇", "Fast", "വേഗം"), ("🐢", "Slow", "പതുക്കെ"), ("🛌", "Sleepy", "ഉറക്കം")], 0, "Slow and fast are opposites.", "പതുക്കെ, വേഗം എതിരാണ്."),
    ("📏", "A pole is tall. What is a stool?", "തൂണ് ഉയരമുള്ളതാണ്. സ്റ്റൂൾ എങ്ങനെ?",
     [("🪑", "Short", "ഉയരം കുറഞ്ഞത്"), ("🌳", "Tall", "ഉയരമുള്ളത്"), ("🍎", "Red", "ചുവപ്പ്")], 0, "Tall and short are opposites.", "ഉയരം, കുറവ് എതിരാണ്."),
    ("😀", "What is the opposite of happy?", "സന്തോഷത്തിന്റെ എതിരായത് ഏത്?",
     [("😢", "Sad", "സങ്കടം"), ("😀", "Glad", "ആഹ്ലാദം"), ("🤪", "Funny", "തമാശ")], 0, "Happy and sad are opposites.", "സന്തോഷം, സങ്കടം എതിരാണ്."),
    ("🚪", "The door is open. What is the opposite?", "വാതിൽ തുറന്നിരിക്കുന്നു. എതിരായത് ഏത്?",
     [("🚪", "Closed", "അടച്ചത്"), ("🔓", "Open", "തുറന്നത്"), ("🔔", "Ring", "മണി")], 0, "Open and closed are opposites.", "തുറന്നത്, അടച്ചത് എതിരാണ്."),
    ("🫗", "A glass is full. What is the opposite?", "ഗ്ലാസ് നിറഞ്ഞിരിക്കുന്നു. എതിരായത് ഏത്?",
     [("🥛", "Empty", "ശൂന്യം"), ("🥛", "Full", "നിറഞ്ഞത്"), ("🧃", "Juice", "ജ്യൂസ്")], 0, "Full and empty are opposites.", "നിറഞ്ഞത്, ശൂന്യം എതിരാണ്."),
]
'''

_SOURCES['content'] = r'''
# Pyqoo Easy content: lessons and a large generated question bank (English + spoken Malayalam).
import random

from items_a import A
from items_b import B
from items_c import C as CC
from life_a import LIFE_A
from life_b import LIFE_B

QUESTIONS_PER_PLAY = 6
MIX_LENGTH = 8

ITEMS = {}   # category -> [(emoji, en, ml)]
for _src in (A, B):
    for _cat, _txt in _src.items():
        ITEMS[_cat] = [tuple(x.strip() for x in ln.split("|")) for ln in _txt.strip().splitlines() if ln.strip()]
LETTERS = {k: [tuple(x.strip() for x in ln.split("|")) for ln in CC[k].strip().splitlines() if ln.strip()] for k in CC}

# prompts: category -> (find_en, find_ml, name_en, name_ml, mode of name options)
P = {
    "animals": ("Tap the {en}.", "{ml} ഏതാ?", "Which animal is this?", "ഇത് ഏത് മൃഗമാ?"),
    "birds": ("Tap the {en}.", "{ml} ഏതാ?", "What is this?", "ഇതെന്താ?"),
    "fruits": ("Tap the {en}.", "{ml} ഏതാ?", "Which fruit is this?", "ഇത് ഏത് പഴമാ?"),
    "vegetables": ("Tap the {en}.", "{ml} ഏതാ?", "Which vegetable is this?", "ഇത് ഏത് പച്ചക്കറിയാ?"),
    "food": ("Tap the {en}.", "{ml} ഏതാ?", "What food is this?", "ഇത് എന്ത് ഭക്ഷണമാ?"),
    "colours": ("Tap the colour {en}.", "{ml} നിറം ഏതാ?", "What colour is this?", "ഇത് ഏത് നിറമാ?"),
    "shapes": ("Tap the {en}.", "{ml} ഏതാ?", "What shape is this?", "ഇത് ഏത് ആകൃതിയാ?"),
    "body": ("Tap the {en}.", "{ml} ഏതാ?", "What part of the body is this?", "ഇത് ശരീരത്തിന്റെ ഏത് ഭാഗമാ?"),
    "people": ("Tap the {en}.", "{ml} ആരാ?", "Who is this?", "ഇതാരാ?"),
    "helpers": ("Tap the {en}.", "{ml} ആരാ?", "Who is this?", "ഇതാരാ?"),
    "clothes": ("Tap the {en}.", "{ml} ഏതാ?", "What do we wear or carry?", "ഇത് എന്താ?"),
    "home": ("Tap the {en}.", "{ml} ഏതാ?", "What is this?", "ഇതെന്താ?"),
    "school": ("Tap the {en}.", "{ml} ഏതാ?", "What is this?", "ഇതെന്താ?"),
    "vehicles": ("Tap the {en}.", "{ml} ഏതാ?", "Which vehicle is this?", "ഇത് ഏത് വണ്ടിയാ?"),
    "nature": ("Tap the {en}.", "{ml} ഏതാ?", "What is this?", "ഇതെന്താ?"),
    "places": ("Tap the {en}.", "{ml} ഏതാ?", "What place is this?", "ഇത് എവിടെയാ?"),
    "feelings": ("Tap the face that is {en}.", "{ml} ഉള്ള മുഖം ഏതാ?", "How does this face feel?", "ഈ മുഖത്തിന് എന്ത് തോന്നുന്നു?"),
    "actions": ("Who is {en}?", "{ml} ആരാ?", "What is happening?", "എന്താ നടക്കുന്നത്?"),
}
# odd one out: category -> (English noun phrase, Malayalam noun, other categories to borrow the odd one from)
ODD = {
    "animals": ("an animal", "മൃഗം", ["vehicles", "fruits", "clothes"]),
    "fruits": ("a fruit", "പഴം", ["animals", "vehicles", "home"]),
    "vegetables": ("a vegetable", "പച്ചക്കറി", ["animals", "vehicles", "clothes"]),
    "food": ("a food", "ഭക്ഷണം", ["animals", "vehicles", "clothes"]),
    "vehicles": ("a vehicle", "വണ്ടി", ["fruits", "animals", "clothes"]),
    "clothes": ("something we wear or carry", "ധരിക്കുന്ന സാധനം", ["fruits", "animals", "vehicles"]),
    "home": ("a thing in a house", "വീട്ടിലെ സാധനം", ["animals", "fruits", "vehicles"]),
    "school": ("a school thing", "സ്കൂൾ സാധനം", ["animals", "fruits", "vehicles"]),
}

LESSON_LIST = []     # in display order
BANK = {}            # lesson id -> [question dicts]


def opt(it):
    return dict(e=it[0], en=it[1], ml=it[2])


def num_opt(n):
    return dict(e="", en=str(n), ml=str(n))


def Q(lid, qid, kind, mode, big, en, ml, rights, wrongs, why_en, why_ml, **extra):
    d = dict(id=f"{lid}:{qid}", lid=lid, kind=kind, mode=mode, big=big, en=en, ml=ml,
             rights=rights, wrongs=wrongs, why_en=why_en, why_ml=why_ml)
    d.update(extra)
    return d


def lesson(lid, level, art, en, ml, blurb_en, blurb_ml, story, bank, goal=""):
    LESSON_LIST.append(dict(id=lid, level=level, art=art, en=en, ml=ml, blurb_en=blurb_en, blurb_ml=blurb_ml, story=story, goal=goal))
    BANK[lid] = bank


def picture_bank(cat):
    items = ITEMS[cat]
    f_en, f_ml, n_en, n_ml = P[cat]
    out = []
    for i, it in enumerate(items):
        others = [opt(x) for j, x in enumerate(items) if j != i]
        me = opt(it)
        out.append(Q(cat, f"{i}f", "find", "pic", "", f_en.format(en=it[1].lower() if cat not in ("people", "helpers") else it[1].lower()), f_ml.format(ml=it[2]),
                     [me], others, f"Yes! This is the {it[1].lower()}.", f"ശരിയാണ്! ഇത് {it[2]} ആണ്."))
        out.append(Q(cat, f"{i}n", "name", "word", it[0], n_en, n_ml, [me], others, f"This is the {it[1].lower()}.", f"ഇത് {it[2]} ആണ്."))
    if cat in ODD:
        noun_en, noun_ml, alien = ODD[cat]
        pool = [opt(x) for a in alien for x in ITEMS[a]]
        for i, it in enumerate(items):
            out.append(Q(cat, f"{i}o", "odd", "pic", "", f"Which one is NOT {noun_en}?", f"ഇതിൽ {noun_ml} അല്ലാത്തത് ഏതാ?",
                         pool, [opt(x) for x in items], "That one does not belong with the others.", "ഇത് മറ്റുള്ളവയുടെ കൂട്ടത്തിൽ പെടില്ല.",
                         anchor=opt(it)))
    return out


def letters_bank(kind):
    items = LETTERS[kind]
    out = []
    for i, (e, en, ml, ch) in enumerate(items):
        me = dict(e=e, en=en, ml=ml)
        others = [dict(e=x[0], en=x[1], ml=x[2]) for j, x in enumerate(items) if j != i]
        letter_opt = dict(e="", en=ch, ml=ch)
        other_letters = [dict(e="", en=x[3], ml=x[3]) for j, x in enumerate(items) if j != i]
        if kind == "abc":
            out.append(Q(kind, f"{i}p", "find", "pic", ch, f"Which picture starts with {ch}?", f"{ch} കൊണ്ട് തുടങ്ങുന്ന ചിത്രം ഏതാ?",
                         [me], others, f"{ch} is for {en}.", f"{ch} എന്നാൽ {en} ({ml})."))
            out.append(Q(kind, f"{i}l", "name", "word", e, "Which letter does this start with?", "ഇത് ഏത് അക്ഷരം കൊണ്ടാ തുടങ്ങുന്നത്?",
                         [letter_opt], other_letters, f"{en} starts with {ch}.", f"{en} തുടങ്ങുന്നത് {ch} കൊണ്ടാണ്."))
        else:
            out.append(Q(kind, f"{i}p", "find", "pic", ch, f"Which picture starts with the letter {ch}?", f"{ch} കൊണ്ട് തുടങ്ങുന്ന ചിത്രം ഏതാ?",
                         [me], others, f"{ch} is for {en}.", f"{ch} എന്നാൽ {ml}."))
            out.append(Q(kind, f"{i}l", "name", "word", e, "Which letter does this start with?", "ഇത് ഏത് അക്ഷരം കൊണ്ടാ തുടങ്ങുന്നത്?",
                         [letter_opt], other_letters, f"{ml} starts with {ch}.", f"{ml} തുടങ്ങുന്നത് {ch} കൊണ്ടാണ്."))
    return out


NUM_ML = {1: "ഒന്ന്", 2: "രണ്ട്", 3: "മൂന്ന്", 4: "നാല്", 5: "അഞ്ച്", 6: "ആറ്", 7: "ഏഴ്", 8: "എട്ട്", 9: "ഒൻപത്", 10: "പത്ത്"}
COUNT_THINGS = [("🍎", "apples", "ആപ്പിൾ"), ("⭐", "stars", "നക്ഷത്രം"), ("🐟", "fish", "മീൻ"), ("🎈", "balloons", "ബലൂൺ"), ("🚗", "cars", "കാർ"),
                ("⚽", "balls", "പന്ത്"), ("🌸", "flowers", "പൂവ്"), ("🐔", "hens", "കോഴി"), ("🥭", "mangoes", "മാങ്ങ"), ("🐘", "elephants", "ആന")]


def counting_bank():
    out = []
    nums = [num_opt(n) for n in range(1, 11)]
    for ti, (e, en, ml) in enumerate(COUNT_THINGS):
        for n in range(1, 11):
            out.append(Q("count", f"c{ti}_{n}", "count", "num", e * n, f"How many {en}?", f"എത്ര {ml} ഉണ്ട്?",
                         [nums[n - 1]], [x for x in nums if x["en"] != str(n)], f"There are {n}.", f"{NUM_ML[n]} എണ്ണം ഉണ്ട്."))
    for n in range(1, 11):
        out.append(Q("count", f"t{n}", "find", "num", "", f"Tap the number {n}.", f"{NUM_ML[n]} ഏതാ?",
                     [nums[n - 1]], [x for x in nums if x["en"] != str(n)], f"This is {n}.", f"ഇത് {NUM_ML[n]}."))
    for n in range(1, 10):
        out.append(Q("count", f"a{n}", "order", "num", "", f"What comes after {n}?", f"{n}-ന് ശേഷം ഏത് സംഖ്യ?",
                     [nums[n]], [x for x in nums if x["en"] != str(n + 1)], f"After {n} comes {n + 1}.", f"{n}-ന് ശേഷം {n + 1}."))
    for n in range(2, 11):
        out.append(Q("count", f"b{n}", "order", "num", "", f"What comes before {n}?", f"{n}-ന് മുമ്പ് ഏത് സംഖ്യ?",
                     [nums[n - 2]], [x for x in nums if x["en"] != str(n - 1)], f"Before {n} comes {n - 1}.", f"{n}-ന് മുമ്പ് {n - 1}."))
    pairs = [(a, b) for a in range(1, 10) for b in range(1, 10) if a > b and a - b >= 1][:30]
    for k, (a, b) in enumerate(pairs):
        e = COUNT_THINGS[k % len(COUNT_THINGS)][0]
        big = e * a + "   " + e * b
        out.append(Q("count", f"m{a}_{b}", "more", "pic", big, "Which group has MORE?", "ഏത് കൂട്ടത്തിലാണ് കൂടുതൽ?",
                     [dict(e=e * a, en=f"{a}", ml=f"{a}")], [dict(e=e * b, en=f"{b}", ml=f"{b}")], f"{a} is more than {b}.", f"{b}-നേക്കാൾ കൂടുതൽ {a} ആണ്."))
    return out


def sums_bank():
    out = []
    nums = [num_opt(n) for n in range(0, 11)]
    for a in range(1, 6):
        for b in range(1, 6):
            e = COUNT_THINGS[(a + b) % len(COUNT_THINGS)][0]
            out.append(Q("sums", f"p{a}_{b}", "add", "num", f"{e * a}  +  {e * b}", f"{a} + {b} = ?", f"{a} + {b} = എത്ര?",
                         [nums[a + b]], [x for x in nums if x["en"] != str(a + b)], f"{a} and {b} make {a + b}.", f"{a} + {b} = {a + b}."))
    for a in range(2, 9):
        for b in range(1, min(a, 4)):
            e = COUNT_THINGS[a % len(COUNT_THINGS)][0]
            out.append(Q("sums", f"s{a}_{b}", "sub", "num", f"{e * a}  −  {b}", f"{a} − {b} = ?", f"{a} − {b} = എത്ര?",
                         [nums[a - b]], [x for x in nums if x["en"] != str(a - b)], f"{a} take away {b} is {a - b}.", f"{a} ൽ നിന്ന് {b} കുറച്ചാൽ {a - b}."))
    return out


def life_bank(cat, src):
    out = []
    for i, (big, qen, qml, opts, right, wen, wml) in enumerate(src[cat]):
        o = [dict(e=e, en=en.strip(), ml=ml.strip()) for e, en, ml in opts]
        out.append(Q(cat, f"x{i}", "life", "pic", big, qen, qml.strip(), [o[right]], [x for j, x in enumerate(o) if j != right], wen, wml))
    return out


def mixed_odd_bank():
    """Mixed odd-one-out across everything: tap the one that is different."""
    return []


# ---------------------------------------------------------------------------------- lessons
S = lambda *pairs: [(e, t) for e, t in pairs]

L1 = "start"
L2 = "grow"
L3 = "shine"

lesson("animals", L1, "🐶", "Animals", "മൃഗങ്ങൾ", "Dog, cat, cow, elephant and more.", "പട്ടി, പൂച്ച, പശു, ആന അങ്ങനെ പലതും.",
       S(("🐶", "Look at the animals!"), ("🐄", "Tap the right picture."), ("⭐", "You can do it!")), picture_bank("animals"), "Names 10 animals")
lesson("fruits", L1, "🍎", "Fruits", "പഴങ്ങൾ", "Apple, mango, banana and more.", "ആപ്പിൾ, മാങ്ങ, പഴം അങ്ങനെ പലതും.",
       S(("🍎", "Yummy fruits!"), ("🥭", "Tap the right picture."), ("⭐", "Let us begin!")), picture_bank("fruits"), "Names 8 fruits")
lesson("colours", L1, "🌈", "Colours", "നിറങ്ങൾ", "Red, blue, green, yellow and more.", "ചുവപ്പ്, നീല, പച്ച, മഞ്ഞ അങ്ങനെ പലതും.",
       S(("🌈", "So many colours!"), ("🔴", "Tap the right colour."), ("⭐", "Let us begin!")), picture_bank("colours"), "Names 6 colours")
lesson("shapes", L1, "🔺", "Shapes", "ആകൃതികൾ", "Circle, square, triangle and star.", "വൃത്തം, ചതുരം, ത്രികോണം, നക്ഷത്രം.",
       S(("⭕", "Shapes are everywhere!"), ("🔺", "Tap the right shape."), ("⭐", "Let us begin!")), picture_bank("shapes"), "Names 4 shapes")
lesson("people", L1, "👨‍👩‍👧", "My Family", "എന്റെ കുടുംബം", "Mother, father, grandparents and more.", "അമ്മ, അച്ഛൻ, അപ്പൂപ്പൻ, അമ്മൂമ്മ.",
       S(("👨‍👩‍👧", "This is a family."), ("👩", "Tap the right person."), ("⭐", "Let us begin!")), picture_bank("people"), "Knows family members")
lesson("body", L1, "🖐️", "My Body", "എന്റെ ശരീരം", "Eyes, nose, mouth, hands and more.", "കണ്ണ്, മൂക്ക്, വായ, കൈ അങ്ങനെ പലതും.",
       S(("🧒", "This is my body."), ("👁️", "Tap the right part."), ("⭐", "Let us begin!")), picture_bank("body"), "Names 6 body parts")
lesson("food", L1, "🍚", "Food and Drink", "ഭക്ഷണവും പാനീയവും", "Rice, milk, egg, tea and more.", "ചോറ്, പാല്, മുട്ട, ചായ അങ്ങനെ പലതും.",
       S(("🍚", "Time to eat!"), ("🥛", "Tap the right food."), ("⭐", "Let us begin!")), picture_bank("food"), "Names 10 foods")
lesson("feelings", L1, "😀", "Faces and Feelings", "മുഖവും വികാരങ്ങളും", "Happy, sad, angry, scared.", "സന്തോഷം, സങ്കടം, ദേഷ്യം, പേടി.",
       S(("😀", "Faces show feelings."), ("😢", "Tap the right face."), ("⭐", "Let us begin!")), picture_bank("feelings"), "Names 4 feelings")

lesson("birds", L2, "🦜", "Birds and Bugs", "പക്ഷികളും ജീവികളും", "Parrot, peacock, bee, ant and more.", "തത്ത, മയിൽ, തേനീച്ച, ഉറുമ്പ് അങ്ങനെ പലതും.",
       S(("🦜", "Birds and little creatures."), ("🐝", "Tap the right picture."), ("⭐", "Let us begin!")), picture_bank("birds"))
lesson("vegetables", L2, "🥕", "Vegetables", "പച്ചക്കറികൾ", "Carrot, tomato, onion and more.", "കാരറ്റ്, തക്കാളി, ഉള്ളി അങ്ങനെ പലതും.",
       S(("🥕", "Vegetables keep us strong."), ("🍅", "Tap the right picture."), ("⭐", "Let us begin!")), picture_bank("vegetables"))
lesson("vehicles", L2, "🚌", "Vehicles", "വാഹനങ്ങൾ", "Bus, train, aeroplane, auto and more.", "ബസ്, ട്രെയിൻ, വിമാനം, ഓട്ടോ അങ്ങനെ പലതും.",
       S(("🚌", "Vehicles take us places."), ("🚂", "Tap the right vehicle."), ("⭐", "Let us begin!")), picture_bank("vehicles"))
lesson("clothes", L2, "👕", "Clothes", "വസ്ത്രങ്ങൾ", "Shirt, shoe, cap, umbrella and more.", "ഷർട്ട്, ഷൂ, തൊപ്പി, കുട അങ്ങനെ പലതും.",
       S(("👕", "We wear clothes."), ("👟", "Tap the right picture."), ("⭐", "Let us begin!")), picture_bank("clothes"))
lesson("home", L2, "🏠", "Things at Home", "വീട്ടിലെ സാധനങ്ങൾ", "Bed, chair, door, clock and more.", "കട്ടിൽ, കസേര, വാതിൽ, ക്ലോക്ക് അങ്ങനെ പലതും.",
       S(("🏠", "Look around the house."), ("🛏️", "Tap the right thing."), ("⭐", "Let us begin!")), picture_bank("home"))
lesson("school", L2, "✏️", "School Things", "സ്കൂൾ സാധനങ്ങൾ", "Pencil, book, pen, ruler and more.", "പെൻസിൽ, പുസ്തകം, പേന, സ്കെയിൽ അങ്ങനെ പലതും.",
       S(("🏫", "Let us go to school."), ("✏️", "Tap the right thing."), ("⭐", "Let us begin!")), picture_bank("school"))
lesson("nature", L2, "🌳", "Nature and Weather", "പ്രകൃതിയും കാലാവസ്ഥയും", "Sun, moon, rain, tree and more.", "സൂര്യൻ, ചന്ദ്രൻ, മഴ, മരം അങ്ങനെ പലതും.",
       S(("🌳", "Nature is beautiful."), ("🌧️", "Tap the right picture."), ("⭐", "Let us begin!")), picture_bank("nature"))
lesson("actions", L2, "🏃", "What are they doing?", "എന്താ ചെയ്യുന്നത്?", "Running, walking, reading, eating.", "ഓടുന്നു, നടക്കുന്നു, വായിക്കുന്നു, കഴിക്കുന്നു.",
       S(("🏃", "People do many things."), ("📖", "Tap the right picture."), ("⭐", "Let us begin!")), picture_bank("actions"))
lesson("helpers", L2, "👩‍⚕️", "People Who Help Us", "നമ്മളെ സഹായിക്കുന്നവർ", "Doctor, teacher, police and more.", "ഡോക്ടർ, ടീച്ചർ, പോലീസ് അങ്ങനെ പലരും.",
       S(("👩‍⚕️", "Many people help us."), ("👮", "Tap the right person."), ("⭐", "Let us begin!")), picture_bank("helpers"))
lesson("places", L2, "🏥", "Places We Go", "നമ്മൾ പോകുന്ന സ്ഥലങ്ങൾ", "Hospital, shop, bank, park and more.", "ആശുപത്രി, കട, ബാങ്ക്, പാർക്ക് അങ്ങനെ പലതും.",
       S(("🏥", "We go to many places."), ("🏪", "Tap the right place."), ("⭐", "Let us begin!")), picture_bank("places"))

lesson("count", L3, "🔢", "Counting 1 to 10", "എണ്ണാം 1 മുതൽ 10 വരെ", "Count, compare, what comes next.", "എണ്ണാം, താരതമ്യം ചെയ്യാം, അടുത്തത് ഏത്.",
       S(("🔢", "Let us count together."), ("🍎", "Touch each one and count."), ("⭐", "Let us begin!")), counting_bank(), "Counts to 10")
lesson("sums", L3, "➕", "Add and Take Away", "കൂട്ടാം, കുറയ്ക്കാം", "Small sums with pictures.", "ചിത്രങ്ങൾ കൊണ്ട് ചെറിയ കണക്കുകൾ.",
       S(("➕", "Put together to add."), ("➖", "Take away to subtract."), ("⭐", "Let us begin!")), sums_bank(), "Adds within 10")
lesson("abc", L3, "🔤", "ABC Letters", "ABC അക്ഷരങ്ങൾ", "A for Apple, B for Ball.", "A for Apple, B for Ball.",
       S(("🍎", "A is for Apple."), ("⚽", "B is for Ball."), ("⭐", "Let us begin!")), letters_bank("abc"), "Knows 10 letters")
lesson("mal", L3, "അ", "Malayalam Letters", "മലയാളം അക്ഷരങ്ങൾ", "അ for അമ്മ, ആ for ആന.", "അ അമ്മ, ആ ആന.",
       S(("👩", "അ അമ്മ."), ("🐘", "ആ ആന."), ("⭐", "Let us begin!")), letters_bank("mal"), "Knows 6 Malayalam letters")
lesson("safety", L3, "🚦", "Stay Safe", "സുരക്ഷിതരായിരിക്കാം", "Roads, fire, strangers, water.", "റോഡ്, തീ, അപരിചിതർ, വെള്ളം.",
       S(("🚦", "Safety keeps us well."), ("🚸", "Think, then tap."), ("⭐", "Let us begin!")), life_bank("safety", LIFE_A), "Knows 5 safety rules")
lesson("signs", L3, "🚸", "Signs Around Us", "അടയാളങ്ങൾ", "Stop, no smoking, warning, toilet.", "നിൽക്കൂ, പുകവലി പാടില്ല, മുന്നറിയിപ്പ്, ടോയ്‌ലറ്റ്.",
       S(("🛑", "Signs tell us things."), ("🚸", "Think, then tap."), ("⭐", "Let us begin!")), life_bank("signs", LIFE_A), "Reads 5 signs")
lesson("routine", L3, "🪥", "Daily Routine", "ദിവസത്തെ ചിട്ടകൾ", "Washing, brushing, eating, sleeping.", "കൈ കഴുകൽ, പല്ല് തേയ്ക്കൽ, ഭക്ഷണം, ഉറക്കം.",
       S(("🪥", "Good habits every day."), ("🧼", "Think, then tap."), ("⭐", "Let us begin!")), life_bank("routine", LIFE_A), "Follows a routine")
lesson("manners", L3, "🤝", "Good Manners", "നല്ല പെരുമാറ്റം", "Thank you, sorry, sharing, helping.", "നന്ദി, ക്ഷമ, പങ്കുവയ്ക്കൽ, സഹായം.",
       S(("🙏", "Be kind and polite."), ("🤝", "Think, then tap."), ("⭐", "Let us begin!")), life_bank("manners", LIFE_B), "Uses polite words")
lesson("feelsit", L3, "🥰", "How Do I Feel?", "എനിക്ക് എന്ത് തോന്നുന്നു?", "Feelings in everyday situations.", "ദൈനംദിന സന്ദർഭങ്ങളിലെ വികാരങ്ങൾ.",
       S(("😀", "Feelings are okay."), ("🥰", "Think, then tap."), ("⭐", "Let us begin!")), life_bank("feelsit", LIFE_B), "Names feelings")
lesson("money", L3, "🪙", "Money and Shop", "പണവും കടയും", "Coins, notes, saving, buying.", "നാണയം, നോട്ട്, സമ്പാദ്യം, വാങ്ങൽ.",
       S(("🪙", "Money buys things."), ("🏪", "Think, then tap."), ("⭐", "Let us begin!")), life_bank("money", LIFE_B), "Buys one item")
lesson("time", L3, "🕰️", "Time and Days", "സമയവും ദിവസങ്ങളും", "Morning, night, days of the week.", "രാവിലെ, രാത്രി, ആഴ്ചയിലെ ദിവസങ്ങൾ.",
       S(("🕰️", "Time goes on."), ("📅", "Think, then tap."), ("⭐", "Let us begin!")), life_bank("time", LIFE_B), "Knows days of week")
lesson("opposites", L3, "↕️", "Opposites", "വിപരീതങ്ങൾ", "Big and small, hot and cold.", "വലുത് ചെറുത്, ചൂട് തണുപ്പ്.",
       S(("↕️", "Things have opposites."), ("🔥", "Think, then tap."), ("⭐", "Let us begin!")), life_bank("opposites", LIFE_B), "Pairs opposites")

LESSON_BY_ID = {l["id"]: l for l in LESSON_LIST}
LEVELS = [
    dict(id="start", en="Step 1", ml="ഒന്നാം ചുവട്", note_en="Look and match. Two big choices.", note_ml="നോക്കി തിരഞ്ഞെടുക്കാം. രണ്ട് വലിയ ഓപ്ഷനുകൾ."),
    dict(id="grow", en="Step 2", ml="രണ്ടാം ചുവട്", note_en="More words and more places.", note_ml="കൂടുതൽ വാക്കുകൾ, കൂടുതൽ സ്ഥലങ്ങൾ."),
    dict(id="shine", en="Step 3", ml="മൂന്നാം ചുവട്", note_en="Numbers, letters and everyday skills.", note_ml="സംഖ്യകൾ, അക്ഷരങ്ങൾ, ദൈനംദിന കഴിവുകൾ."),
]


def lessons_for(level):
    return [l for l in LESSON_LIST if l["level"] == level]


def total_questions():
    return sum(len(b) for b in BANK.values())


def build_options(q, n_choices, rng=random):
    """Pick the right answer and (n_choices - 1) wrong ones. Returns (list of opts, right index)."""
    kind = q["kind"]
    if kind == "odd":
        right = rng.choice(q["rights"])
        wrongs = [w for w in q["wrongs"] if w["en"] != q["anchor"]["en"]]
        picks = [q["anchor"]] + rng.sample(wrongs, min(max(n_choices - 2, 0), len(wrongs)))
        opts = picks + [right]
    else:
        right = q["rights"][0]
        wrongs = rng.sample(q["wrongs"], min(n_choices - 1, len(q["wrongs"])))
        opts = [right] + wrongs
    rng.shuffle(opts)
    return opts, next(i for i, o in enumerate(opts) if o is right)

QBY_ID = {q["id"]: q for b in BANK.values() for q in b}
'''

_SOURCES['storage'] = r'''
# Tiny JSON store: one file, one entry per nickname. Fine for a family laptop or a classroom PC.
# For a public site replace this with a proper database and real verifiable parental consent.
import contextlib
import datetime
import json
import os
import tempfile

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
PATH = os.path.join(DATA_DIR, "progress.json")

DEFAULT_PREFS = {
    "support": "auto",      # auto | full | some | free
    "show_words": True,     # words under pictures
    "size": "large",        # normal | large | huge
    "contrast": False,
    "calm": False,          # no animation
    "session_len": 6,       # questions per play: 4, 6, 8, 10
    "listen_lang": "app",   # app | ml | both
}
DEFAULT_PROFILE = {
    "level": "start", "xp": 0, "streak": 0, "last_day": "", "done": {}, "badges": [], "q_total": 0, "q_first": 0,
    "seconds": 0, "created": "", "flowers": 0, "lvl": {}, "run": {}, "miss": {}, "review": [], "stats": {},
    "goals": [], "note": "", "photos": [], "prefs": {}, "mix_best": 0, "plays": 0,
}
DEFAULT_SETTINGS = {"theme": "auto", "lang": "en", "last_profile": ""}


def _read():
    try:
        with open(PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        data = {}
    data.setdefault("profiles", {})
    data.setdefault("settings", dict(DEFAULT_SETTINGS))
    return data


def _write(data):
    os.makedirs(DATA_DIR, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=DATA_DIR, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    os.replace(tmp, PATH)


def profile_names():
    return sorted(_read()["profiles"].keys())


def load_profile(name):
    p = json.loads(json.dumps(DEFAULT_PROFILE))
    p.update(_read()["profiles"].get(name, {}))
    prefs = dict(DEFAULT_PREFS)
    prefs.update(p.get("prefs") or {})
    p["prefs"] = prefs
    if not p["created"]:
        p["created"] = datetime.date.today().isoformat()
    return p


def save_profile(name, profile):
    with edit() as d:
        d["profiles"][name] = profile


def delete_profile(name):
    with edit() as d:
        d["profiles"].pop(name, None)


def settings():
    s = dict(DEFAULT_SETTINGS)
    s.update(_read()["settings"])
    return s


def save_settings(s):
    with edit() as d:
        d["settings"] = s


@contextlib.contextmanager
def edit():
    data = _read()
    yield data
    _write(data)


def export_json(name):
    p = load_profile(name)
    p = dict(p)
    p["photos"] = [dict(name=x["name"]) for x in p.get("photos", [])]   # keep the export small
    return json.dumps({name: p}, ensure_ascii=False, indent=2)
'''

_SOURCES['ml_ui'] = r'''
# Malayalam interface text (spoken style). Key = the English sentence used in the app.
UI = {
    "A few questions from everything you have learned. Questions you found tricky come back gently.": "പഠിച്ച കാര്യങ്ങളിൽ നിന്ന് കുറച്ച് ചോദ്യങ്ങൾ. ബുദ്ധിമുട്ട് തോന്നിയ ചോദ്യങ്ങൾ പതുക്കെ വീണ്ടും വരും.",
    "A parent, guardian or teacher is with me and agrees": "അച്ഛനോ അമ്മയോ ടീച്ചറോ എന്റെ കൂടെയുണ്ട്, അവർക്ക് സമ്മതമാണ്",
    "A private note about what works for this child": "ഈ കുട്ടിക്ക് എന്താണ് ഫലിക്കുന്നത് എന്നതിനെക്കുറിച്ച് ഒരു സ്വകാര്യ കുറിപ്പ്",
    "A quick grown-up check, then you can see progress and settings.": "വലിയവർക്കായി ഒരു ചെറിയ പരിശോധന. അതുകഴിഞ്ഞാൽ പുരോഗതിയും സെറ്റിംഗ്സും കാണാം.",
    "Add photo": "ഫോട്ടോ ചേർക്കുക",
    "Add photos of family, friends, pets and favourite things. With two or more, a My World lesson appears in Step 1.": "വീട്ടുകാർ, കൂട്ടുകാർ, വളർത്തുമൃഗങ്ങൾ, ഇഷ്ടപ്പെട്ട സാധനങ്ങൾ എന്നിവയുടെ ഫോട്ടോ ചേർക്കൂ. രണ്ടോ അതിലധികമോ ഉണ്ടെങ്കിൽ ഒന്നാം ചുവടിൽ 'എന്റെ ലോകം' പാഠം വരും.",
    "Another round": "ഒന്നുകൂടി",
    "Auto starts with 2 choices and a glowing answer, then slowly gives less help as your child succeeds. Choose a fixed level if you prefer.": "ഓട്ടോ രണ്ട് ഓപ്ഷനും തിളങ്ങുന്ന ഉത്തരവുമായി തുടങ്ങും. കുട്ടി ശരിയാക്കുന്നതിനനുസരിച്ച് സഹായം പതുക്കെ കുറയ്ക്കും. ഇഷ്ടമുണ്ടെങ്കിൽ ഒരു നിശ്ചിത ലെവൽ തിരഞ്ഞെടുക്കാം.",
    "Back to lessons": "പാഠങ്ങളിലേക്ക്",
    "Both": "രണ്ടും",
    "Calm mode (no movement): off": "ശാന്ത മോഡ് (ചലനമില്ല): ഓഫ്",
    "Calm mode (no movement): on": "ശാന്ത മോഡ് (ചലനമില്ല): ഓൺ",
    "Choose a photo": "ഒരു ഫോട്ടോ തിരഞ്ഞെടുക്കൂ",
    "Delete this learner's data": "ഈ കുട്ടിയുടെ വിവരങ്ങൾ ഡിലീറ്റ് ചെയ്യുക",
    "Display": "കാഴ്ച",
    "Download progress (JSON)": "പുരോഗതി ഡൗൺലോഡ് ചെയ്യുക (JSON)",
    "Extra large": "വളരെ വലുത്",
    "First try and support": "ആദ്യ ശ്രമവും സഹായവും",
    "Great job!": "കൊള്ളാം!",
    "Hi {name}!": "ഹായ് {name}!",
    "Hi, I am Pyqoo!": "ഹായ്, ഞാൻ പിക്കൂ!",
    "High contrast: off": "ഉയർന്ന കോൺട്രാസ്റ്റ്: ഓഫ്",
    "High contrast: on": "ഉയർന്ന കോൺട്രാസ്റ്റ്: ഓൺ",
    "How much help?": "എത്ര സഹായം വേണം?",
    "Keep it": "വേണ്ട, വച്ചോളൂ",
    "Large": "വലുത്",
    "Last problem: {err}": "അവസാനത്തെ പ്രശ്നം: {err}",
    "Learning goals": "പഠന ലക്ഷ്യങ്ങൾ",
    "Learning since {date}": "{date} മുതൽ പഠിക്കുന്നു",
    "Lesson stars": "പാഠങ്ങളുടെ നക്ഷത്രങ്ങൾ",
    "Let us play! 🎮": "വാ, കളിക്കാം! 🎮",
    "Let us start ➜": "തുടങ്ങാം ➜",
    "Listen": "കേൾക്കാം",
    "Listen language": "കേൾക്കുന്ന ഭാഷ",
    "Malayalam voice: Sarvam is connected.": "മലയാളം ശബ്ദം: സർവം ബന്ധിപ്പിച്ചിട്ടുണ്ട്.",
    "Malayalam voice: saved audio clips are installed.": "മലയാളം ശബ്ദം: സേവ് ചെയ്ത ഓഡിയോ ക്ലിപ്പുകൾ ഉണ്ട്.",
    "Malayalam voice: using the browser voice. Add a Sarvam key in the app secrets for a natural voice.": "മലയാളം ശബ്ദം: ബ്രൗസറിന്റെ ശബ്ദമാണ് ഉപയോഗിക്കുന്നത്. സ്വാഭാവിക ശബ്ദത്തിന് ആപ്പ് സീക്രട്ട്സിൽ സർവം കീ ചേർക്കൂ.",
    "Mixed Review": "എല്ലാം ചേർത്ത് റിവ്യൂ",
    "My Garden": "എന്റെ പൂന്തോട്ടം",
    "My World photos": "എന്റെ ലോകം ഫോട്ടോകൾ",
    "Name for this photo": "ഈ ഫോട്ടോയുടെ പേര്",
    "New badge: <b>{name}</b>.": "പുതിയ ബാഡ്ജ്: <b>{name}</b>.",
    "Next ▶": "അടുത്തത് ▶",
    "Next ➜": "അടുത്തത് ➜",
    "Nice try! Look again.": "നല്ല ശ്രമം! ഒന്നുകൂടി നോക്കൂ.",
    "Nice try! Look again. The glowing one is a good choice.": "നല്ല ശ്രമം! ഒന്നുകൂടി നോക്കൂ. തിളങ്ങുന്നത് നല്ല ഉത്തരമാണ്.",
    "No Malayalam voice on this device. A parent can add a natural voice in Parent corner.": "ഈ ഫോണിൽ മലയാളം ശബ്ദമില്ല. രക്ഷിതാവിന് രക്ഷിതാവിന്റെ കോർണറിൽ നിന്ന് സ്വാഭാവിക ശബ്ദം ചേർക്കാം.",
    "No answers yet. Progress will show here.": "ഇതുവരെ ഉത്തരങ്ങളില്ല. പുരോഗതി ഇവിടെ കാണാം.",
    "Normal": "സാധാരണ",
    "Only a nickname, progress and the photos you add are stored, on this device. No ads, no chat, no timers. If you run this online for children, get verifiable parental consent as required by the DPDP Act and Rules.": "വിളിപ്പേര്, പുരോഗതി, നിങ്ങൾ ചേർക്കുന്ന ഫോട്ടോകൾ എന്നിവ മാത്രമേ ഈ ഉപകരണത്തിൽ സൂക്ഷിക്കൂ. പരസ്യമില്ല, ചാറ്റില്ല, ടൈമറില്ല. കുട്ടികൾക്കായി ഓൺലൈനിൽ ഇത് ഓടിക്കുന്നെങ്കിൽ DPDP നിയമപ്രകാരമുള്ള സ്ഥിരീകരിക്കാവുന്ന രക്ഷിതാവിന്റെ സമ്മതം വാങ്ങണം.",
    "Open": "തുറക്കുക",
    "Parent and teacher corner": "രക്ഷിതാവിന്റെയും ടീച്ചറുടെയും കോർണർ",
    "Pick a nickname (not the full name)": "ഒരു വിളിപ്പേര് തിരഞ്ഞെടുക്കൂ (മുഴുവൻ പേര് വേണ്ട)",
    "Picture size": "ചിത്രത്തിന്റെ വലുപ്പം",
    "Play again": "ഒന്നുകൂടി കളിക്കാം",
    "Play ➜": "കളിക്കാം ➜",
    "Privacy and safety": "സ്വകാര്യതയും സുരക്ഷയും",
    "Pyqoo Easy is learning support. It is not therapy, diagnosis or medical advice. No timers, no ads, no chat.": "പിക്കൂ ഈസി പഠനത്തിനുള്ള സഹായി മാത്രമാണ്. ഇത് ചികിത്സയോ രോഗനിർണയമോ വൈദ്യോപദേശമോ അല്ല. ടൈമറില്ല, പരസ്യമില്ല, ചാറ്റില്ല.",
    "Question bank: {q} questions in {l} lessons. Each play draws a few at random with new wrong choices, so repeats feel fresh.": "{l} പാഠങ്ങളിലായി {q} ചോദ്യങ്ങൾ. ഓരോ തവണയും കുറച്ച് ചോദ്യങ്ങൾ ക്രമരഹിതമായി വരും, തെറ്റായ ഓപ്ഷനുകളും മാറും. അതുകൊണ്ട് ആവർത്തിച്ചാലും പുതുമയുണ്ടാകും.",
    "Question {i} of {n}": "ചോദ്യം {i} / {n}",
    "Questions in each play": "ഓരോ കളിയിലും ചോദ്യങ്ങൾ",
    "Review done!": "റിവ്യൂ കഴിഞ്ഞു!",
    "Same as app": "ആപ്പിലെ ഭാഷ",
    "Save note": "കുറിപ്പ് സേവ് ചെയ്യുക",
    "See my flowers ➜": "എന്റെ പൂക്കൾ കാണാം ➜",
    "Skill": "കഴിവ്",
    "Skill progress": "കഴിവുകളുടെ പുരോഗതി",
    "Skip": "ഒഴിവാക്കുക",
    "Special badges": "പ്രത്യേക ബാഡ്ജുകൾ",
    "Start review ➜": "റിവ്യൂ തുടങ്ങാം ➜",
    "Switch learner": "കുട്ടിയെ മാറ്റുക",
    "Tap a lesson to make it a goal. Goals show up on the child screen as Today we try.": "പാഠത്തിൽ തൊട്ടാൽ അത് ലക്ഷ്യമാകും. ലക്ഷ്യങ്ങൾ കുട്ടിയുടെ സ്ക്രീനിൽ 'ഇന്ന് നമുക്ക് ശ്രമിക്കാം' എന്ന് കാണിക്കും.",
    "Teacher or parent note": "ടീച്ചറുടെയോ രക്ഷിതാവിന്റെയോ കുറിപ്പ്",
    "This browser cannot read aloud.": "ഈ ബ്രൗസറിന് വായിച്ച് കേൾപ്പിക്കാൻ പറ്റില്ല.",
    "This deletes all progress and photos for this learner. It cannot be undone.": "ഇത് ഈ കുട്ടിയുടെ എല്ലാ പുരോഗതിയും ഫോട്ടോകളും ഡിലീറ്റ് ചെയ്യും. തിരിച്ചെടുക്കാൻ പറ്റില്ല.",
    "Today we try": "ഇന്ന് നമുക്ക് ശ്രമിക്കാം",
    "Voice": "ശബ്ദം",
    "Welcome back": "വീണ്ടും സ്വാഗതം",
    "Welcome to <b>Pyqoo Easy</b>. Look, listen and tap. Learn at your own speed. There are no timers.": "<b>പിക്കൂ ഈസി</b>യിലേക്ക് സ്വാഗതം. നോക്കൂ, കേൾക്കൂ, തൊടൂ. നിങ്ങളുടെ വേഗത്തിൽ പഠിക്കാം. ടൈമറില്ല.",
    "Well done!": "കലക്കി!",
    "What is {q}?": "{q} എത്രയാ?",
    "Where should we start?": "എവിടെ നിന്ന് തുടങ്ങണം?",
    "Words under pictures: off": "ചിത്രത്തിന് താഴെ വാക്കുകൾ: ഓഫ്",
    "Words under pictures: on": "ചിത്രത്തിന് താഴെ വാക്കുകൾ: ഓൺ",
    "Yes, delete": "അതെ, ഡിലീറ്റ് ചെയ്യൂ",
    "You did it!": "നീ ചെയ്തു!",
    "You grew {f} flowers today!": "ഇന്ന് നീ {f} പൂക്കൾ വളർത്തി!",
    "day streak": "ദിവസം തുടർച്ച",
    "e.g. Anu": "ഉദാ. അനു",
    "first-try right": "ആദ്യശ്രമത്തിൽ ശരി",
    "flowers": "പൂക്കൾ",
    "one step at a time": "ഓരോ ചുവടായി",
    "lessons": "പാഠങ്ങൾ",
    "minutes": "മിനിറ്റ്",
    "or start a new learner": "അല്ലെങ്കിൽ പുതിയ കുട്ടിയെ ചേർക്കൂ",
    "stars": "നക്ഷത്രം",
    "to revisit": "വീണ്ടും നോക്കാൻ",
    "{done} of {total} lessons done. Every tap grows a flower!": "{total} പാഠങ്ങളിൽ {done} കഴിഞ്ഞു. ഓരോ തൊടലിലും ഒരു പൂവ് വളരും!",
    "{name} progress": "{name}-ന്റെ പുരോഗതി",
    "{n} flowers grown so far.": "ഇതുവരെ {n} പൂക്കൾ വളർന്നു.",
    "{q} questions to practise. Tricky ones waiting: <b>{r}</b>": "പരിശീലിക്കാൻ {q} ചോദ്യങ്ങൾ. വീണ്ടും നോക്കാനുള്ള ബുദ്ധിമുട്ടുള്ളവ: <b>{r}</b>",
    "◀ Back": "◀ പിന്നോട്ട്",
    "🔒 Lock": "🔒 ലോക്ക്",
    # labels passed through variables
    "🌓 Auto": "🌓 ഓട്ടോ", "☀️ Light": "☀️ വെളിച്ചം", "🌙 Dark": "🌙 ഇരുട്ട്",
    "🎒 Learn": "🎒 പഠിക്കാം", "🎯 Review": "🎯 റിവ്യൂ", "🌻 Garden": "🌻 തോട്ടം", "👪 Parent": "👪 രക്ഷിതാവ്",
    "Auto (grows with the child)": "ഓട്ടോ (കുട്ടിക്കൊപ്പം വളരും)",
    "Full help (2 choices, answer glows)": "പൂർണ്ണ സഹായം (2 ഓപ്ഷൻ, ഉത്തരം തിളങ്ങും)",
    "Some help (3 choices)": "കുറച്ച് സഹായം (3 ഓപ്ഷൻ)",
    "On my own (4 choices)": "തനിയെ (4 ഓപ്ഷൻ)",
    "Full help": "പൂർണ്ണ സഹായം", "Some help": "കുറച്ച് സഹായം", "On own": "തനിയെ",
    "Please type a nickname.": "ഒരു വിളിപ്പേര് ടൈപ്പ് ചെയ്യൂ.",
    "A parent, guardian or teacher needs to be with you. Tick the box when they are.": "അച്ഛനോ അമ്മയോ ടീച്ചറോ കൂടെ വേണം. അവർ ഉള്ളപ്പോൾ ബോക്സിൽ ടിക്ക് ചെയ്യൂ.",
    "That is not right. Try again.": "ശരിയായില്ല. ഒന്നുകൂടി നോക്കൂ.",
    "Choose a photo and type a name.": "ഒരു ഫോട്ടോ തിരഞ്ഞെടുത്ത് പേര് ടൈപ്പ് ചെയ്യൂ.",
    "You can keep up to 12 photos.": "12 ഫോട്ടോ വരെ വയ്ക്കാം.",
    "That photo could not be read.": "ആ ഫോട്ടോ വായിക്കാൻ പറ്റിയില്ല.",
    # badges
    "First Flower": "ആദ്യ പൂവ്", "Finish your first lesson": "ആദ്യത്തെ പാഠം തീർക്കൂ",
    "Busy Bee": "തിരക്കുള്ള തേനീച്ച", "Finish 5 lessons": "5 പാഠം തീർക്കൂ",
    "Come Back Star": "തിരിച്ചുവരവിന്റെ നക്ഷത്രം", "Learn on 3 days in a row": "തുടർച്ചയായി 3 ദിവസം പഠിക്കൂ",
    "Little Garden": "കൊച്ചുതോട്ടം", "Grow 50 flowers": "50 പൂക്കൾ വളർത്തൂ",
    "Big Garden": "വലിയ തോട്ടം", "Grow 200 flowers": "200 പൂക്കൾ വളർത്തൂ",
    "Step 1 Done": "ഒന്നാം ചുവട് കഴിഞ്ഞു", "Finish every Step 1 lesson": "ഒന്നാം ചുവടിലെ എല്ലാ പാഠവും തീർക്കൂ",
    "Step 2 Done": "രണ്ടാം ചുവട് കഴിഞ്ഞു", "Finish every Step 2 lesson": "രണ്ടാം ചുവടിലെ എല്ലാ പാഠവും തീർക്കൂ",
    "Step 3 Done": "മൂന്നാം ചുവട് കഴിഞ്ഞു", "Finish every Step 3 lesson": "മൂന്നാം ചുവടിലെ എല്ലാ പാഠവും തീർക്കൂ",
    "Mix Master": "മിക്സ് മാസ്റ്റർ", "Finish a Mixed Review": "ഒരു മിക്സഡ് റിവ്യൂ തീർക്കൂ",
    "Pyqoo Champion": "പിക്കൂ ചാമ്പ്യൻ", "Finish every lesson": "എല്ലാ പാഠവും തീർക്കൂ",
    # story cards
    "A is for Apple.": "A എന്നാൽ ആപ്പിൾ.",
    "B is for Ball.": "B എന്നാൽ ബോൾ.",
    "Be kind and polite.": "സ്നേഹത്തോടെ, മര്യാദയോടെ പെരുമാറാം.",
    "Birds and little creatures.": "പക്ഷികളും ചെറിയ ജീവികളും.",
    "Faces show feelings.": "മുഖം നമ്മുടെ വികാരങ്ങൾ കാണിക്കും.",
    "Feelings are okay.": "ഏത് വികാരം തോന്നിയാലും സാരമില്ല.",
    "Good habits every day.": "എന്നും നല്ല ശീലങ്ങൾ.",
    "Let us begin!": "തുടങ്ങാം!",
    "Let us count together.": "നമുക്ക് ഒരുമിച്ച് എണ്ണാം.",
    "Let us go to school.": "നമുക്ക് സ്കൂളിൽ പോകാം.",
    "Look around the house.": "വീടിന് ചുറ്റും നോക്കൂ.",
    "Look at the animals!": "മൃഗങ്ങളെ നോക്കൂ!",
    "Look at the photo, then tap the name.": "ഫോട്ടോ നോക്കൂ, എന്നിട്ട് പേരിൽ തൊടൂ.",
    "Many people help us.": "പലരും നമ്മളെ സഹായിക്കുന്നുണ്ട്.",
    "Money buys things.": "പണം കൊടുത്താൽ സാധനങ്ങൾ വാങ്ങാം.",
    "Nature is beautiful.": "പ്രകൃതി എത്ര ഭംഗിയാണ്.",
    "People do many things.": "ആളുകൾ പലതും ചെയ്യും.",
    "Put together to add.": "ചേർത്തുവച്ചാൽ കൂട്ടാം.",
    "Safety keeps us well.": "സുരക്ഷ നമ്മളെ സുഖമായി വയ്ക്കും.",
    "Shapes are everywhere!": "ആകൃതികൾ എല്ലായിടത്തുമുണ്ട്!",
    "Signs tell us things.": "അടയാളങ്ങൾ നമ്മോട് പലതും പറയും.",
    "So many colours!": "എത്ര നിറങ്ങൾ!",
    "Take away to subtract.": "എടുത്തുമാറ്റിയാൽ കുറയ്ക്കാം.",
    "Tap the right colour.": "ശരിയായ നിറത്തിൽ തൊടൂ.",
    "Tap the right face.": "ശരിയായ മുഖത്തിൽ തൊടൂ.",
    "Tap the right food.": "ശരിയായ ഭക്ഷണത്തിൽ തൊടൂ.",
    "Tap the right part.": "ശരിയായ ഭാഗത്തിൽ തൊടൂ.",
    "Tap the right person.": "ശരിയായ ആളിൽ തൊടൂ.",
    "Tap the right picture.": "ശരിയായ ചിത്രത്തിൽ തൊടൂ.",
    "Tap the right place.": "ശരിയായ സ്ഥലത്തിൽ തൊടൂ.",
    "Tap the right shape.": "ശരിയായ ആകൃതിയിൽ തൊടൂ.",
    "Tap the right thing.": "ശരിയായ സാധനത്തിൽ തൊടൂ.",
    "Tap the right vehicle.": "ശരിയായ വണ്ടിയിൽ തൊടൂ.",
    "These are your own people and things.": "ഇത് നിങ്ങളുടെ സ്വന്തം ആളുകളും സാധനങ്ങളുമാണ്.",
    "Things have opposites.": "എല്ലാത്തിനും വിപരീതമുണ്ട്.",
    "Think, then tap.": "ആലോചിക്കൂ, എന്നിട്ട് തൊടൂ.",
    "This is a family.": "ഇതൊരു കുടുംബമാണ്.",
    "This is my body.": "ഇത് എന്റെ ശരീരമാണ്.",
    "Time goes on.": "സമയം പോയിക്കൊണ്ടിരിക്കും.",
    "Time to eat!": "കഴിക്കാൻ സമയമായി!",
    "Touch each one and count.": "ഓരോന്നിലും തൊട്ട് എണ്ണൂ.",
    "Vegetables keep us strong.": "പച്ചക്കറി നമ്മളെ ആരോഗ്യമുള്ളവരാക്കും.",
    "Vehicles take us places.": "വണ്ടികൾ നമ്മളെ പലയിടത്തും കൊണ്ടുപോകും.",
    "We go to many places.": "നമ്മൾ പല സ്ഥലങ്ങളിലും പോകും.",
    "We wear clothes.": "നമ്മൾ വസ്ത്രം ധരിക്കും.",
    "You can do it!": "നിനക്ക് പറ്റും!",
    "Yummy fruits!": "രുചിയുള്ള പഴങ്ങൾ!",
    "അ അമ്മ.": "അ അമ്മ.",
    "ആ ആന.": "ആ ആന.",
}

# English words used in lesson Step names are handled by content (en / ml fields).
'''

_SOURCES['i18n'] = r'''
# Language layer. T("English sentence {x}", x=1) returns the Malayalam text when the language is Malayalam.
# A missing translation simply shows English (the test suite reports those).
import streamlit as st

import ml_ui

MISSING = set()
LANGS = ("en", "ml")


def lang():
    try:
        return st.session_state.get("lang", "en")
    except Exception:
        return "en"


def T(en, **kw):
    text = en
    if lang() == "ml":
        found = ml_ui.UI.get(en)
        if found is None:
            MISSING.add(en)
        else:
            text = found
    return text.format(**kw) if kw else text


def pick(en, ml):
    """Choose between two texts for the current language (used for question data)."""
    return ml if lang() == "ml" else en
'''

_SOURCES['ui'] = r'''
# Look and feel: light, dark and auto themes, plus small HTML helpers.
import html

import streamlit as st

LIGHT = {
    "bg": "#F3F8F6", "card": "#FFFFFF", "ink": "#16302C", "muted": "#566D68", "line": "#D9E6E2",
    "brand": "#0B7A75", "brand-ink": "#FFFFFF", "brand-soft": "#DDF1EF",
    "sun": "#F5A524", "sun-ink": "#3B2800", "sun-soft": "#FFF0D2",
    "good": "#17803F", "good-soft": "#DEF3E5", "bad": "#B8430F", "bad-soft": "#FDE6DA",
    "shadow": "0 8px 24px rgba(22,48,44,.08)", "scheme": "light",
}
DARK = {
    "bg": "#0C1A19", "card": "#15292A", "ink": "#E8F3F0", "muted": "#9DB7B1", "line": "#27403F",
    "brand": "#2FC1B8", "brand-ink": "#04211F", "brand-soft": "#17403F",
    "sun": "#F7B63F", "sun-ink": "#2A1C00", "sun-soft": "#3A2E12",
    "good": "#4BD08A", "good-soft": "#143A27", "bad": "#FF9B6B", "bad-soft": "#42241A",
    "shadow": "0 8px 24px rgba(0,0,0,.35)", "scheme": "dark",
}


def _vars(tokens):
    return ";".join(f"--{k}:{v}" for k, v in tokens.items() if k != "scheme") + f";color-scheme:{tokens['scheme']}"


def theme_css(mode):
    if mode == "dark":
        root = f":root{{{_vars(DARK)}}}"
    elif mode == "light":
        root = f":root{{{_vars(LIGHT)}}}"
    else:
        root = f":root{{{_vars(LIGHT)}}}@media (prefers-color-scheme: dark){{:root{{{_vars(DARK)}}}}}"
    return root


BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Baloo+Chettan+2:wght@600;700;800&family=Lexend:wght@400;500;600&family=Noto+Sans+Malayalam:wght@400;500;600;700&display=swap');
html,body,.stApp,[data-testid="stAppViewContainer"]{background:var(--bg)!important;color:var(--ink)}
.stApp{font-family:'Lexend','Noto Sans Malayalam',system-ui,sans-serif}
[data-testid="stHeader"],header[data-testid="stHeader"]{display:none!important;pointer-events:none!important}
[data-testid="stToolbar"],[data-testid="stDecoration"],footer,#MainMenu{display:none!important}
.block-container{max-width:760px!important;padding:1rem 16px 5rem!important}
.stApp p,.stApp li,.stApp label,.stApp span,.stApp div[data-testid="stMarkdownContainer"]{color:inherit}
h1,h2,h3,.nk-title{font-family:'Baloo 2','Baloo Chettan 2','Noto Sans Malayalam','Lexend','Noto Sans Malayalam',sans-serif!important;color:var(--ink)!important;letter-spacing:0}
[data-testid="stVerticalBlock"]{gap:.7rem}

/* keep rows side by side on phones */
[class*="st-key-ns-"] [data-testid="stHorizontalBlock"]{flex-direction:row!important;flex-wrap:nowrap!important;gap:.5rem!important}
[class*="st-key-ns-"] [data-testid="stColumn"],[class*="st-key-ns-"] [data-testid="column"]{min-width:0!important}

/* buttons */
.stButton,[data-testid="stElementContainer"]:has(>.stButton),[data-testid="stButton"]{width:100%!important}
.stButton>button,[data-testid="stButton"]>button{width:100%!important;min-height:3rem;border-radius:16px;border:2px solid var(--line);background:var(--card);color:var(--ink);
  font-family:'Lexend','Noto Sans Malayalam',sans-serif;font-weight:600;box-shadow:0 3px 0 var(--line);transition:transform .08s,border-color .15s;padding:.4rem .8rem}
.stButton>button:hover{border-color:var(--brand);color:var(--brand)}
.stButton>button:active{transform:translateY(2px);box-shadow:0 1px 0 var(--line)}
.stButton>button:focus-visible{outline:3px solid var(--sun);outline-offset:2px}
.stButton>button[kind="primary"],.stButton>button[data-testid="stBaseButton-primary"]{background:var(--brand);color:var(--brand-ink);border-color:var(--brand);box-shadow:0 3px 0 rgba(0,0,0,.28)}
.stButton>button[kind="primary"]:hover,.stButton>button[data-testid="stBaseButton-primary"]:hover{filter:brightness(1.06);color:var(--brand-ink)}
.stButton>button p,.stButton>button div{color:inherit!important;margin:0;font-weight:inherit}
.stButton>button:disabled{opacity:.55;cursor:not-allowed}

/* answer states */
[class*="st-key-ok-"] .stButton>button{background:var(--good-soft);border-color:var(--good);color:var(--good);box-shadow:0 3px 0 var(--good)}
[class*="st-key-no-"] .stButton>button{background:var(--bad-soft);border-color:var(--bad);color:var(--bad);box-shadow:none;opacity:.9}
[class*="st-key-sel-"] .stButton>button{background:var(--brand-soft);border-color:var(--brand);color:var(--brand)}
[class*="st-key-tab-on"] .stButton>button{background:var(--brand);color:var(--brand-ink);border-color:var(--brand)}
[class*="st-key-tile-"] .stButton>button{min-height:4.4rem;font-size:1.05rem}
[class*="st-key-tile-"] .stButton>button p{font-size:1.05rem;line-height:1.2}
[class*="st-key-big-"] .stButton>button{min-height:3.6rem;font-size:1.1rem}

/* inputs */
[data-baseweb="input"],[data-baseweb="base-input"],.stTextInput input{background:var(--card)!important;color:var(--ink)!important;border-radius:14px!important}
[data-baseweb="input"]{border:2px solid var(--line)!important}
.stTextInput label p,.stTextInput label{color:var(--muted)!important}
.stTextInput input::placeholder{color:var(--muted)!important;opacity:.8}
.stDownloadButton>button{width:100%;border-radius:16px;border:2px solid var(--line);background:var(--card);color:var(--ink);min-height:3rem;font-weight:600}
.stDownloadButton>button p{color:inherit!important}
[data-testid="stAlert"]{border-radius:14px}

/* cards */
[class*="st-key-card-"]{background:var(--card);border:2px solid var(--line);border-radius:22px;padding:14px 16px;box-shadow:var(--shadow)}
.nk-hero{background:linear-gradient(135deg,var(--brand),#065a57);color:#fff;border-radius:26px;padding:18px 18px 16px;box-shadow:var(--shadow);position:relative;overflow:hidden}
.nk-hero *{color:#fff!important}
.nk-hero .nk-title{font-size:1.65rem;font-weight:800;line-height:1.15;margin:0 0 4px}
.nk-hero small{opacity:.9}
.nk-mascot{position:absolute;right:12px;top:8px;font-size:3.1rem;filter:drop-shadow(0 4px 0 rgba(0,0,0,.18))}
.nk-card{background:var(--card);border:2px solid var(--line);border-radius:22px;padding:14px 16px;box-shadow:var(--shadow)}
.nk-title{font-weight:800;font-size:1.25rem;margin:0}
.nk-sub{color:var(--muted)!important;font-size:.92rem;margin:2px 0 0}
.nk-row{display:flex;align-items:center;gap:12px}
.nk-art{width:54px;height:54px;border-radius:16px;background:var(--brand-soft);display:grid;place-items:center;font-size:1.9rem;flex:none}
.nk-grow{flex:1;min-width:0}
.nk-pill{display:inline-block;padding:2px 10px;border-radius:99px;background:var(--brand-soft);color:var(--brand)!important;font-weight:600;font-size:.78rem}
.nk-pill.sun{background:var(--sun-soft);color:var(--sun)!important}
.nk-stars{letter-spacing:2px;font-size:1.05rem}
.nk-bar{height:14px;border-radius:99px;background:var(--line);overflow:hidden}
.nk-bar>i{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,var(--sun),#ffcf6b)}
.nk-bar.brand>i{background:linear-gradient(90deg,var(--brand),#43c9c0)}
.nk-stats{display:flex;gap:8px}
.nk-stat{flex:1;background:var(--card);border:2px solid var(--line);border-radius:18px;padding:8px 6px;text-align:center}
.nk-stat b{display:block;font-family:'Baloo 2','Baloo Chettan 2','Noto Sans Malayalam',sans-serif;font-size:1.35rem;line-height:1.1}
.nk-stat span{font-size:.72rem;color:var(--muted)!important}
.nk-story{background:var(--card);border:2px solid var(--line);border-radius:26px;padding:22px 18px;text-align:center;box-shadow:var(--shadow)}
.nk-story .em{font-size:4.2rem;line-height:1.1}
.nk-story p{font-size:1.2rem;line-height:1.5;margin:10px 0 0;font-weight:500}
.nk-q{background:var(--card);border:2px solid var(--line);border-radius:22px;padding:16px 18px;font-size:1.15rem;font-weight:600;line-height:1.4}
.nk-fb{border-radius:16px;padding:12px 14px;font-weight:500;line-height:1.45}
.nk-fb.ok{background:var(--good-soft);color:var(--good)!important;border:2px solid var(--good)}
.nk-fb.no{background:var(--bad-soft);color:var(--bad)!important;border:2px solid var(--bad)}
.nk-fb.hint{background:var(--sun-soft);color:var(--ink)!important;border:2px solid var(--sun)}
.nk-fb *{color:inherit!important}
.nk-dots{display:flex;gap:6px;justify-content:center;flex-wrap:nowrap}
.nk-dot{width:13px;height:13px;border-radius:50%;background:var(--line);flex:none}
.nk-dot.on{background:var(--brand)}.nk-dot.cur{background:var(--sun)}
.nk-big{font-family:'Baloo 2','Baloo Chettan 2','Noto Sans Malayalam',sans-serif;font-size:2.4rem;font-weight:800;text-align:center;line-height:1.1}
.nk-big small{display:block;font-size:.8rem;color:var(--muted);font-weight:500;font-family:'Lexend','Noto Sans Malayalam',sans-serif}
.nk-money{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;min-height:42px}
.nk-money span{background:var(--sun-soft);border:2px solid var(--sun);border-radius:99px;padding:2px 10px;font-weight:600;font-size:.95rem}
.nk-jar{display:flex;align-items:center;gap:10px}
.nk-jar .bar{flex:1}
.nk-badge{background:var(--card);border:2px solid var(--line);border-radius:20px;padding:12px 6px;text-align:center}
.nk-badge .em{font-size:2rem}.nk-badge.locked{opacity:.4;filter:grayscale(1)}
.nk-badge b{display:block;font-size:.78rem;line-height:1.2;margin-top:2px}
.nk-badge span{font-size:.68rem;color:var(--muted)!important}
.nk-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.nk-table{width:100%;border-collapse:collapse;font-size:.9rem}
.nk-table td,.nk-table th{padding:6px 4px;border-bottom:1px solid var(--line);text-align:left}
.nk-table th{color:var(--muted);font-weight:600;font-size:.78rem}
.nk-foot b{color:inherit}
.nk-foot{font-size:.75rem;color:var(--muted)!important;text-align:center;margin-top:24px;line-height:1.5}
.nk-seg{display:flex;gap:6px}
.nk-seg b{flex:1;text-align:center;padding:6px 4px;border-radius:12px;background:var(--brand-soft);font-size:.8rem}
@keyframes pop{0%{transform:scale(.7);opacity:0}70%{transform:scale(1.08)}100%{transform:scale(1);opacity:1}}
.nk-pop{animation:pop .45s ease both}
@media (prefers-reduced-motion:reduce){.nk-pop{animation:none}.stButton>button{transition:none}}
"""


ML_CSS = ".stApp{line-height:1.75}.nk-title,.nk-q,.nk-story p{line-height:1.45!important}.stButton>button p{line-height:1.4;font-size:.9rem}[class*='st-key-ns-'] .stButton>button p{font-size:.78rem}[class*='st-key-ns-'] .stButton>button{padding-left:4px!important;padding-right:4px!important}.nk-hero p,.nk-hero .nk-sub{padding-right:52px}.nk-hero .nk-title{font-size:1.4rem}"


EXTRA_CSS = """
.stButton>button p{white-space:pre-line}
[class*="-tile-"] .stButton>button{min-height:var(--tile-h,7rem);padding:.5rem .4rem;line-height:1.1}
[class*="-tile-"] .stButton>button p{font-size:1.02rem;line-height:1.25;font-weight:700}
[class*="-tile-"] .stButton>button p::first-line{font-size:var(--tile-e,3rem);line-height:1.3}
[class*="-stack-"] .stButton>button{min-height:var(--stack-h,4rem);font-size:1.12rem;justify-content:flex-start;text-align:left}
[class*="-stack-"] .stButton>button p{font-size:1.1rem;line-height:1.3;font-weight:600}
[class*="glow-"] .stButton>button{border-color:var(--sun)!important;background:var(--sun-soft)!important;box-shadow:0 0 0 4px var(--sun),0 3px 0 var(--sun)!important;animation:glow 1.6s ease-in-out infinite}
@keyframes glow{0%,100%{box-shadow:0 0 0 3px var(--sun),0 3px 0 var(--sun)}50%{box-shadow:0 0 0 7px rgba(245,165,36,.45),0 3px 0 var(--sun)}}
[class*="fade-"] .stButton>button{opacity:.28;filter:grayscale(1);box-shadow:none}
.nk-big-pic{background:var(--card);border:2px solid var(--line);border-radius:26px;padding:12px 10px;text-align:center;font-size:var(--big,4.6rem);line-height:1.2;word-break:break-all;box-shadow:var(--shadow)}
.nk-big-pic.small{font-size:2.2rem}
.nk-qtext{font-family:'Baloo 2','Baloo Chettan 2','Noto Sans Malayalam','Lexend',sans-serif;font-size:1.45rem;font-weight:700;line-height:1.35;text-align:center;padding:6px 4px}
.nk-garden{display:flex;flex-wrap:wrap;gap:2px;justify-content:center;font-size:1.7rem;min-height:2.2rem;letter-spacing:2px}
.nk-goal{border-left:6px solid var(--sun)}
.nk-photo{border-radius:22px;overflow:hidden}
:root{--tile-h:7rem;--tile-e:3rem;--stack-h:4rem;--big:4.6rem}
"""
SIZE_CSS = {
    "normal": ":root{--tile-h:5.6rem;--tile-e:2.4rem;--stack-h:3.4rem;--big:3.6rem}",
    "large": ":root{--tile-h:7rem;--tile-e:3rem;--stack-h:4rem;--big:4.6rem}",
    "huge": ":root{--tile-h:9rem;--tile-e:4.2rem;--stack-h:5rem;--big:6rem}.stButton>button p{font-size:1.2rem}",
}
CONTRAST_CSS = ":root{--line:#000;--ink:#000;--muted:#222}.stApp{--card:#FFFFFF}.stButton>button{border-width:4px!important;border-color:#000!important}[data-theme='dark'] .stButton>button{border-color:#fff!important}"
CALM_CSS = ".nk-pop{animation:none!important}[class*='glow-'] .stButton>button{animation:none!important}"


def inject(mode, lang="en", prefs=None):
    prefs = prefs or {}
    extra = ML_CSS if lang == "ml" else ""
    css = theme_css(mode) + BASE_CSS + EXTRA_CSS + SIZE_CSS.get(prefs.get("size", "large"), "") + extra
    if prefs.get("contrast"):
        css += CONTRAST_CSS
        if mode == "dark":
            css += ":root{--ink:#fff;--muted:#eee;--card:#000;--line:#fff}"
    if prefs.get("calm"):
        css += CALM_CSS
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def esc(x):
    return html.escape(str(x), quote=True)


def md(s):
    """Render an HTML string (blank lines would break the block, so squeeze them)."""
    flat = "".join(line.strip() for line in s.strip().splitlines())
    st.markdown(flat, unsafe_allow_html=True)


def stars(n, total=3):
    return "★" * n + "☆" * (total - n)


def bar(pct, brand=False):
    pct = max(0, min(100, pct))
    return f'<div class="nk-bar{" brand" if brand else ""}"><i style="width:{pct:.0f}%"></i></div>'


def dots(n, cur, total):
    out = []
    for i in range(total):
        cls = "on" if i < n else ("cur" if i == cur else "")
        out.append(f'<span class="nk-dot {cls}"></span>')
    return f'<div class="nk-dots">{"".join(out)}</div>'


def inr(x):
    """Indian digit grouping: 1,23,456."""
    x = int(round(x))
    sign = "-" if x < 0 else ""
    s = str(abs(x))
    if len(s) <= 3:
        return f"{sign}₹{s}"
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return f"{sign}₹{','.join(parts)},{tail}"
'''

_SOURCES['voice'] = r'''
"""Read-aloud. English and Malayalam use the browser voice by default.

For a natural Malayalam voice, add a Sarvam AI key (https://www.sarvam.ai). Set it in
.streamlit/secrets.toml (or the Streamlit Cloud "Secrets" box) or as an environment variable:

    SARVAM_API_KEY = "your-key"
    SARVAM_MODEL   = "bulbul:v4-flash" # optional
    SARVAM_SPEAKER = "shilpa_hi_narration"  # optional, must match the model
    SARVAM_PACE    = "1.0"            # optional

Audio is requested only when the Listen button is pressed, and each sentence is cached.
"""
import base64
import hashlib
import json
import os
import urllib.error
import urllib.request

import streamlit as st

from i18n import T, lang

SARVAM_URL = "https://api.sarvam.ai/text-to-speech"
LANG_CODE = {"en": "en-IN", "ml": "ml-IN"}


def _secret(name, default=""):
    value = None
    try:
        value = st.secrets.get(name)
    except Exception:
        value = None
    return str(value) if value else os.environ.get(name, default)


AUDIO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio", "ml")


def clip_name(text):
    """File name of a pre-made clip. make_audio.py uses the same function."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:16] + ".mp3"


def premade(text):
    path = os.path.join(AUDIO_DIR, clip_name(text))
    return path if os.path.isfile(path) else None


def sarvam_ready():
    return bool(_secret("SARVAM_API_KEY"))


@st.cache_data(show_spinner=False, max_entries=500, ttl=7 * 24 * 3600)
def _sarvam_audio(text, code, model, speaker, pace):
    """Returns WAV bytes. Raises on any failure, so failures are never cached."""
    key = _secret("SARVAM_API_KEY")
    if not key:
        raise RuntimeError("No Sarvam key")
    body = {"text": text[:1400], "target_language_code": code, "model": model, "speaker": speaker, "pace": pace,
            "speech_sample_rate": 24000}
    req = urllib.request.Request(
        SARVAM_URL, data=json.dumps(body).encode("utf-8"), method="POST",
        headers={"Content-Type": "application/json", "api-subscription-key": key})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError("Sarvam %s: %s" % (exc.code, exc.read().decode("utf-8", "ignore")[:120]))
    return base64.b64decode(data["audios"][0])


def status():
    if sarvam_ready():
        err = st.session_state.get("voice_err")
        base = T("Malayalam voice: Sarvam is connected.")
        return base + (" " + T("Last problem: {err}", err=err) if err else "")
    if os.path.isdir(AUDIO_DIR) and os.listdir(AUDIO_DIR):
        return T("Malayalam voice: saved audio clips are installed.")
    return T("Malayalam voice: using the browser voice. Add a Sarvam key in the app secrets for a natural voice.")


LISTEN_HTML = """
<style>
html,body{margin:0;background:transparent;font-family:system-ui,'Noto Sans Malayalam',sans-serif}
button{display:inline-flex;gap:8px;align-items:center;min-height:40px;padding:0 16px;border-radius:99px;background:#F5A524;color:#3B2800;font-weight:700;font-size:14px;border:0;cursor:pointer;font-family:inherit}
button:focus-visible{outline:3px solid #0B7A75;outline-offset:2px}
#n{font-size:12px;color:#7a8b87;margin-top:4px}
</style>
<button id="b" type="button">__LABEL__</button><div id="n" hidden></div>
<script>
const T=__TEXT__, L=__LANG__, NOVOICE=__NOVOICE__, NOSPEECH=__NOSPEECH__;
document.getElementById('b').addEventListener('click',function(){
  const n=document.getElementById('n');
  try{
    const s=window.speechSynthesis;
    if(!s||!window.SpeechSynthesisUtterance){n.textContent=NOSPEECH;n.hidden=false;return}
    s.cancel();const u=new SpeechSynthesisUtterance(T);u.lang=L;u.rate=.9;
    const want=L.toLowerCase(),vs=s.getVoices()||[];
    const v=vs.find(function(x){return x.lang.replace('_','-').toLowerCase()===want})||vs.find(function(x){return x.lang.toLowerCase().indexOf(want.slice(0,2))===0});
    if(v){u.voice=v}else if(want.indexOf('ml')===0&&vs.length){n.textContent=NOVOICE;n.hidden=false;return}
    s.speak(u);
  }catch(e){}
});
</script>
"""


def _browser_widget(text, code):
    page = (LISTEN_HTML.replace("__LABEL__", "🔊 " + T("Listen"))
            .replace("__TEXT__", json.dumps(text))
            .replace("__LANG__", json.dumps(code))
            .replace("__NOVOICE__", json.dumps(T("No Malayalam voice on this device. A parent can add a natural voice in Parent corner.")))
            .replace("__NOSPEECH__", json.dumps(T("This browser cannot read aloud."))))
    if hasattr(st, "iframe"):
        st.iframe(page.strip(), height=70)
    else:  # Streamlit 1.41 to 1.5x
        import streamlit.components.v1 as components
        components.html(page, height=70)


def _play(text):
    st.session_state.voice_play = text


def listen(text, force=None):
    """Show a Listen control for text in the current language (or force='ml')."""
    ss = st.session_state
    which = force or lang()
    if which == "ml" and (sarvam_ready() or premade(text)):
        tag = hashlib.md5(text.encode("utf-8")).hexdigest()[:10]
        st.button("🔊 " + T("Listen"), key=f"listen-{tag}", on_click=_play, args=(text,))
        if ss.get("voice_play") == text:
            ss.voice_play = None            # play once, then clear
            try:
                clip = premade(text)
                if clip:                    # saved clip: no Sarvam call, no cost
                    with open(clip, "rb") as fh:
                        ss.voice_err = ""
                        st.audio(fh.read(), format="audio/mp3", autoplay=True)
                    return
                audio = _sarvam_audio(text, LANG_CODE["ml"], _secret("SARVAM_MODEL", "bulbul:v4-flash"),
                                      _secret("SARVAM_SPEAKER", "shilpa_hi_narration"), float(_secret("SARVAM_PACE", "1.0")))
                ss.voice_err = ""
                st.audio(audio, format="audio/wav", autoplay=True)
            except Exception as exc:       # fall back to the browser voice below
                ss.voice_err = str(exc)[:160]
                _browser_widget(text, LANG_CODE["ml"])
        return
    _browser_widget(text, LANG_CODE.get(which, "en-IN"))
'''

_HERE = _os.path.dirname(_os.path.abspath(__file__))
for _name in ('items_a', 'items_b', 'items_c', 'life_a', 'life_b', 'content', 'storage', 'ml_ui', 'i18n', 'ui', 'voice'):
    _bid = _hl.md5(_SOURCES[_name].encode('utf-8')).hexdigest()
    if getattr(_sys.modules.get(_name), '_pe_build', None) != _bid:
        _mod = _types.ModuleType(_name)
        _mod._pe_build = _bid
        _mod.__file__ = _os.path.join(_HERE, _name + '.py')
        _sys.modules[_name] = _mod
        exec(compile(_SOURCES[_name], _mod.__file__, 'exec'), _mod.__dict__)

# ===== APP =====
# Pyqoo Easy: gentle, picture-first learning for children with learning difficulties.
# Run:  streamlit run app.py
#
# Learning support only. No therapy or medical claims. No timers, no negative scores, no ads.
import base64
import datetime
import io
import random
import time

import streamlit as st

import content as C
import i18n
import storage
import ui
import voice
from i18n import T, pick as PK
from ui import esc, md

st.set_page_config(page_title="Pyqoo Easy", page_icon="🦉", layout="centered", initial_sidebar_state="collapsed")

THEMES = ["auto", "light", "dark"]
THEME_LABEL = {"auto": "🌓 Auto", "light": "☀️ Light", "dark": "🌙 Dark"}
GARDEN = ["🌱", "🌷", "🌻", "🌼", "🌸", "🍀", "🌺", "🍎"]
CHOICES = {"full": 2, "some": 3, "free": 4}
SUPPORT_LABEL = {"auto": "Auto (grows with the child)", "full": "Full help (2 choices, answer glows)",
                 "some": "Some help (3 choices)", "free": "On my own (4 choices)"}

BADGES = [
    ("first", "First Flower", "🌷", "Finish your first lesson"),
    ("five", "Busy Bee", "🐝", "Finish 5 lessons"),
    ("streak3", "Come Back Star", "🔥", "Learn on 3 days in a row"),
    ("f50", "Little Garden", "🌻", "Grow 50 flowers"),
    ("f200", "Big Garden", "🌳", "Grow 200 flowers"),
    ("g_start", "Step 1 Done", "🥇", "Finish every Step 1 lesson"),
    ("g_grow", "Step 2 Done", "🥈", "Finish every Step 2 lesson"),
    ("g_shine", "Step 3 Done", "🥉", "Finish every Step 3 lesson"),
    ("mix", "Mix Master", "🎯", "Finish a Mixed Review"),
    ("all", "Pyqoo Champion", "👑", "Finish every lesson"),
]


# ------------------------------------------------------------------ state
def init():
    ss = st.session_state
    if "lang" not in ss:
        _l = storage.settings().get("lang", "en")
        ss.lang = _l if _l in ("en", "ml") else "en"
    if "boot" in ss:
        return
    ss.boot = True
    s = storage.settings()
    ss.theme = s["theme"] if s["theme"] in THEMES else "auto"
    ss.name = None
    ss.P = None
    ss.page = "learn"
    ss.lesson = None
    ss.stage = "story"
    ss.step = 0
    ss.quiz = None
    ss.parent_ok = False
    ss.confirm_reset = False
    ss.err = ""
    ss.tick = time.time()
    ss.pick_level = "start"


def commit():
    ss = st.session_state
    if ss.name and ss.P is not None:
        storage.save_profile(ss.name, ss.P)


def save_settings():
    ss = st.session_state
    storage.save_settings({"theme": ss.theme, "lang": ss.lang, "last_profile": ss.name or ""})


def prefs():
    ss = st.session_state
    return ss.P["prefs"] if ss.P else {}


def tick():
    ss = st.session_state
    now = time.time()
    if ss.P is not None:
        ss.P["seconds"] += int(min(now - ss.tick, 90))
    ss.tick = now


def total_stars(P):
    return sum(P["done"].values())


def touch_day(P):
    today = datetime.date.today()
    last = P["last_day"]
    if last == today.isoformat():
        return
    P["streak"] = P["streak"] + 1 if last == (today - datetime.timedelta(days=1)).isoformat() else 1
    P["last_day"] = today.isoformat()


def award(P, bid, new):
    if bid not in P["badges"]:
        P["badges"].append(bid)
        new.append(bid)


def check_badges(P, mix=False):
    new = []
    done = P["done"]
    if len(done) >= 1:
        award(P, "first", new)
    if len(done) >= 5:
        award(P, "five", new)
    if P["streak"] >= 3:
        award(P, "streak3", new)
    if P["flowers"] >= 50:
        award(P, "f50", new)
    if P["flowers"] >= 200:
        award(P, "f200", new)
    if mix:
        award(P, "mix", new)
    for lv in C.LEVELS:
        if all(l["id"] in done for l in C.lessons_for(lv["id"])):
            award(P, "g_" + lv["id"], new)
    if len(done) >= len(C.LESSON_LIST):
        award(P, "all", new)
    return new


def badge_info(bid):
    for gid, name, em, desc in BADGES:
        if gid == bid:
            return T(name), em, T(desc)
    return bid, "🏅", ""


# ------------------------------------------------------------------ text helpers (language aware)
def L(l, field):
    """Lesson text in the current language: field is title, blurb or story."""
    if field == "title":
        return PK(l["en"], l["ml"])
    if field == "blurb":
        return PK(l["blurb_en"], l["blurb_ml"])
    return l.get(field)


def story_text(l, i):
    em, en = l["story"][i]
    return em, T(en)


def opt_label(o, mode, show_words):
    en, ml = o["en"], o["ml"]
    word = PK(en, ml)
    if mode == "word":
        return word
    if mode == "num":
        return word
    if mode == "more":
        return o["e"]
    if mode == "pic" and o["e"] and o.get("tile", True):
        return o["e"] + ("\n" + word if show_words else "")
    return word


def q_text(q):
    return PK(q["en"], q["ml"])


def why_text(q):
    return PK(q["why_en"], q["why_ml"])


# ------------------------------------------------------------------ callbacks
def go(page):
    ss = st.session_state
    ss.page = page
    ss.lesson = None
    ss.quiz = None
    if page != "parent":
        ss.parent_ok = False


def cycle_theme():
    ss = st.session_state
    ss.theme = THEMES[(THEMES.index(ss.theme) + 1) % len(THEMES)]
    save_settings()


def toggle_lang():
    ss = st.session_state
    ss.lang = "ml" if ss.lang == "en" else "en"
    save_settings()


def set_level(lv):
    ss = st.session_state
    ss.P["level"] = lv
    commit()


def start_profile():
    ss = st.session_state
    nick = (ss.get("nick") or "").strip()[:20]
    if not nick:
        ss.err = "Please type a nickname."
        return
    if not ss.get("consent"):
        ss.err = "A parent, guardian or teacher needs to be with you. Tick the box when they are."
        return
    ss.err = ""
    open_profile(nick, ss.pick_level)


def open_profile(nick, level=None):
    ss = st.session_state
    ss.name = nick
    ss.P = storage.load_profile(nick)
    if level and not ss.P["done"] and ss.P["xp"] == 0:
        ss.P["level"] = level
    ss.tick = time.time()
    commit()
    save_settings()
    ss.page = "learn"


def switch_child():
    ss = st.session_state
    ss.name, ss.P, ss.lesson, ss.quiz, ss.parent_ok = None, None, None, None, False


def open_lesson(lid):
    ss = st.session_state
    ss.lesson, ss.stage, ss.step, ss.quiz = lid, "story", 0, None


def story_move(delta, n):
    ss = st.session_state
    ss.step += delta
    if ss.step >= n:
        to_quiz(ss.lesson)
    ss.step = max(0, ss.step)


def skip_story():
    to_quiz(st.session_state.lesson)


def photo_questions():
    """Build questions from the child's own photos (My World)."""
    P = st.session_state.P
    ph = P["photos"]
    out = []
    for i, p in enumerate(ph):
        others = [dict(e="", en=x["name"], ml=x["name"]) for j, x in enumerate(ph) if j != i]
        out.append(dict(id=f"myworld:{i}", lid="myworld", kind="photo", mode="word", big="", en="Who or what is this?", ml="ഇതാരാ / ഇതെന്താ?",
                        rights=[dict(e="", en=p["name"], ml=p["name"])], wrongs=others or [dict(e="", en="?", ml="?")],
                        why_en=f"This is {p['name']}!", why_ml=f"ഇത് {p['name']} ആണ്!", photo=p["b64"]))
    return out


def lesson_pool(lid):
    return photo_questions() if lid == "myworld" else C.BANK[lid]


def to_quiz(lid):
    ss = st.session_state
    P = ss.P
    ss.stage = "quiz"
    pool = lesson_pool(lid)
    n = min(P["prefs"]["session_len"], len(pool))
    review = [C.QBY_ID[i] for i in P["review"] if i in C.QBY_ID and C.QBY_ID[i]["lid"] == lid]
    chosen = random.sample(review, min(2, len(review), n))
    ids = {q["id"] for q in chosen}
    rest = [q for q in pool if q["id"] not in ids]
    chosen += random.sample(rest, min(n - len(chosen), len(rest)))
    random.shuffle(chosen)
    ss.quiz = new_quiz("lesson", chosen, lid)


def new_quiz(kind, qs, lid=None):
    return dict(kind=kind, lid=lid, qs=[dict(q=q) for q in qs], i=0, wrong=[], answered=False, first_ok=0, flowers=0, result=None, hint=False)


def choices_for(lid):
    P = st.session_state.P
    sup = P["prefs"]["support"]
    if sup in CHOICES:
        return CHOICES[sup]
    return 2 + P["lvl"].get(lid, 0)


def ensure_opts(qz):
    ent = qz["qs"][qz["i"]]
    if "opts" not in ent:
        q = ent["q"]
        n = choices_for(q["lid"])
        if q["mode"] == "word" and q["kind"] not in ("name", "photo"):
            n = max(n, 2)
        opts, right = C.build_options(q, n)
        ent["opts"], ent["right"] = opts, right
    return ent


def support_mode():
    sup = prefs()["support"]
    if sup == "auto":
        return "full" if st.session_state.P["lvl"].get("_cur", 0) == 0 else "some"
    return sup


def glow_now(qz, ent):
    """Errorless learning: how much the right answer is shown depends on the support level."""
    sup = prefs()["support"]
    lid = ent["q"]["lid"]
    if sup == "auto":
        lvl = st.session_state.P["lvl"].get(lid, 0)
        sup = "full" if lvl == 0 else ("some" if lvl == 1 else "free")
    wrong = len(qz["wrong"])
    if sup == "full":
        return True
    if sup == "some":
        return wrong >= 1
    return wrong >= 2


def adapt(lid, ok_first):
    P = st.session_state.P
    if P["prefs"]["support"] != "auto":
        return
    lvl = P["lvl"].get(lid, 0)
    if ok_first:
        P["run"][lid] = P["run"].get(lid, 0) + 1
        P["miss"][lid] = 0
        if P["run"][lid] >= 3 and lvl < 2:
            P["lvl"][lid], P["run"][lid] = lvl + 1, 0
    else:
        P["miss"][lid] = P["miss"].get(lid, 0) + 1
        P["run"][lid] = 0
        if P["miss"][lid] >= 2 and lvl > 0:
            P["lvl"][lid], P["miss"][lid] = lvl - 1, 0


def pick_ans(oi):
    ss = st.session_state
    qz = ss.quiz
    ent = qz["qs"][qz["i"]]
    q = ent["q"]
    if qz["answered"] or oi in qz["wrong"]:
        return
    P = ss.P
    if oi == ent["right"]:
        first = not qz["wrong"]
        qz["answered"] = True
        P["q_total"] += 1
        P["flowers"] += 1
        qz["flowers"] += 1
        st_ = P["stats"].setdefault(q["lid"], dict(plays=0, ok=0, tot=0, last=""))
        st_["tot"] += 1
        if first:
            qz["first_ok"] += 1
            P["q_first"] += 1
            st_["ok"] += 1
            if q["id"] in P["review"]:
                P["review"].remove(q["id"])
        P["xp"] += 10 if first else 5
        adapt(q["lid"], first)
        commit()
    else:
        qz["wrong"].append(oi)
        if len(qz["wrong"]) == 1:
            if q["id"] not in P["review"] and not q["id"].startswith("myworld"):
                P["review"].append(q["id"])
                P["review"] = P["review"][-60:]
            adapt(q["lid"], False)
            commit()


def next_q():
    ss = st.session_state
    qz = ss.quiz
    if qz["i"] + 1 < len(qz["qs"]):
        qz["i"] += 1
        qz["wrong"], qz["answered"] = [], False
    else:
        finish_quiz()


def finish_quiz():
    ss = st.session_state
    qz, P = ss.quiz, ss.P
    n = len(qz["qs"])
    touch_day(P)
    P["plays"] += 1
    new = []
    if qz["kind"] == "lesson":
        lid = qz["lid"]
        stars_ = 3 if qz["first_ok"] >= n * 0.7 else (2 if qz["first_ok"] >= n * 0.4 else 1)   # always at least one star
        P["done"][lid] = max(P["done"].get(lid, 0), stars_)
        P["stats"].setdefault(lid, dict(plays=0, ok=0, tot=0, last=""))
        P["stats"][lid]["plays"] += 1
        P["stats"][lid]["last"] = datetime.date.today().isoformat()
        P["xp"] += 20
        new = check_badges(P)
        qz["result"] = dict(stars=stars_, new=new)
    else:
        P["mix_best"] = max(P["mix_best"], qz["first_ok"])
        new = check_badges(P, mix=True)
        qz["result"] = dict(stars=0, new=new)
    commit()


def start_mix():
    ss = st.session_state
    P = ss.P
    n = C.MIX_LENGTH
    unlocked = [l["id"] for l in C.LESSON_LIST if l["level"] == P["level"] or l["id"] in P["done"]]
    pool = [q for lid in unlocked for q in C.BANK[lid]]
    rev = [C.QBY_ID[i] for i in P["review"] if i in C.QBY_ID]
    chosen = random.sample(rev, min(n // 2, len(rev)))
    ids = {q["id"] for q in chosen}
    rest = [q for q in pool if q["id"] not in ids]
    chosen += random.sample(rest, min(n - len(chosen), len(rest)))
    random.shuffle(chosen)
    ss.quiz = new_quiz("mix", chosen)


def check_gate():
    ss = st.session_state
    try:
        ok = int(str(ss.get("gate", "")).strip()) == ss.gate_answer
    except ValueError:
        ok = False
    ss.parent_ok = ok
    ss.err = "" if ok else "That is not right. Try again."


def lock_parent():
    st.session_state.parent_ok = False


def ask_reset():
    st.session_state.confirm_reset = True


def do_reset():
    ss = st.session_state
    storage.delete_profile(ss.name)
    ss.confirm_reset = False
    switch_child()


def cancel_reset():
    st.session_state.confirm_reset = False


def set_pref(key, value):
    ss = st.session_state
    ss.P["prefs"][key] = value
    commit()


def toggle_goal(lid):
    P = st.session_state.P
    if lid in P["goals"]:
        P["goals"].remove(lid)
    else:
        P["goals"].append(lid)
    commit()


def save_note():
    ss = st.session_state
    ss.P["note"] = (ss.get("note_in") or "")[:500]
    commit()


def add_photo():
    ss = st.session_state
    f = ss.get("photo_file")
    nm = (ss.get("photo_name") or "").strip()[:20]
    if f is None or not nm:
        ss.err = "Choose a photo and type a name."
        return
    if len(ss.P["photos"]) >= 12:
        ss.err = "You can keep up to 12 photos."
        return
    try:
        from PIL import Image
        im = Image.open(f).convert("RGB")
        im.thumbnail((420, 420))
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=80)
        b64 = base64.b64encode(buf.getvalue()).decode()
    except Exception:
        ss.err = "That photo could not be read."
        return
    ss.P["photos"].append(dict(name=nm, b64=b64))
    ss.err = ""
    commit()


def del_photo(i):
    ss = st.session_state
    if 0 <= i < len(ss.P["photos"]):
        ss.P["photos"].pop(i)
        commit()


MYWORLD = dict(id="myworld", level="start", art="📷", en="My World", ml="എന്റെ ലോകം", blurb_en="Your own photos and names.", blurb_ml="നിങ്ങളുടെ സ്വന്തം ഫോട്ടോകളും പേരുകളും.",
               story=[("📷", "These are your own people and things."), ("👀", "Look at the photo, then tap the name."), ("⭐", "Let us begin!")])


def show_img(data):
    try:
        st.image(data, width="stretch")
    except TypeError:           # older Streamlit
        st.image(data, use_container_width=True)


def all_lessons_for(level, P):
    ls = list(C.lessons_for(level))
    if level == "start" and len(P["photos"]) >= 2:
        ls = [MYWORLD] + ls
    return ls


def lesson_by_id(lid):
    return MYWORLD if lid == "myworld" else C.LESSON_BY_ID[lid]


# ------------------------------------------------------------------ shared UI
def level_buttons(current, on_pick, prefix):
    with st.container(key=f"ns-{prefix}-lv"):
        cols = st.columns(len(C.LEVELS))
        for col, lv in zip(cols, C.LEVELS):
            with col:
                state = "tab-on" if lv["id"] == current else "tab"
                with st.container(key=f"{state}-{prefix}-{lv['id']}"):
                    st.button(PK(lv["en"], lv["ml"]), key=f"{prefix}-{lv['id']}", on_click=on_pick, args=(lv["id"],))


def topbar():
    ss = st.session_state
    with st.container(key="ns-top"):
        c1, c2, c3 = st.columns([2.1, 1.25, 1.1])
        with c1:
            md('<div class="nk-row"><span style="font-size:1.8rem">🦉</span><div><div class="nk-title" style="font-size:1.1rem;white-space:nowrap">Pyqoo Easy</div>'
               f'<div class="nk-sub" style="margin:0;white-space:nowrap">{esc(T("one step at a time"))}</div></div></div>')
        with c2:
            st.button("English" if ss.lang == "ml" else "മലയാളം", key="lang-btn", on_click=toggle_lang)
        with c3:
            st.button(T(THEME_LABEL[ss.theme]), key="theme-btn", on_click=cycle_theme)


def nav():
    ss = st.session_state
    items = [("learn", "🎒 Learn"), ("mix", "🎯 Review"), ("rewards", "🌻 Garden"), ("parent", "👪 Parent")]
    with st.container(key="ns-nav"):
        cols = st.columns(len(items))
        for col, (pid, label) in zip(cols, items):
            with col:
                state = "tab-on" if ss.page == pid else "tab"
                with st.container(key=f"{state}-nav-{pid}"):
                    st.button(T(label), key=f"nav-{pid}", on_click=go, args=(pid,))


def garden_html(n):
    shown = [GARDEN[i % len(GARDEN)] for i in range(max(0, n - 24), n)] if n else []
    return f'<div class="nk-garden">{"".join(shown) if shown else "🌱"}</div>'


def stats_row(P):
    md(f'<div class="nk-stats">'
       f'<div class="nk-stat"><b>⭐ {total_stars(P)}</b><span>{esc(T("stars"))}</span></div>'
       f'<div class="nk-stat"><b>🌷 {P["flowers"]}</b><span>{esc(T("flowers"))}</span></div>'
       f'<div class="nk-stat"><b>🔥 {P["streak"]}</b><span>{esc(T("day streak"))}</span></div>'
       f'<div class="nk-stat"><b>{len(P["done"])}/{len(C.LESSON_LIST)}</b><span>{esc(T("lessons"))}</span></div></div>')


def footer():
    md(f'<div class="nk-foot">{esc(T("Pyqoo Easy is learning support. It is not therapy, diagnosis or medical advice. No timers, no ads, no chat."))}'
       '<br><b>Pyqoo Easy</b></div>')


def seg(prefix, options, current, on_pick, stack=False):
    """Row (or stack) of choice buttons. options: [(value, label)]"""
    if stack:
        for val, label in options:
            with st.container(key=f"{'sel' if val == current else 'opt'}-{prefix}-{val}"):
                st.button(label, key=f"{prefix}-{val}", on_click=on_pick, args=(val,))
        return
    with st.container(key=f"ns-{prefix}"):
        cols = st.columns(len(options))
        for col, (val, label) in zip(cols, options):
            with col:
                with st.container(key=f"{'sel' if val == current else 'opt'}-{prefix}-{val}"):
                    st.button(label, key=f"{prefix}-{val}", on_click=on_pick, args=(val,))


def listen_row(q_en, q_ml):
    """Listen buttons for the current prompt. Malayalam can use a saved clip, Sarvam, or the browser voice."""
    p = prefs()
    mode = p.get("listen_lang", "app")
    if mode == "both":
        with st.container(key="ns-listen2"):
            c1, c2 = st.columns(2)
            with c1:
                voice.listen(q_en, force="en")
            with c2:
                voice.listen(q_ml, force="ml")
    elif mode == "ml":
        voice.listen(q_ml, force="ml")
    else:
        voice.listen(PK(q_en, q_ml))


# ------------------------------------------------------------------ onboarding
def onboarding():
    ss = st.session_state
    md('<div class="nk-hero"><div class="nk-mascot">🦉</div><div class="nk-title">' + esc(T("Hi, I am Pyqoo!")) + '</div>'
       '<small>' + T("Welcome to <b>Pyqoo Easy</b>. Look, listen and tap. Learn at your own speed. There are no timers.") + '</small></div>')
    names = storage.profile_names()
    if names:
        md(f'<div class="nk-title" style="font-size:1.05rem">{esc(T("Welcome back"))}</div>')
        for n in names[:8]:
            st.button(f"🦉 {n}", key=f"prof-{n}", on_click=open_profile, args=(n,))
        md(f'<div class="nk-sub" style="text-align:center">{esc(T("or start a new learner"))}</div>')
    with st.container(key="card-new"):
        st.text_input(T("Pick a nickname (not the full name)"), key="nick", max_chars=20, placeholder=T("e.g. Anu"))
        md(f'<div class="nk-sub">{esc(T("Where should we start?"))}</div>')
        level_buttons(ss.pick_level, lambda v: setattr(ss, "pick_level", v), "ob")
        lv = next(x for x in C.LEVELS if x["id"] == ss.pick_level)
        md(f'<div class="nk-sub" style="text-align:center">{esc(PK(lv["note_en"], lv["note_ml"]))}</div>')
        st.checkbox(T("A parent, guardian or teacher is with me and agrees"), key="consent")
        if ss.err:
            md(f'<div class="nk-fb no">{esc(T(ss.err))}</div>')
        st.button(T("Let us start ➜"), key="start", type="primary", on_click=start_profile)
    footer()


# ------------------------------------------------------------------ learn
def learn():
    ss = st.session_state
    P = ss.P
    md(f'<div class="nk-hero"><div class="nk-mascot">🦉</div><div class="nk-title">{esc(T("Hi {name}!", name=ss.name))}</div>'
       f'<small>{esc(T("{done} of {total} lessons done. Every tap grows a flower!", done=len(P["done"]), total=len(C.LESSON_LIST)))}</small>'
       f'{garden_html(P["flowers"])}</div>')
    stats_row(P)
    goals = [g for g in P["goals"] if g not in P["done"] and (g in C.LESSON_BY_ID or g == "myworld")]
    if goals:
        md(f'<div class="nk-title" style="font-size:1.05rem">{esc(T("Today we try"))}</div>')
        for g in goals[:3]:
            l = lesson_by_id(g)
            with st.container(key=f"card-goal-{g}"):
                md(f'<div class="nk-row"><div class="nk-art">{l["art"]}</div><div class="nk-grow"><div class="nk-title" style="font-size:1.1rem">{esc(L(l, "title"))}</div></div></div>')
                st.button(T("Play ➜"), key=f"goal-{g}", type="primary", on_click=open_lesson, args=(g,))
    level_buttons(P["level"], set_level, "lb")
    lv = next(x for x in C.LEVELS if x["id"] == P["level"])
    md(f'<div class="nk-sub" style="text-align:center">{esc(PK(lv["note_en"], lv["note_ml"]))}</div>')
    for l in all_lessons_for(P["level"], P):
        s = P["done"].get(l["id"], 0)
        with st.container(key=f"card-{l['id']}"):
            md(f'<div class="nk-row"><div class="nk-art">{l["art"]}</div><div class="nk-grow"><div class="nk-title" style="font-size:1.1rem">{esc(L(l, "title"))}</div>'
               f'<div class="nk-sub">{esc(L(l, "blurb"))}</div></div></div>'
               f'<div class="nk-stars" style="color:var(--sun);margin:6px 0 2px">{ui.stars(s)}</div>')
            st.button(T("Play again") if s else T("Play ➜"), key=f"play-{l['id']}", type="secondary" if s else "primary",
                      on_click=open_lesson, args=(l["id"],))


# ------------------------------------------------------------------ lesson
def exit_lesson():
    go("learn")


def lesson_view():
    ss = st.session_state
    l = lesson_by_id(ss.lesson)
    with st.container(key="ns-lhead"):
        c1, c2 = st.columns([1, 3])
        with c1:
            st.button("✕", key="exit", on_click=exit_lesson)
        with c2:
            md(f'<div class="nk-title" style="padding-top:6px">{l["art"]} {esc(L(l, "title"))}</div>')
    if ss.stage == "story":
        story_view(l)
    else:
        quiz_view(l)


def story_view(l):
    ss = st.session_state
    n = len(l["story"])
    em, text = story_text(l, ss.step)
    md(ui.dots(ss.step, ss.step, n))
    md(f'<div class="nk-story nk-pop"><div class="em">{em}</div><p>{esc(text)}</p></div>')
    with st.container(key="ns-story-nav"):
        c1, c2 = st.columns([1, 2])
        with c1:
            st.button(T("◀ Back"), key="story-back", on_click=story_move, args=(-1, n), disabled=ss.step == 0)
        with c2:
            st.button(T("Next ▶") if ss.step < n - 1 else T("Let us play! 🎮"), key="story-next", type="primary", on_click=story_move, args=(1, n))
    st.button(T("Skip"), key="story-skip", on_click=skip_story)


def quiz_view(l=None):
    ss = st.session_state
    qz = ss.quiz
    if qz is None:
        to_quiz(l["id"])
        qz = ss.quiz
    if qz["result"]:
        return result_view(l)
    n = len(qz["qs"])
    ent = ensure_opts(qz)
    q = ent["q"]
    opts, right = ent["opts"], ent["right"]
    p = prefs()
    show_words = p["show_words"]
    md(ui.dots(qz["i"], qz["i"], n))
    md(f'<div class="nk-sub" style="text-align:center">{esc(T("Question {i} of {n}", i=qz["i"] + 1, n=n))}</div>')
    if q.get("photo"):
        show_img(base64.b64decode(q["photo"]))
    elif q["big"]:
        small = " small" if len(q["big"]) > 14 else ""
        md(f'<div class="nk-big-pic{small}">{esc(q["big"])}</div>')
    md(f'<div class="nk-qtext">{esc(q_text(q))}</div>')
    listen_row(q["en"], q["ml"])
    glow = glow_now(qz, ent) and not qz["answered"]
    mode = "more" if q["kind"] == "more" else q["mode"]
    stack = q["kind"] in ("life", "name", "photo")
    labels = []
    for o in opts:
        lab = opt_label(o, mode, show_words)
        if q["kind"] == "life":
            lab = (o["e"] + "  " if o["e"] else "") + PK(o["en"], o["ml"])
        labels.append(lab)

    def state_of(oi):
        if qz["answered"]:
            return "ok" if oi == right else "fade"
        if oi in qz["wrong"]:
            return "fade"
        if glow and oi == right:
            return "glow"
        return "opt"

    def render(oi):
        state = state_of(oi)
        kind = "stack" if stack else "tile"
        with st.container(key=f"{state}-{kind}-q{qz['i']}-{oi}"):
            st.button(labels[oi], key=f"q{qz['i']}-o{oi}", on_click=pick_ans, args=(oi,), disabled=qz["answered"] or oi in qz["wrong"])

    if stack:
        for oi in range(len(opts)):
            render(oi)
    else:
        for r in range(0, len(opts), 2):
            row = list(range(r, min(r + 2, len(opts))))
            with st.container(key=f"ns-row{qz['i']}-{r}"):
                cols = st.columns(2)
                for c, oi in zip(cols, row):
                    with c:
                        render(oi)
    if qz["answered"]:
        first = not qz["wrong"]
        md(f'<div class="nk-fb ok nk-pop">🌷 {esc(T("Great job!") if first else T("You did it!"))} {esc(why_text(q))}</div>')
        if ss.lang == "ml" or prefs().get("listen_lang") in ("ml", "both"):
            voice.listen(q["why_ml"], force="ml")
        last = qz["i"] + 1 >= n
        st.button(T("See my flowers ➜") if last else T("Next ➜"), key="next-q", type="primary", on_click=next_q)
    elif qz["wrong"]:
        msg = T("Nice try! Look again. The glowing one is a good choice.") if glow_now(qz, ent) else T("Nice try! Look again.")
        md(f'<div class="nk-fb hint">{esc(msg)}</div>')


def result_view(l):
    ss = st.session_state
    qz = ss.quiz
    res = qz["result"]
    n = len(qz["qs"])
    if qz["kind"] == "lesson":
        md(f'<div class="nk-hero nk-pop" style="text-align:center"><div class="nk-title">{esc(T("Well done!"))}</div>'
           f'<div style="font-size:2.6rem;letter-spacing:6px;margin:6px 0">{"⭐" * res["stars"]}{"☆" * (3 - res["stars"])}</div>'
           f'<small>{esc(T("You grew {f} flowers today!", f=qz["flowers"]))}</small>{garden_html(ss.P["flowers"])}</div>')
    else:
        md(f'<div class="nk-hero nk-pop" style="text-align:center"><div class="nk-title">{esc(T("Review done!"))}</div>'
           f'<small>{esc(T("You grew {f} flowers today!", f=qz["flowers"]))}</small>{garden_html(ss.P["flowers"])}</div>')
    for bid in res["new"]:
        name, em, desc = badge_info(bid)
        md(f'<div class="nk-fb hint nk-pop">{em} {T("New badge: <b>{name}</b>.", name=esc(name))} {esc(desc)}</div>')
    with st.container(key="ns-res-act"):
        c1, c2 = st.columns(2)
        with c1:
            if qz["kind"] == "lesson":
                st.button(T("Play again"), key="res-again", on_click=open_lesson, args=(l["id"],))
            else:
                st.button(T("Another round"), key="res-again", on_click=start_mix)
        with c2:
            st.button(T("Back to lessons"), key="res-back", type="primary", on_click=go, args=("learn",))


# ------------------------------------------------------------------ mixed review
def mix_view():
    ss = st.session_state
    P = ss.P
    if ss.quiz and ss.quiz["kind"] == "mix":
        return quiz_view(None)
    md('<div class="nk-hero"><div class="nk-mascot">🎯</div><div class="nk-title">' + esc(T("Mixed Review")) + '</div>'
       '<small>' + esc(T("A few questions from everything you have learned. Questions you found tricky come back gently.")) + '</small></div>')
    md(f'<div class="nk-card"><div class="nk-sub">{T("{q} questions to practise. Tricky ones waiting: <b>{r}</b>", q=C.total_questions(), r=len(P["review"]))}</div></div>')
    st.button(T("Start review ➜"), key="mix-start", type="primary", on_click=start_mix)


# ------------------------------------------------------------------ garden and badges
def rewards_view():
    ss = st.session_state
    P = ss.P
    md(f'<div class="nk-hero"><div class="nk-mascot">🌻</div><div class="nk-title">{esc(T("My Garden"))}</div>'
       f'<small>{esc(T("{n} flowers grown so far.", n=P["flowers"]))}</small>{garden_html(P["flowers"])}</div>')
    stats_row(P)
    md(f'<div class="nk-title" style="margin-top:6px">{esc(T("Lesson stars"))}</div>')
    cells = ""
    for l in C.LESSON_LIST:
        got = P["done"].get(l["id"], 0)
        cells += f'<div class="nk-badge {"" if got else "locked"}"><div class="em">{l["art"]}</div><b>{esc(L(l, "title"))}</b><span>{ui.stars(got)}</span></div>'
    md(f'<div class="nk-grid">{cells}</div>')
    md(f'<div class="nk-title" style="margin-top:6px">{esc(T("Special badges"))}</div>')
    cells = ""
    for gid, name, em, desc in BADGES:
        got = gid in P["badges"]
        cells += f'<div class="nk-badge {"" if got else "locked"}"><div class="em">{em}</div><b>{esc(T(name))}</b><span>{esc(T(desc))}</span></div>'
    md(f'<div class="nk-grid">{cells}</div>')


# ------------------------------------------------------------------ parent and teacher corner
def lvl_name(lid, P):
    sup = P["prefs"]["support"]
    if sup != "auto":
        return T({"full": "Full help", "some": "Some help", "free": "On own"}[sup])
    return T(["Full help", "Some help", "On own"][P["lvl"].get(lid, 0)])


def parent_view():
    ss = st.session_state
    P = ss.P
    if not ss.parent_ok:
        if "gate_answer" not in ss:
            a, b = random.randint(6, 9), random.randint(6, 9)
            ss.gate_q, ss.gate_answer = f"{a} × {b}", a * b
        md('<div class="nk-hero"><div class="nk-mascot">👪</div><div class="nk-title">' + esc(T("Parent and teacher corner")) + '</div><small>' + esc(T("A quick grown-up check, then you can see progress and settings.")) + '</small></div>')
        with st.container(key="card-gate"):
            st.text_input(T("What is {q}?", q=ss.gate_q), key="gate", max_chars=3)
            if ss.err:
                md(f'<div class="nk-fb no">{esc(T(ss.err))}</div>')
            st.button(T("Open"), key="gate-open", type="primary", on_click=check_gate)
        return
    acc = round(P["q_first"] / P["q_total"] * 100) if P["q_total"] else 0
    minutes = round(P["seconds"] / 60)
    md(f'<div class="nk-hero"><div class="nk-mascot">👪</div><div class="nk-title">{esc(T("{name} progress", name=ss.name))}</div>'
       f'<small>{esc(T("Learning since {date}", date=P["created"]))}</small></div>')
    md(f'<div class="nk-stats"><div class="nk-stat"><b>{len(P["done"])}/{len(C.LESSON_LIST)}</b><span>{esc(T("lessons"))}</span></div>'
       f'<div class="nk-stat"><b>{acc}%</b><span>{esc(T("first-try right"))}</span></div>'
       f'<div class="nk-stat"><b>{minutes}</b><span>{esc(T("minutes"))}</span></div>'
       f'<div class="nk-stat"><b>{len(P["review"])}</b><span>{esc(T("to revisit"))}</span></div></div>')

    # goals
    md(f'<div class="nk-title" style="margin-top:6px">{esc(T("Learning goals"))}</div>')
    md(f'<div class="nk-sub">{esc(T("Tap a lesson to make it a goal. Goals show up on the child screen as Today we try."))}</div>')
    for lv in C.LEVELS:
        md(f'<div class="nk-sub" style="margin-top:8px"><b>{esc(PK(lv["en"], lv["ml"]))}</b></div>')
        for l in C.lessons_for(lv["id"]):
            goal = l["id"] in P["goals"]
            done = P["done"].get(l["id"], 0)
            mark = "🎯 " if goal else ""
            with st.container(key=f"{'sel' if goal else 'opt'}-stack-goal-{l['id']}"):
                st.button(f"{mark}{l['art']} {L(l, 'title')}  {ui.stars(done)}", key=f"goal-t-{l['id']}", on_click=toggle_goal, args=(l["id"],))

    # table
    md(f'<div class="nk-title" style="margin-top:10px">{esc(T("Skill progress"))}</div>')
    rows = ""
    for l in C.LESSON_LIST:
        s = P["stats"].get(l["id"])
        if not s or not s["tot"]:
            continue
        pct = round(s["ok"] / s["tot"] * 100)
        rows += (f'<tr><td>{l["art"]} <b>{esc(L(l, "title"))}</b><br><span class="nk-sub">{esc(l.get("goal") or "")}</span></td>'
                 f'<td style="white-space:nowrap">{pct}%<br><span class="nk-sub">{esc(lvl_name(l["id"], P))}</span></td></tr>')
    if rows:
        md(f'<div class="nk-card"><table class="nk-table"><tr><th>{esc(T("Skill"))}</th><th>{esc(T("First try and support"))}</th></tr>{rows}</table></div>')
    else:
        md(f'<div class="nk-card"><div class="nk-sub">{esc(T("No answers yet. Progress will show here."))}</div></div>')
    md(f'<div class="nk-card"><div class="nk-sub">{esc(T("Question bank: {q} questions in {l} lessons. Each play draws a few at random with new wrong choices, so repeats feel fresh.", q=C.total_questions(), l=len(C.LESSON_LIST)))}</div></div>')

    # support
    md(f'<div class="nk-title" style="margin-top:10px">{esc(T("How much help?"))}</div>')
    md(f'<div class="nk-sub">{esc(T("Auto starts with 2 choices and a glowing answer, then slowly gives less help as your child succeeds. Choose a fixed level if you prefer."))}</div>')
    seg("sup", [(k, T(v)) for k, v in SUPPORT_LABEL.items()], P["prefs"]["support"], lambda v: set_pref("support", v), stack=True)
    md(f'<div class="nk-title" style="margin-top:10px">{esc(T("Questions in each play"))}</div>')
    seg("slen", [(v, str(v)) for v in (4, 6, 8, 10)], P["prefs"]["session_len"], lambda v: set_pref("session_len", v))
    md(f'<div class="nk-title" style="margin-top:10px">{esc(T("Picture size"))}</div>')
    seg("size", [("normal", T("Normal")), ("large", T("Large")), ("huge", T("Extra large"))], P["prefs"]["size"], lambda v: set_pref("size", v))
    md(f'<div class="nk-title" style="margin-top:10px">{esc(T("Display"))}</div>')
    seg("words", [(True, T("Words under pictures: on")), (False, T("Words under pictures: off"))], P["prefs"]["show_words"], lambda v: set_pref("show_words", v), stack=True)
    seg("contrast", [(True, T("High contrast: on")), (False, T("High contrast: off"))], P["prefs"]["contrast"], lambda v: set_pref("contrast", v), stack=True)
    seg("calm", [(True, T("Calm mode (no movement): on")), (False, T("Calm mode (no movement): off"))], P["prefs"]["calm"], lambda v: set_pref("calm", v), stack=True)
    md(f'<div class="nk-title" style="margin-top:10px">{esc(T("Listen language"))}</div>')
    seg("ll", [("app", T("Same as app")), ("ml", "മലയാളം"), ("both", T("Both"))], P["prefs"]["listen_lang"], lambda v: set_pref("listen_lang", v))
    md(f'<div class="nk-card"><div class="nk-title" style="font-size:1rem">{esc(T("Voice"))}</div><div class="nk-sub">{esc(voice.status())}</div></div>')
    voice.listen("നമസ്കാരം, ഞാൻ പിക്കൂ ആണ്. നമുക്ക് ഒരുമിച്ച് പഠിക്കാം.", force="ml")

    # my world photos
    md(f'<div class="nk-title" style="margin-top:10px">{esc(T("My World photos"))}</div>')
    md(f'<div class="nk-sub">{esc(T("Add photos of family, friends, pets and favourite things. With two or more, a My World lesson appears in Step 1."))}</div>')
    with st.container(key="card-photos"):
        st.file_uploader(T("Choose a photo"), type=["jpg", "jpeg", "png"], key="photo_file")
        st.text_input(T("Name for this photo"), key="photo_name", max_chars=20)
        if ss.err and ss.err in ("Choose a photo and type a name.", "You can keep up to 12 photos.", "That photo could not be read."):
            md(f'<div class="nk-fb no">{esc(T(ss.err))}</div>')
        st.button(T("Add photo"), key="photo-add", on_click=add_photo)
        for i, p in enumerate(P["photos"]):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.image(base64.b64decode(p["b64"]), caption=p["name"], width=140)
            with c2:
                st.button("🗑️", key=f"photo-del-{i}", on_click=del_photo, args=(i,))

    # note
    md(f'<div class="nk-title" style="margin-top:10px">{esc(T("Teacher or parent note"))}</div>')
    st.text_area(T("A private note about what works for this child"), value=P["note"], key="note_in", max_chars=500, height=100)
    st.button(T("Save note"), key="note-save", on_click=save_note)

    st.download_button(T("Download progress (JSON)"), storage.export_json(ss.name), file_name=f"pyqoo-easy-{ss.name}.json", mime="application/json")
    with st.container(key="ns-set2"):
        c1, c2 = st.columns(2)
        with c1:
            st.button(T("Switch learner"), key="set-switch", on_click=switch_child)
        with c2:
            st.button(T("🔒 Lock"), key="set-lock", on_click=lock_parent)
    if not ss.confirm_reset:
        st.button(T("Delete this learner's data"), key="reset", on_click=ask_reset)
    else:
        md(f'<div class="nk-fb no">{esc(T("This deletes all progress and photos for this learner. It cannot be undone."))}</div>')
        with st.container(key="ns-reset"):
            c1, c2 = st.columns(2)
            with c1:
                st.button(T("Yes, delete"), key="reset-yes", on_click=do_reset)
            with c2:
                st.button(T("Keep it"), key="reset-no", on_click=cancel_reset)
    md(f'<div class="nk-card"><div class="nk-title" style="font-size:1rem">{esc(T("Privacy and safety"))}</div>'
       f'<div class="nk-sub">{esc(T("Only a nickname, progress and the photos you add are stored, on this device. No ads, no chat, no timers. If you run this online for children, get verifiable parental consent as required by the DPDP Act and Rules."))}</div></div>')


# ------------------------------------------------------------------ main
def main():
    init()
    ss = st.session_state
    ui.inject(ss.theme, ss.lang, prefs())
    if ss.P is None:
        topbar()
        onboarding()
        return
    tick()
    if ss.lesson:
        lesson_view()
        footer()
        return
    topbar()
    nav()
    {"learn": learn, "mix": mix_view, "rewards": rewards_view, "parent": parent_view}[ss.page]()
    footer()


main()
