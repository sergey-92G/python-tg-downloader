import json
from pathlib import Path
from domain.models import Config

CONFIG_PATH = Path("config.json")

def save_config(config: Config):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config.model_dump(), f, ensure_ascii=False, indent=2)

def load_config() -> Config | None:
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Config(**data)
    return None
