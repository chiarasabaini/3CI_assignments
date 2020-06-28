@ECHO OFF
CLS

REM vbox
REM Created by Castellani Davide & Sabaini Chiara

REM %1 = vm name
REM %2 = vm net setting

REM Go in the correct path (change it if you don't use the standard path)
CD C:\Program Files\Oracle\VirtualBox

REM Turn off
VBoxManage.exe controlvm %1 poweroff soft

REM Make sure the machine name is correct
if %ERRORLEVEL% == 1 goto end

REM Change settings
VBoxManage.exe modifyvm %1 --nic1 %2

REM Turn on
VBoxManage.exe startvm %1
GOTO EOF

:end
ECHO There is an error, make sure you put the correct machine name and net name
GOTO EOF

:EOF