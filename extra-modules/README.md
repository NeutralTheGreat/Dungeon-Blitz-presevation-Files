# 🧩 Decrypted SWZ Files (Currently Unused)

> These are decrypted `.swz` runtime libraries from Dungeon Blitz.  
> We’re not currently using them — but we’ve preserved them for future exploration, debugging, or restoration of missing client-side logic.

---

## 📄 What Are These?

These files are decrypted versions of custom Adobe SWZ modules used by the original Dungeon Blitz Flash client:

| File Name       | Purpose (Assumed)                        |
|----------------|-------------------------------------------|
| `Game.swz.txt`  | Likely contains core game logic          |
| `Login.swz.txt` | Likely manages authentication/login flow |
| `Init.swz.txt`  | Likely sets up runtime/init environment  |

They were encrypted RSLs (Runtime Shared Libraries) loaded during game startup. We decrypted and saved them in `.txt` format.

---

## ❓ Why Aren’t We Using Them?

We haven’t yet figured out:
- **How to correctly re-link these into the SWF**
- Whether they are actually needed by the current version
- How to load RSLs in a local FlashPlayer runtime setup

> For now, the game appears to work **without** them, using a patched `DungeonBlitz.swf`.

---

## 🔒 Why Keep Them?

- They may contain **game logic we’re currently missing** or not seeing in the SWF
- Useful for **future reverse engineering**
- We may eventually need to patch the SWF to call them again
- They could include classes or assets used in live multiplayer or other features