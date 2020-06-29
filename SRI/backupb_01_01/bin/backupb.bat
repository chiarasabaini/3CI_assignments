@ECHO ON
REM backupb
REM Created by Castellani Davide and Sabaini Chiara
REM Does a backup

IF EXIST C:\Temp\ GOTO OK
ECHO ------------------------------
ECHO SORRY, C:\Temp DOESN'T EXIST.
ECHO I CAN'T PROCEED :(
ECHO ------------------------------
GOTO END

:OK
XCOPY %USERPROFILE%\Documents C:\Temp /E /C /I /Y

:END