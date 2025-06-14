# 🔧 Setup with Debug Flash Player

1. Copy the debugger Flash Player EXE:
  - Drop `flashplayer32_0r0_465_sa_debug.exe` into:
  ```bash
  Flashpoint/FPSoftware/Flash/
  ```

2. Replace the default launcher path:
  - In Flashpoint, edit your game entry
  - Change the "Application Path" to:
  ```bash
  FPSoftware\Flash\flashplayer32_0r0_465_sa_debug.exe
  ```

3. Place mm.cfg into your user directory:
```bash
C:\Users\%USERPROFILE%\mm.cfg
```

This enables debugging output and log generation.

## 📜 How to Read Flash Logs in Real Time

Open PowerShell and run:

```bash
get-content "$env:APPDATA\Macromedia\Flash Player\Logs\flashlog.txt" -wait -tail 1
```

This lets you watch internal Flash logs live as the game runs — essential for debugging and behavior analysis.

## 🤝 Credits

💻 **Flash Debugger Files:** Coldice (cold.ic)

🎮 **Game Developer:** Blue Mammoth Games

🧊 **Emulator & Platform:** Flashpoint

🛠 **Project Maintainer:** @NeutralTheGreat