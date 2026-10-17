"""Saves learner progress and settings to one JSON file.

Good enough for a pilot with a handful of learners. For many users, replace the
_read and _write functions with a database such as SQLite or Supabase.
On Streamlit Community Cloud the disk is wiped when the app restarts, so use a
server with a persistent folder (set PYQOO_DATA_DIR) for real pilots.
"""
import json
import os
import threading
from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(os.environ.get("PYQOO_DATA_DIR", "data"))
DB_FILE = DATA_DIR / "progress.json"
_LOCK = threading.Lock()

DEFAULT_SETTINGS = {
    "start_choices": 2,       # 2, 3 or 4 pictures at the start
    "voice_speed": 0.85,      # 0.6 to 1.1
    "read_aloud": True,
    "chime": True,
    "show_names": False,      # names under pictures
    "size": "large",          # "large" or "xl"
    "calm": False,            # no movement
    "high_contrast": False,
    "audio_engine": "browser",  # "browser" or "server"
    "goal_sets": 5,           # term goal: number of mastered sets
}


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def _new_learner():
    return {"settings": deepcopy(DEFAULT_SETTINGS), "sets": {}, "items": {},
            "garden": [], "log": [], "created": now_iso()}


def _read():
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            db = json.load(f)
            if isinstance(db, dict) and isinstance(db.get("learners"), dict):
                return db
    except (OSError, ValueError):
        pass
    return {"learners": {}}


def _write(db):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    tmp = DB_FILE.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=1)
    os.replace(tmp, DB_FILE)


def _ensure(db, name):
    learner = db["learners"].setdefault(name, _new_learner())
    learner["settings"] = {**DEFAULT_SETTINGS, **learner.get("settings", {})}
    for key, default in (("sets", {}), ("items", {}), ("garden", []), ("log", [])):
        learner.setdefault(key, default)
    return learner


def learner_names():
    with _LOCK:
        return sorted(_read()["learners"].keys())


def snapshot(name):
    """Read-only copy of one learner's record."""
    with _LOCK:
        return deepcopy(_ensure(_read(), name))


@contextmanager
def edit(name):
    """Use as: with storage.edit(name) as learner: ...  Changes are saved on exit."""
    with _LOCK:
        db = _read()
        learner = _ensure(db, name)
        yield learner
        _write(db)


def ensure_learner(name):
    with edit(name):
        pass


def add_log(learner, text):
    learner["log"].insert(0, {"t": now_iso(), "text": text})
    del learner["log"][200:]
