@ECHO OFF

REM author: Sabaini Chiara 3CI - email: 18762@studenti.marconiverona.edu.it
REM version: 01.01
REM date: 2020-05-17

REM executes "getinfo.py" and redirects its output in "getinfo.log"

PYTHON getinfo.py >> ..\log\getinfo.log

ECHO ------- >> ..\log\getinfo.log
