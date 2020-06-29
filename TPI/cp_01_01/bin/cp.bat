@ECHO ON
REM gives the info about the language settings of the computer
CLS
SYSTEMINFO > %COMPUTERNAME%_INFO.txt
FINDSTR /c:"Impostazioni locali di input" INFO.txt > %COMPUTERNAME%_CP.txt
CHCP >> %COMPUTERNAME%_CP.txt
TZUTIL /g >> %COMPUTERNAME%_CP.txt