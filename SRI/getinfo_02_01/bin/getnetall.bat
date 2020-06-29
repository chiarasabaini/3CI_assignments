@ECHO OFF

REM author: Sabaini Chiara 3CI - email: 18762@studenti.marconiverona.edu.it
REM version: 01.02
REM date: 2020-05-16

REM executes "getnetall.vbs" and redirects its output in "getnetall.log"

CSCRIPT getnetall.vbs >> ..\log\getnetall.log

ECHO -------- >> ..\log\getnetall.log