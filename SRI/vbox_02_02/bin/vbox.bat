@ECHO OFF
CLS

REM vbox
REM Created by Castellani Davide & Sabaini Chiara

REM %1 = vm name
REM %2 = vm net setting

REM Writing on the file log.log
ECHO %date% >> ../log/bat_log.log
ECHO Starting %time% >> ../log/bat_log.log
ECHO Execution program >> ../log/bat_log.log

REM Go in the correct path (change it if you don't use the standard path)
CD ..\virtualboxm

REM Turn off
VBoxManage.exe controlvm %1 poweroff soft
ECHO Turn off the vm %1 >> ../log/bat_log.log

REM Make sure the machine name is correct
if %ERRORLEVEL% == 1 goto end

REM Change settings
VBoxManage.exe modifyvm %1 --nic1 %2
ECHO Setting the vm %1's network setting to %2 >> ../log/bat_log.log

REM Turn on
VBoxManage.exe startvm %1
ECHO Turn on the machine %1 >> ../log/bat_log.log
GOTO EOF

:end
ECHO There is an error, make sure you put the correct machine name and net name
REM Writing on log.log
ECHO There is an error, make sure you put the correct machine name and net name >> ../log/bat_log.log
GOTO EOF

:EOF

REM Writing the log.log file in the log folder
ECHO End program >> ../log/bat_log.log
ECHO Ending %time% >> ../log/bat_log.log
ECHO. >> ../log/bat_log.log