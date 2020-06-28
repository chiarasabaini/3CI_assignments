# virtualbox cli

## Descrition
This is a test of VMachines and show you some datas (eg. the name of your VMachines).

## Can I do it ?
To reply the test we need:
- Windows or Linux (I don't test it with MacOS)
- Vbox Oracle
- (A Vmachine on Vbox Oracle, if you will see something in the first file)

And we can write on cmd(Windows) or the shell of Linux:
- cd [Director of the Vmachine menager]
- name_of_progr list vms > vmsinstalled.txt
- name_of_progr list vms ostypes > vmsinstalledos.txt

The name_of_progr depends by the OS:
- Windows:
  - VBoxManage.exe
- Linux:
  - vboxmanage


Now you have all the file in the same folder.

## Changelog 
- [01.01_2020-2-28](#0101_2020-2-28)

---
### 01.01_2020-2-28
 - Now there are two file, that rappresent the outputs of 2 instructions:

    | Istructions by cmd               	| File generated       	|
    |---------------------------------	|--------------------	|
    | Vboxmanage.exe list vms         	| vmsinstalled.txt   	|
    | VBoxManage.exe list vms ostypes 	| vmsinstalledos.txt 	|

By Davide Castellani

---
If you have any problem please contact me:
- contacts@castellanidavide.it
