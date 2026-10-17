"""Pyqoo Easy: inclusive learning app (Streamlit).

Run with:  streamlit run app.py
Two views: Learner (big pictures, voice, gentle feedback, garden reward) and
Teacher or parent (progress, settings, export). Open the sidebar to switch.
"""
import base64
import csv
import html
import io
import json
import os
import random
from datetime import datetime

import streamlit as st
import streamlit.components.v1 as components

import content
import storage

st.set_page_config(page_title="Pyqoo Easy", page_icon="🌱", layout="centered",
                   initial_sidebar_state="collapsed")

FLOWERS = ["🌻", "🌼", "🌷", "🌸"]
esc = html.escape

UI = {
    "hello": {"en": "Hello", "ml": "ഹലോ"},
    "learn": {"en": "What shall we learn?", "ml": "ഇന്ന് എന്ത് പഠിക്കാം?"},
    "go": {"en": "Start", "ml": "തുടങ്ങാം"},
    "home": {"en": "Home", "ml": "ഹോം"},
    "next": {"en": "Next", "ml": "അടുത്തത്"},
    "listen": {"en": "Listen", "ml": "കേൾക്കൂ"},
    "start": {"en": "Listen, then tap the picture.", "ml": "കേൾക്കൂ, എന്നിട്ട് ചിത്രം തൊടൂ."},
    "yes": {"en": "Yes! Well done.", "ml": "ശരിയാണ്! നന്നായി."},
    "try1": {"en": "Nearly. Listen again and try another picture.",
             "ml": "ഏതാണ്ട് ശരി. ഒന്നുകൂടി കേട്ട് വേറെ ചിത്രം നോക്കൂ."},
    "try2": {"en": "Look at the glowing picture.", "ml": "തിളങ്ങുന്ന ചിത്രം നോക്കൂ."},
    "done": {"en": "All done!", "ml": "കഴിഞ്ഞു!"},
    "again": {"en": "Play again", "ml": "വീണ്ടും കളിക്കാം"},
    "nextset": {"en": "Next set", "ml": "അടുത്ത സെറ്റ്"},
    "garden": {"en": "My garden", "ml": "എന്റെ തോട്ടം"},
    "best": {"en": "Best", "ml": "മികച്ചത്"},
    "grew": {"en": "plants grew today", "ml": "ചെടികൾ വളർന്നു"},
    "pictures": {"en": "pictures", "ml": "ചിത്രങ്ങൾ"},
}


def T(d):
    return d[st.session_state.lang]


# ------------------------------------------------------------------ styling
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Baloo+Chettan+2:wght@600;700&family=Noto+Sans+Malayalam:wght@400;600;700&display=swap');
.stApp, .stApp p, .stApp label, .stApp li {font-family:'Atkinson Hyperlegible','Noto Sans Malayalam',system-ui,sans-serif}
.stApp {background:#EEF5F0}
header[data-testid="stHeader"] {background:transparent}
.block-container {max-width:680px; padding-top:2rem; padding-bottom:3rem}
h1,h2,h3 {font-family:'Baloo Chettan 2','Noto Sans Malayalam',system-ui,sans-serif !important; color:#14302A}
.stButton > button {border-radius:14px; font-weight:700; min-height:48px; border:2px solid #CFE0D6}
.stButton > button p {color:inherit}
.hello h1 {font-size:clamp(34px,9vw,46px); line-height:1.1; margin:0; padding:0}
.hello p {font-size:20px; color:#566D65; margin:4px 0 12px}

/* set cards on the home screen */
[class*="st-key-setcard"] {background:#fff; border-radius:22px !important; border:1px solid #CFE0D6 !important; box-shadow:0 6px 18px rgba(20,48,42,.07)}
.setcard .ico {width:64px; height:64px; border-radius:18px; background:#FBEDC2; display:grid; place-items:center; font-size:36px}
.setcard .nm {font-family:'Baloo Chettan 2','Noto Sans Malayalam',sans-serif; font-weight:700; font-size:22px; line-height:1.15; margin-top:8px}
.setcard .cp {font-size:14px; color:#566D65; min-height:40px}
.setcard .bs {font-size:14px; font-weight:700; color:#1B7A5A; min-height:20px}

/* question screen */
[class*="st-key-tiles"] [data-testid="stHorizontalBlock"], [class*="st-key-topbar"] [data-testid="stHorizontalBlock"] {flex-direction:row !important; flex-wrap:nowrap !important; gap:.75rem; align-items:center}
[class*="st-key-tiles"] [data-testid="stColumn"], [class*="st-key-tiles"] [data-testid="column"], [class*="st-key-topbar"] [data-testid="stColumn"], [class*="st-key-topbar"] [data-testid="column"] {min-width:0 !important; width:auto !important; flex:1 1 0 !important}
[class*="st-key-tiles"] .stButton > button {min-height:var(--tile-h); width:100%; border:var(--tile-bw) solid var(--tile-line); border-radius:22px; background:#fff; box-shadow:0 6px 18px rgba(20,48,42,.07); position:relative}
[class*="st-key-tiles"] .stButton > button p {font-size:var(--tile-font); line-height:1.15; font-weight:600}
[class*="st-key-tiles"] .stButton > button:hover:not(:disabled) {border-color:#1B7A5A}
[class*="st-key-tiles"] .stButton > button:disabled {opacity:.32; cursor:not-allowed}
.st-key-tiles_good .stButton > button:disabled {opacity:.45}
.st-key-tiles_good [data-testid="stBaseButton-primary"], .st-key-tiles_good button[kind="primary"] {background:#D3EBDF !important; border:var(--tile-bw) solid #1B7A5A !important; color:#14302A !important; opacity:1 !important}
.st-key-tiles_good [data-testid="stBaseButton-primary"]::after, .st-key-tiles_good button[kind="primary"]::after {content:"\\2713"; position:absolute; top:8px; right:8px; width:34px; height:34px; border-radius:50%; background:#1B7A5A; color:#fff; display:grid; place-items:center; font-size:20px; font-weight:700}
.st-key-tiles_hint [data-testid="stBaseButton-primary"], .st-key-tiles_hint button[kind="primary"] {background:#FBEDC2 !important; border:var(--tile-bw) solid #F2B52E !important; color:#14302A !important; box-shadow:0 0 0 6px #FBEDC2 !important; animation:glow 1.4s ease-in-out infinite}
@keyframes glow {0%,100% {transform:scale(1)} 50% {transform:scale(1.03)}}
.lab {text-align:center; font-family:'Baloo Chettan 2','Noto Sans Malayalam',sans-serif; font-weight:600; font-size:20px; margin-top:6px; line-height:1.2}
.dots {display:flex; gap:8px; justify-content:center; align-items:center}
.dots {gap:5px !important; flex-wrap:nowrap}
.dot {width:13px; height:13px; min-width:13px; flex:none; box-sizing:border-box; border-radius:50%; border:3px solid #CFE0D6; display:inline-block}
.dot.ok {background:#1B7A5A; border-color:#1B7A5A}
.dot.help {background:#F2B52E; border-color:#F2B52E}
.dot.cur {border-color:#14302A}
.lvl {text-align:right; font-size:14px; color:#566D65}
.prompt {background:#fff; border:1px solid #CFE0D6; border-radius:26px; padding:20px; box-shadow:0 6px 18px rgba(20,48,42,.07); margin:8px 0 6px}
.bigword {font-family:'Baloo Chettan 2','Noto Sans Malayalam',sans-serif; font-weight:700; font-size:clamp(44px,12vw,68px); line-height:1.1; overflow-wrap:anywhere}
.bigglyph {font-size:64px; line-height:1.15; overflow-wrap:anywhere}
.bigglyph.count {font-size:46px; letter-spacing:6px}
.price {display:inline-block; background:#F2B52E; color:#3A2A00; font-family:'Baloo Chettan 2',sans-serif; font-weight:700; font-size:30px; border-radius:14px; padding:2px 14px; margin-left:12px; vertical-align:middle}
.ptext {font-size:19px; color:#566D65; margin-top:8px}
.ptext.lead {font-size:clamp(24px,6vw,30px); color:#14302A; font-family:'Baloo Chettan 2','Noto Sans Malayalam',sans-serif; font-weight:600; line-height:1.25; margin-top:0}
.fb {min-height:60px; padding:12px 18px; border-radius:18px; background:#F4F9F6; border:1px solid #CFE0D6; font-size:20px; display:flex; align-items:center; margin:10px 0}
.fb.good {background:#D3EBDF; border-color:#1B7A5A}
.st-key-nextwrap .stButton > button {min-height:64px; font-size:22px; border-radius:18px}
.st-key-nextwrap .stButton > button p {font-size:22px}
.garden {display:flex; flex-wrap:wrap; gap:6px; align-items:flex-end; min-height:56px; padding:8px 12px 4px; border-bottom:8px solid #8B6B4A; border-radius:4px; font-size:34px; line-height:1.1; margin-top:8px}
.garden.big {font-size:48px}
.plant.new {animation:grow .7s ease-out}
@keyframes grow {from {transform:scale(.3) translateY(14px); opacity:.2} to {transform:none; opacity:1}}
.donebox h1 {font-size:clamp(40px,11vw,56px)}

/* teacher view */
.pill {display:inline-block; font-size:14px; font-weight:700; border-radius:999px; padding:3px 12px; background:#F4F9F6; border:1px solid #CFE0D6; white-space:nowrap}
.pill.ok {background:#D3EBDF} .pill.mid {background:#DCE8FA} .pill.need {background:#F9DDD6}
.ttable {width:100%; border-collapse:collapse; font-size:16px}
.ttable th {text-align:left; font-size:13px; letter-spacing:.04em; text-transform:uppercase; color:#566D65; padding:6px 8px; border-bottom:2px solid #CFE0D6}
.ttable td {padding:10px 8px; border-bottom:1px solid #CFE0D6; vertical-align:top}
.tscroll {overflow-x:auto}
.muted {color:#566D65; font-size:15px}
.logline {display:flex; gap:12px; padding:6px 0; border-top:1px solid #CFE0D6; font-size:16px}
.logline time {color:#566D65; flex:none; width:110px; font-size:14px}

body.calm *, .calm-on *, .calm-on *::before, .calm-on *::after {animation:none !important; transition:none !important}
@media (prefers-reduced-motion: reduce) {* {animation:none !important; transition:none !important}}
@media (max-width:420px) {.bigglyph {font-size:52px} .lab {font-size:17px}}
"""


def inject_css(S):
    xl = S["size"] == "xl"
    tile_h = 200 if xl else 150
    tile_font = "5.6rem" if xl else "4.2rem"
    border = "#14302A" if S["high_contrast"] else "#CFE0D6"
    bw = "5px" if S["high_contrast"] else "3px"
    extra = ".stApp *, .stApp *::before, .stApp *::after{animation:none !important;transition:none !important}" if S["calm"] else ""
    st.markdown(
        f"<style>{CSS}:root{{--tile-h:{tile_h}px;--tile-font:{tile_font};--tile-line:{border};--tile-bw:{bw}}}{extra}"
        f"@media (max-width:520px){{[class*='st-key-tiles'] .stButton > button p{{font-size:calc(var(--tile-font) * .8)}}}}</style>",
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------------ audio
@st.cache_data(show_spinner=False, max_entries=600)
def tts_b64(text, lang):
    """Server audio using gTTS (needs internet on the server). Returns '' on failure."""
    try:
        from gtts import gTTS
        buf = io.BytesIO()
        gTTS(text=text, lang=lang, tld="co.in" if lang == "en" else "com").write_to_fp(buf)
        return base64.b64encode(buf.getvalue()).decode()
    except Exception:
        return ""


LISTEN_HTML = """
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@700&family=Noto+Sans+Malayalam:wght@600&display=swap" rel="stylesheet">
<style>
html,body{margin:0;background:transparent;font-family:'Atkinson Hyperlegible','Noto Sans Malayalam',system-ui,sans-serif}
button{display:inline-flex;gap:10px;align-items:center;min-height:56px;padding:0 24px;border-radius:30px;background:#F2B52E;color:#3A2A00;font-weight:700;font-size:20px;border:0;cursor:pointer;font-family:inherit}
button:focus-visible{outline:4px solid #2F6FD0;outline-offset:3px}
#note{font-size:14px;color:#566D65;margin-top:6px}
</style>
<button id="b" type="button">
<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path d="M3 9v6h4l5 4V5L7 9H3z" fill="currentColor"/><path d="M16 8.5a5 5 0 0 1 0 7M18.5 6a8.5 8.5 0 0 1 0 12" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>
<span>__LABEL__</span></button>
<div id="note" hidden></div>
__AUDIO__
<script>
const TEXT=__TEXT__, LANG=__LANG__, RATE=__RATE__, ENGINE=__ENGINE__, CHIME=__CHIME__, AUTO=__AUTO__;
const note=document.getElementById('note'), audio=document.getElementById('a');
function say(m){note.textContent=m;note.hidden=false}
function speak(){
  if(ENGINE==='audio'&&audio){try{audio.currentTime=0;audio.play().catch(function(){})}catch(e){}return}
  try{
    const ss=window.speechSynthesis;
    if(!ss||!window.SpeechSynthesisUtterance){say('This browser cannot read aloud.');return}
    ss.cancel();
    const voices=ss.getVoices()||[], want=LANG.toLowerCase();
    let v=voices.find(function(x){return x.lang.replace('_','-').toLowerCase()===want})||voices.find(function(x){return x.lang.toLowerCase().indexOf(want.slice(0,2))===0});
    if(!v&&voices.length&&want.indexOf('ml')===0){say('No Malayalam voice on this device. A teacher can switch to server audio in settings.');return}
    const u=new SpeechSynthesisUtterance(TEXT);u.lang=LANG;u.rate=RATE;if(v)u.voice=v;ss.speak(u);
  }catch(e){}
}
function chime(){
  try{
    const C=window.AudioContext||window.webkitAudioContext,ac=new C(),t=ac.currentTime;
    [523.25,659.25,783.99].forEach(function(f,i){
      const o=ac.createOscillator(),g=ac.createGain();o.type='sine';o.frequency.value=f;
      g.gain.setValueAtTime(0,t+i*.12);g.gain.linearRampToValueAtTime(.12,t+i*.12+.03);g.gain.exponentialRampToValueAtTime(.001,t+i*.12+.4);
      o.connect(g);g.connect(ac.destination);o.start(t+i*.12);o.stop(t+i*.12+.45);
    });
  }catch(e){}
}
document.getElementById('b').addEventListener('click',speak);
window.addEventListener('load',function(){if(CHIME)chime();if(AUTO)setTimeout(speak,250)});
</script>
"""


def listen_widget(text, S, chime=False):
    lang = "ml-IN" if st.session_state.lang == "ml" else "en-IN"
    engine, audio_tag = "browser", ""
    if S["audio_engine"] == "server":
        data = tts_b64(text, st.session_state.lang)
        if data:
            engine = "audio"
            audio_tag = f'<audio id="a" src="data:audio/mp3;base64,{data}"></audio>'
    page = (LISTEN_HTML
            .replace("__LABEL__", esc(T(UI["listen"])))
            .replace("__AUDIO__", audio_tag)
            .replace("__TEXT__", json.dumps(text))
            .replace("__LANG__", json.dumps(lang))
            .replace("__RATE__", str(float(S["voice_speed"])))
            .replace("__ENGINE__", json.dumps(engine))
            .replace("__CHIME__", "true" if chime and S["chime"] else "false")
            .replace("__AUTO__", "true" if S["read_aloud"] else "false"))
    if hasattr(st, "iframe"):          # newer Streamlit
        st.iframe(page.strip(), height=96)
    else:                              # Streamlit 1.41 to 1.5x
        components.html(page, height=96)


# ------------------------------------------------------------------ learner logic
def init_state():
    ss = st.session_state
    ss.setdefault("mode", "learner")
    ss.setdefault("lang", "en")
    ss.setdefault("learner", "Anu")
    ss.setdefault("screen", "home")
    ss.setdefault("session", None)
    ss.setdefault("cur", None)
    ss.setdefault("level", 2)
    ss.setdefault("streak", 0)
    ss.setdefault("counter", 0)
    ss.setdefault("unlocked", False)


def go_home():
    st.session_state.screen = "home"
    st.session_state.cur = None


def reset_play():
    go_home()
    st.session_state.session = None


def open_question():
    ss = st.session_state
    sess = ss.session
    q = content.QUESTION_BY_ID[sess["qids"][sess["i"]]]
    n = min(ss.level, len(q["pool"]) + 1)
    choices = random.sample(q["pool"], n - 1) + [q["answer"]]
    random.shuffle(choices)
    ss.counter += 1
    ss.cur = {"qid": q["id"], "choices": choices, "wrong": [], "solved": False, "n": ss.counter}
    ss.screen = "question"


def start_set(set_id):
    ss = st.session_state
    S = storage.snapshot(ss.learner)["settings"]
    qids = [q["id"] for q in content.questions_for(set_id)]
    random.shuffle(qids)
    ss.session = {"set": set_id, "qids": qids, "i": 0, "results": [], "plants": []}
    ss.level = int(S["start_choices"])
    ss.streak = 0
    open_question()


def pick(opt_id):
    ss = st.session_state
    cur = ss.cur
    if cur is None or cur["solved"] or opt_id in cur["wrong"]:
        return
    q = content.QUESTION_BY_ID[cur["qid"]]
    if opt_id != q["answer"]:
        cur["wrong"].append(opt_id)
        return
    cur["solved"] = True
    indep = not cur["wrong"]
    if indep:
        ss.streak += 1
        if ss.streak >= 2 and ss.level < 4:
            ss.level += 1
            ss.streak = 0
    else:
        ss.streak = 0
        if len(cur["wrong"]) >= 2 and ss.level > 2:
            ss.level -= 1
    plant = random.choice(FLOWERS) if indep else "🌱"
    ss.session["results"].append(indep)
    ss.session["plants"].append(plant)
    sd = content.SET_BY_ID[q["set"]]
    answer_name = content.OPTIONS[q["answer"]]["en"].lower()
    with storage.edit(ss.learner) as L:
        rec = L["items"].setdefault(q["id"], {"tries": 0, "indep": 0})
        rec["tries"] += 1
        rec["indep"] += int(indep)
        L["garden"].append(plant)
        del L["garden"][:-120]
        storage.add_log(L, f"{sd['en']} · {answer_name} · {'first try' if indep else 'with help'}")


def next_question():
    ss = st.session_state
    sess = ss.session
    sess["i"] += 1
    if sess["i"] >= len(sess["qids"]):
        score = sum(1 for r in sess["results"] if r)
        sd = content.SET_BY_ID[sess["set"]]
        with storage.edit(ss.learner) as L:
            rec = L["sets"].setdefault(str(sess["set"]), {"scores": [], "plays": 0, "last": None})
            rec["scores"].append(score)
            del rec["scores"][:-20]
            rec["plays"] += 1
            rec["last"] = storage.now_iso()
            storage.add_log(L, f"Finished {sd['en']}: {score} of {len(sess['qids'])} on the first try")
        ss.screen = "done"
        ss.cur = None
    else:
        open_question()


# ------------------------------------------------------------------ learner screens
def plants_html(plants, big=False, new_last=False):
    out = []
    for i, p in enumerate(plants):
        cls = "plant new" if (new_last and i == len(plants) - 1) else "plant"
        out.append(f'<span class="{cls}" aria-hidden="true">{p}</span>')
    return f'<div class="garden{" big" if big else ""}">{"".join(out)}</div>'


def home_screen(name, L):
    st.markdown(
        f'<div class="hello"><h1>{esc(T(UI["hello"]))} {esc(name)}!</h1><p>{esc(T(UI["learn"]))}</p></div>',
        unsafe_allow_html=True)
    sets = content.SETS
    for i in range(0, len(sets), 2):
        cols = st.columns(2)
        for col, sd in zip(cols, sets[i:i + 2]):
            rec = L["sets"].get(str(sd["id"]))
            best = f'{T(UI["best"])} {max(rec["scores"])}/10' if rec and rec["scores"] else ""
            with col:
                with st.container(key=f"setcard_{sd['id']}", border=True):
                    st.markdown(
                        f'<div class="setcard"><div class="ico" aria-hidden="true">{sd["icon"]}</div>'
                        f'<div class="nm">{esc(sd[st.session_state.lang])}</div>'
                        f'<div class="cp">{esc(sd["cap_" + st.session_state.lang])}</div>'
                        f'<div class="bs">{esc(best)}</div></div>', unsafe_allow_html=True)
                    st.button(T(UI["go"]), key=f"start_{sd['id']}", on_click=start_set,
                              args=(sd["id"],), use_container_width=True, type="primary")
    st.markdown(f"<h3>{esc(T(UI['garden']))}</h3>", unsafe_allow_html=True)
    st.markdown(plants_html(L["garden"][-30:]), unsafe_allow_html=True)


def spoken_text(q, cur):
    wrong = len(cur["wrong"])
    if cur["solved"]:
        return T(UI["yes"])
    if wrong == 0:
        return T(q["say"])
    return T(UI["try1"] if wrong == 1 else UI["try2"]) + " " + T(q["say"])


def big_block(q):
    big = q["big"]
    if not big:
        return ""
    if big["type"] == "word":
        return f'<div class="bigword">{esc(content.OPTIONS[q["answer"]][st.session_state.lang])}</div>'
    if big["type"] == "count":
        return f'<div class="bigglyph count" aria-label="{big["n"]}">{(big["glyph"] + " ") * big["n"]}</div>'
    if big["type"] == "price":
        return (f'<div><span class="bigglyph" aria-hidden="true">{big["glyph"]}</span>'
                f'<span class="price">{esc(big["price"])}</span></div>')
    return f'<div class="bigglyph" aria-hidden="true">{big["glyph"]}</div>'


def question_screen(S):
    ss = st.session_state
    sess, cur = ss.session, ss.cur
    q = content.QUESTION_BY_ID[cur["qid"]]
    n = len(cur["choices"])

    dots = []
    for i in range(len(sess["qids"])):
        if i < len(sess["results"]):
            dots.append(f'<span class="dot {"ok" if sess["results"][i] else "help"}"></span>')
        else:
            dots.append(f'<span class="dot{" cur" if i == sess["i"] else ""}"></span>')
    with st.container(key="topbar"):
        c1, c2, c3 = st.columns([1.1, 3, 1])
        with c1:
            st.button("← " + T(UI["home"]), key="home_btn", on_click=go_home)
        with c2:
            st.markdown(f'<div class="dots" role="img" aria-label="Question {sess["i"] + 1} of {len(sess["qids"])}">'
                        f'{"".join(dots)}</div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="lvl">{n} {esc(T(UI["pictures"]))}</div>', unsafe_allow_html=True)

    lead = " lead" if not q["big"] else ""
    st.markdown(f'<div class="prompt">{big_block(q)}<p class="ptext{lead}">{esc(T(q["prompt"]))}</p></div>',
                unsafe_allow_html=True)
    listen_widget(spoken_text(q, cur), S, chime=cur["solved"])

    solved = cur["solved"]
    hint = (not solved) and len(cur["wrong"]) >= 2
    show_names = S["show_names"] or q["names"]
    rows = [cur["choices"]] if n <= 3 else [cur["choices"][:2], cur["choices"][2:]]
    with st.container(key="tiles_good" if solved else "tiles_hint" if hint else "tiles"):
        for r, row in enumerate(rows):
            cols = st.columns(len(row))
            for col, oid in zip(cols, row):
                opt = content.OPTIONS[oid]
                is_answer = oid == q["answer"]
                with col:
                    st.button(
                        opt["glyph"], key=f"opt_{cur['n']}_{oid}", on_click=pick, args=(oid,),
                        disabled=(oid in cur["wrong"]) or (solved and not is_answer),
                        type="primary" if (is_answer and (solved or hint)) else "secondary",
                        use_container_width=True)
                    if show_names:
                        st.markdown(f'<div class="lab">{esc(opt[ss.lang])}</div>', unsafe_allow_html=True)

    if solved:
        msg, cls = T(UI["yes"]), " good"
    elif not cur["wrong"]:
        msg, cls = T(UI["start"]), ""
    else:
        msg, cls = T(UI["try1"] if len(cur["wrong"]) == 1 else UI["try2"]), ""
    st.markdown(f'<div class="fb{cls}" role="status" aria-live="polite">{esc(msg)}</div>', unsafe_allow_html=True)
    if solved:
        with st.container(key="nextwrap"):
            st.button(T(UI["next"]) + " →", key=f"next_{cur['n']}", on_click=next_question,
                      type="primary", use_container_width=True)
    st.markdown(plants_html(sess["plants"], new_last=solved), unsafe_allow_html=True)


def done_screen(S):
    ss = st.session_state
    sess = ss.session
    n = len(sess["plants"])
    suffix = T(UI["grew"])
    st.markdown(f'<div class="donebox"><h1>{esc(T(UI["done"]))}</h1></div>', unsafe_allow_html=True)
    st.markdown(plants_html(sess["plants"], big=True), unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:22px;margin-top:12px">{n} {esc(suffix)}</p>', unsafe_allow_html=True)
    listen_widget(T(UI["done"]), S, chime=True)
    st.button(T(UI["again"]), key="again", on_click=start_set, args=(sess["set"],),
              type="primary", use_container_width=True)
    if sess["set"] < len(content.SETS):
        st.button(T(UI["nextset"]), key="nextset", on_click=start_set, args=(sess["set"] + 1,),
                  use_container_width=True)
    st.button(T(UI["home"]), key="done_home", on_click=go_home, use_container_width=True)


def learner_view():
    ss = st.session_state
    name = ss.learner
    L = storage.snapshot(name)
    S = L["settings"]
    inject_css(S)
    st.radio("Language", ["en", "ml"], format_func=lambda x: {"en": "English", "ml": "മലയാളം"}[x],
             horizontal=True, key="lang", label_visibility="collapsed")
    if ss.screen == "question" and ss.cur and ss.session:
        question_screen(S)
    elif ss.screen == "done" and ss.session:
        done_screen(S)
    else:
        ss.screen = "home"
        home_screen(name, L)


# ------------------------------------------------------------------ teacher view
def set_status(rec):
    scores = rec["scores"] if rec else []
    if not scores:
        return "none", "Not started", "Not tried yet."
    last = scores[-2:]
    if (len(last) == 2 and min(last) >= 8) or scores[-1] == 10:
        return "ok", "Mastered", "Ready for the next set."
    if scores[-1] <= 4:
        return "need", "Needs support", "Try 2 pictures and turn on names under pictures."
    return "mid", "Practising", "Keep going with short sessions."


def pretty_time(iso):
    try:
        return datetime.fromisoformat(iso).strftime("%d %b, %H:%M")
    except (TypeError, ValueError):
        return ""


def teacher_pin():
    try:
        pin = st.secrets.get("teacher_pin")
    except Exception:
        pin = None
    return pin or os.environ.get("PYQOO_TEACHER_PIN")


def csv_export(name, L):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["learner", "set", "question_id", "answer_en", "tries", "first_try_correct"])
    for qid, rec in sorted(L["items"].items()):
        q = content.QUESTION_BY_ID.get(qid)
        if not q:
            continue
        w.writerow([name, content.SET_BY_ID[q["set"]]["en"], qid,
                    content.OPTIONS[q["answer"]]["en"], rec["tries"], rec["indep"]])
    return buf.getvalue()


def teacher_view():
    ss = st.session_state
    inject_css(storage.snapshot(ss.learner)["settings"])
    pin = teacher_pin()
    if pin and not ss.unlocked:
        st.markdown("## Teacher or parent")
        entered = st.text_input("Enter the PIN", type="password", key="pin_input")
        if entered:
            if entered == str(pin):
                ss.unlocked = True
                st.rerun()
            else:
                st.error("That PIN is not correct.")
        return

    name = ss.learner
    L = storage.snapshot(name)
    S = L["settings"]
    st.markdown(f"## {esc(name)}")
    st.caption("Progress and settings. Everything the learner does shows up here.")

    statuses = {sd["id"]: set_status(L["sets"].get(str(sd["id"]))) for sd in content.SETS}
    mastered = sum(1 for s in statuses.values() if s[0] == "ok")
    tries = sum(r["tries"] for r in L["items"].values())
    indep = sum(r["indep"] for r in L["items"].values())
    sessions = sum(r["plays"] for r in L["sets"].values())
    c1, c2, c3 = st.columns(3)
    c1.metric("Sets mastered", f"{mastered} of {len(content.SETS)}")
    c2.metric("Sessions played", sessions)
    c3.metric("Right on first try", f"{round(100 * indep / tries)}%" if tries else "None yet")

    with st.container(border=True):
        st.markdown("#### Term goal")
        goal = int(S["goal_sets"])
        st.write(f"Master {goal} sets. Mastered so far: {mastered}.")
        st.progress(min(1.0, mastered / goal) if goal else 0.0)

    with st.container(border=True):
        st.markdown("#### Sets")
        st.caption("Mastered means 8 or more right on the first try in the last two sessions.")
        rows = []
        for sd in content.SETS:
            rec = L["sets"].get(str(sd["id"]))
            kind, label, note = statuses[sd["id"]]
            last = f'{rec["scores"][-1]}/10' if rec and rec["scores"] else ""
            best = f'{max(rec["scores"])}/10' if rec and rec["scores"] else ""
            rows.append(
                f'<tr><td>{sd["icon"]} {esc(sd["en"])}<div class="muted">{esc(sd["ml"])}</div></td>'
                f'<td><span class="pill {kind}">{label}</span></td><td>{last}</td><td>{best}</td>'
                f'<td class="muted">{esc(note)}</td></tr>')
        st.markdown('<div class="tscroll"><table class="ttable"><tr><th>Set</th><th>Status</th><th>Last</th>'
                    f'<th>Best</th><th>Next step</th></tr>{"".join(rows)}</table></div>',
                    unsafe_allow_html=True)

    weak = []
    for qid, rec in L["items"].items():
        q = content.QUESTION_BY_ID.get(qid)
        if q and rec["tries"] >= 2 and rec["indep"] / rec["tries"] < 0.5:
            weak.append((rec["indep"] / rec["tries"], content.SET_BY_ID[q["set"]]["en"],
                         content.OPTIONS[q["answer"]]["en"]))
    with st.container(border=True):
        st.markdown("#### Needs more practice")
        if weak:
            for _, set_name, ans in sorted(weak)[:12]:
                st.write(f"{ans} ({set_name})")
        else:
            st.caption("Nothing yet. Items asked at least twice with fewer than half right on the first try appear here.")

    with st.container(border=True):
        st.markdown("#### Recent activity")
        if L["log"]:
            html_rows = "".join(f'<div class="logline"><time>{pretty_time(e["t"])}</time><span>{esc(e["text"])}</span></div>'
                                for e in L["log"][:10])
            st.markdown(html_rows, unsafe_allow_html=True)
        else:
            st.caption("No activity yet.")

    with st.container(border=True):
        st.markdown("#### Session settings")
        with st.form("settings_form"):
            start = st.selectbox("Pictures to choose from at the start", [2, 3, 4],
                                 index=[2, 3, 4].index(int(S["start_choices"])),
                                 help="2 is the gentlest. It grows to 4 after steady first-try answers.")
            speed = st.slider("Voice speed", 0.6, 1.1, float(S["voice_speed"]), 0.05)
            size = st.selectbox("Picture size", ["large", "xl"], index=["large", "xl"].index(S["size"]),
                                format_func=lambda x: {"large": "Large", "xl": "Extra large"}[x])
            engine = st.radio("Voice source", ["browser", "server"], index=["browser", "server"].index(S["audio_engine"]),
                              format_func=lambda x: {"browser": "This device's voice",
                                                     "server": "Server audio (gTTS, needs internet)"}[x],
                              help="Choose server audio if the device has no Malayalam voice.")
            read_aloud = st.checkbox("Read each question aloud", value=S["read_aloud"])
            chime = st.checkbox("Soft chime on a right answer", value=S["chime"])
            names = st.checkbox("Show names under pictures", value=S["show_names"])
            calm = st.checkbox("Calm mode (no movement)", value=S["calm"])
            contrast = st.checkbox("High contrast outlines", value=S["high_contrast"])
            goal_in = st.number_input("Term goal: sets to master", 1, 10, int(S["goal_sets"]))
            if st.form_submit_button("Save settings", type="primary"):
                with storage.edit(name) as LL:
                    LL["settings"].update({
                        "start_choices": start, "voice_speed": speed, "size": size, "audio_engine": engine,
                        "read_aloud": read_aloud, "chime": chime, "show_names": names, "calm": calm,
                        "high_contrast": contrast, "goal_sets": int(goal_in)})
                st.success("Saved.")
                st.rerun()

    with st.container(border=True):
        st.markdown("#### Data")
        st.download_button("Download results (CSV)", csv_export(name, L), file_name=f"{name}_results.csv",
                           mime="text/csv")
        st.caption("Progress is saved on the server for this learner. Collect only what you need and "
                   "get parent consent before use. Keep exports private.")
        sure = st.checkbox("I understand this removes all progress for this learner", key="reset_ok")
        if st.button("Reset progress", disabled=not sure):
            with storage.edit(name) as LL:
                LL["sets"], LL["items"], LL["garden"], LL["log"] = {}, {}, [], []
            reset_play()
            st.rerun()


# ------------------------------------------------------------------ sidebar and routing
def add_learner():
    new = st.session_state.get("new_learner", "").strip()[:30]
    if new:
        storage.ensure_learner(new)
        st.session_state.learner = new
        st.session_state.new_learner = ""
        reset_play()


def main():
    init_state()
    ss = st.session_state
    storage.ensure_learner(ss.learner)
    with st.sidebar:
        st.markdown("### Pyqoo Easy")
        st.radio("View", ["learner", "teacher"], key="mode",
                 format_func=lambda x: {"learner": "Learner", "teacher": "Teacher or parent"}[x])
        st.selectbox("Learner", storage.learner_names(), key="learner", on_change=reset_play)
        with st.expander("Add a learner"):
            st.text_input("Name", key="new_learner", max_chars=30)
            st.button("Add", on_click=add_learner)
    if ss.mode == "teacher":
        teacher_view()
    else:
        learner_view()


main()
