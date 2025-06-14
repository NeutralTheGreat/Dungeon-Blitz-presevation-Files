# 🧪 Dungeon Blitz - SWF Modding & Local Server Setup

> Everything you need to know about what was changed in `DungeonBlitz.swf` and how to run it with your own server.

---

## 🎯 Purpose of This SWF

This is a **modified version** of the original `DungeonBlitz.swf` file to:

- Enable **local server testing**
- Provide **real-time debugging** using trace logs
- Make it easier to reverse-engineer and study game behavior

---

## 🔍 What Was Changed?

### ✅ 1. Localhost Networking

- Replaced original server IPs with `127.0.0.1`
- This forces the client to connect to your **local Python server** instead of the live game servers (which are dead anyway)

> ⚠️ This is done in `LinkUpdater.as`. If you build your own SWF, you **must** do the same.

---

### ✅ 2. Tracers for Debugging

- Inserted `trace()` calls throughout critical functions
- Useful for:
  - Logging game state
  - Catching failed auth or asset loads
  - Monitoring real-time behavior

> 🔧 These logs will appear if you use the **Flash Debug Player** and have `mm.cfg` set up correctly (see main README).

---

## 🛠 Custom SWF Usage

Want to use your own SWF?

1. Decompile and patch `LinkUpdater.as`
2. Replace the IP with:
   ```as3
   var ip:String = "127.0.0.1";
   ```
3. Recompile and drop the SWF in `game-files/`

If you don't patch this, the game will silently fail to connect — and you'll waste hours debugging a non-issue.

