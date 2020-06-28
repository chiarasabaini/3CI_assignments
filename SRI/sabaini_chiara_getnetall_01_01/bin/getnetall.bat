@ECHO OFF

REM author: Sabaini Chiara 3CI - email: 18762@studenti.marconiverona.edu.it
REM version: 01.01
REM date: 2020-05-13

REM executes "getnetall.vbs" and redirects its output in "getnetall.log"

ECHO %date% %time% >> ..\log\getnetall.log
CSCRIPT getnetall.vbs >> ..\log\getnetall.log