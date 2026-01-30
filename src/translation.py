import json
from pathlib import Path
from src.settings import load_settings

def load_translation():
    settings = load_settings()
    lang = settings["language"].lower()
    file_path = Path(f"data/{lang}.json")

    if not file_path.exists():
        file_path = Path("data/fr.json")  # fallback

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

T = load_translation()
