# VBOX

## Tags
 #vbox, #vboxmanage, #log, #network, #batch, #python

## Description
There are two imgs, that represents the differences between NAT, Bridge systems and local machine. 

The program vbox.bat changes the network setting of a virtual machine.

From the v02.01 there's a file called "vbox.bat", his parameters are:
- %1 : vm name
- %2 : network setting (nat or bridged)

## Required
- working vm

---

### Directories structure
- bin
  - Bridge.png
  - NAT.png
  - vbox.bat
  - vbox.py
  
- doc
  - README.md
  - vmsfromp.csv
  
- log
  - bat_log.log
  - py_log.log
  
- virtualboxm
  - VBoxDDU.dll
  - VBoxManage.exe
  - VBoxRT.dll
  
---

### Execution examples
- vbox.bat : 
  - open cmd
  - go in the directory with vbox.bat
  - call "vbox ROS2 nat"
  - you can find a log file called "bat_log.log" in the directory "log"

- vbox.py :
  - double click on it
  -  you can see the output in "vmsfromp.csv"
  - you can find a log file called "py_log.log" in the directory "log"

---

## Changelog 
- [02.02_2020-3-20](#0202_2020-3-20)
- [02.01_2020-3-14](#0201_2020-3-14)
- [01.01_2020-3-12](#0201_2020-3-12)

---
### 02.02_2020-3-20
- #### Added
  - there's a program in python 
  - log's files

---
### 02.01_2020-3-14
 - #### Added
	 - now it's parametrized

---

### 01.01_2020-3-12
 - now you can see 2 images in bin

---

#### By Castellani Davide & Sabaini Chiara

---
If you have any problem please contact us:
- chiara@sabaini.com
- contacts@castellanidavide.it 