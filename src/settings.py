import json
from pathlib import Path

SETTINGS_FILE = Path("settings.json")

default_settings = {
    "language": "FR",
    "music_volume": 0.5,
    "sfx_volume": 0.5,
    "music_enabled": True,
    "sfx_enabled": True
}


def load_settings():
    if SETTINGS_FILE.exists():
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return default_settings.copy()

def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)
