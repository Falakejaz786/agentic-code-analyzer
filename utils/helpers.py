import json
import os

def save_json(data: dict, filepath: str):
    """Save dictionary to JSON file."""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def load_json(filepath: str) -> dict:
    """Load dictionary from JSON file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r") as f:
        return json.load(f)

def log_message(message: str, filepath: str = "outputs/log.txt"):
    """Append a log message to a file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "a") as f:
        f.write(message + "\n")
