"""Pre-generate Malayalam audio clips for Pyqoo Easy (saves Sarvam cost: each sentence is made once).

Usage (run in the folder that contains app.py):
    python make_audio.py --dry-run        count clips, characters and estimated cost
    python make_audio.py                  generate missing clips into audio/ml/
Needs SARVAM_API_KEY in the environment or in .streamlit/secrets.toml.
Re-run after you edit any Malayalam question text; only new or changed sentences are generated.
Optional: SARVAM_RATE_PER_1000 (rupees per 1000 characters, default 1.0).
"""
import base64, hashlib, json, os, re, sys, time, types, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "audio", "ml")
URL = "https://api.sarvam.ai/text-to-speech"


def clip_name(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:16] + ".mp3"   # same as voice.clip_name in app.py


def load_texts():
    src = open(os.path.join(HERE, "app.py"), encoding="utf-8").read()
    mods = dict(re.findall(r"_SOURCES\['(\w+)'\] = r'''\n(.*?)\n'''\n", src, re.S))
    for name in ("items_a", "items_b", "items_c", "life_a", "life_b", "content"):
        m = types.ModuleType(name)
        sys.modules[name] = m
        exec(compile(mods[name], name, "exec"), m.__dict__)
    C = sys.modules["content"]
    texts = set()
    for bank in C.BANK.values():
        for q in bank:
            texts.add(q["ml"].strip())
            texts.add(q["why_ml"].strip())
    texts.add("നമസ്കാരം, ഞാൻ പിക്കൂ ആണ്. നമുക്ക് ഒരുമിച്ച് പഠിക്കാം.")
    return sorted(t for t in texts if t)


def secret(name):
    if os.environ.get(name):
        return os.environ[name]
    p = os.path.join(HERE, ".streamlit", "secrets.toml")
    if os.path.isfile(p):
        m = re.search(r'^\s*%s\s*=\s*"([^"]+)"' % name, open(p, encoding="utf-8").read(), re.M)
        if m:
            return m.group(1)
    return ""


def make(text, key):
    body = {"text": text, "target_language_code": "ml-IN", "model": secret("SARVAM_MODEL") or "bulbul:v4-flash",
            "speaker": secret("SARVAM_SPEAKER") or "shilpa_hi_narration", "pace": 1.0, "speech_sample_rate": 24000,
            "output_audio_codec": "mp3"}
    for attempt in range(4):
        req = urllib.request.Request(URL, data=json.dumps(body).encode("utf-8"), method="POST",
                                     headers={"Content-Type": "application/json", "api-subscription-key": key})
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return base64.b64decode(json.loads(r.read().decode("utf-8"))["audios"][0])
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2 * (attempt + 1)); continue
            raise RuntimeError("Sarvam %s: %s" % (e.code, e.read().decode("utf-8", "ignore")[:160]))
    raise RuntimeError("failed")


def main():
    texts = load_texts()
    missing = [t for t in texts if not os.path.isfile(os.path.join(OUT, clip_name(t)))]
    chars = sum(len(t) for t in missing)
    rate = float(os.environ.get("SARVAM_RATE_PER_1000", "1.0"))
    print("%d sentences, %d still to make, %d characters, about Rs %.1f at Rs %.2f per 1000 characters" % (len(texts), len(missing), chars, chars / 1000 * rate, rate))
    if "--dry-run" in sys.argv or not missing:
        return
    key = secret("SARVAM_API_KEY")
    if not key:
        sys.exit("Set SARVAM_API_KEY first (environment variable or .streamlit/secrets.toml).")
    os.makedirs(OUT, exist_ok=True)
    for i, t in enumerate(missing, 1):
        with open(os.path.join(OUT, clip_name(t)), "wb") as f:
            f.write(make(t, key))
        if i % 25 == 0 or i == len(missing):
            print("  %d / %d" % (i, len(missing)))
    print("Done. Upload the audio/ml folder together with app.py.")


main()
