# accounts.py

import os
import json
import tempfile
from threading import Lock
from uuid import uuid4

_ACCOUNTS_PATH = "Accounts.json"
_SAVES_DIR     = "saves"
_lock          = Lock()

def _atomic_write(path: str, data) -> None:
    """
    Atomically write JSON-serializable `data` to `path`.
    Writes to a temp file then renames it into place.
    """
    # Ensure directory exists
    dirpath = os.path.dirname(path) or "."
    os.makedirs(dirpath, exist_ok=True)

    # Write to a temp file in the same directory
    with tempfile.NamedTemporaryFile("w", dir=dirpath, delete=False, encoding="utf-8") as tf:
        json.dump(data, tf, ensure_ascii=False, indent=2)
        tf.flush()
        os.fsync(tf.fileno())

    # Atomically replace the target
    os.replace(tf.name, path)

def load_accounts() -> dict[str, str]:
    """
    Load Accounts.json and return a dict mapping email → user_id.
    If the file is missing or corrupted, returns an empty dict.
    """
    try:
        with open(_ACCOUNTS_PATH, "r", encoding="utf-8") as f:
            entries = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    # entries is a list of {"email":..., "user_id":...}
    return { e["email"]: e["user_id"] for e in entries }

def save_accounts_index(index: dict[str, str]) -> None:
    """
    Persist the email→user_id map to Accounts.json atomically.
    """
    entries = [ {"email": email, "user_id": uid} for email, uid in index.items() ]
    with _lock:
        _atomic_write(_ACCOUNTS_PATH, entries)

def get_or_create_user_id(email: str) -> str:
    """
    Lookup an existing user_id by email, or create a new one if missing.
    Always lowercases the email for consistency.
    """
    email = email.strip().lower()
    accounts = load_accounts()

    if email in accounts:
        return accounts[email]

    # New registration
    user_id = uuid4().hex[:12]
    accounts[email] = user_id
    save_accounts_index(accounts)

    # Initialize an empty save file
    os.makedirs(_SAVES_DIR, exist_ok=True)
    save_path = os.path.join(_SAVES_DIR, f"{user_id}.json")
    _atomic_write(save_path, {"email": email, "characters": []})

    return user_id


