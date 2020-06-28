@echo off
setlocal
set SDK_DIR=%~dp0
"%SDK_DIR%\bin\monitor-bin.exe" %*
endlocal
pause
