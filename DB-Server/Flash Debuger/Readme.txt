
the Credit goes to cold.ic  for giving me the Flash debugger  files 

it works with flashpoint make sure to drop this exe file into the directory  FPSoftware\Flash\ and replace the launch command with FPSoftware\Flash\flashplayer32_0r0_465_sa_debug.exe 
Also make sure to drop the file mm.cfg in %USERPROFILE% directory as that turns on debugging in flash.

then read the logs in real time in powershell:
get-content "$env:APPDATA\Macromedia\Flash Player\Logs\flashlog.txt" -wait -tail 1