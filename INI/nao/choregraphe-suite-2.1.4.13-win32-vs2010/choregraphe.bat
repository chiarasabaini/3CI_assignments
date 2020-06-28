@echo off
setlocal
set SDK_DIR=%~dp0
"%SDK_DIR%\bin\choregraphe_launcher.exe" %*
endlocal
pause
