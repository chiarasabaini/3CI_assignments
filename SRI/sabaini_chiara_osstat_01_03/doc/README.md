# OSSTAT

## Tags

 #tpi, #os, #filesystem, #osstat, #python, #properties, #csv, #time

## Description

This program uses the os.walk() funcion to browse trough the directory and the os.stat() function to see the files properties, and creates a csv file with all the properties

## Required

- a working version of python 3.6+
  
---

### Directories structure

- bin
  - osstat.py
- doc
  - README.md
- log
  - log.log
- flussi
  - osstat.csv

---

### Execution examples

- osstat.py:
  - open the source code and set the "directory" variable to the name of the directory you want to work with, and the "directory_path" to the path of that directory
  - double click

---

## Changelog

- [01.03_2020-05-07](#0103_2020-05-07)
- [01.02_2020-05-07](#0102_2020-05-07)
- [01.01_2020-05-04](#0101_2020-05-04)

---

### 01.03_2020-05-07

#### Added

- used the web service endpoint "https://showcase.linx.twenty57.net:8081/UnixTime/fromunix?timestamp=1587304498" to convert the unix system time in a user-friendly format

---

### 01.02_2020-05-07

#### Added

- "csv" function that creates a csv file with all the properties
- added timestamp

---

### 01.01_2020-05-04

- first version

---
By Sabaini Chiara 3CI a.s. 2019/2020

---
If you have any problem please contact me:

- 18762@studenti.marconiverona.edu.it.com
