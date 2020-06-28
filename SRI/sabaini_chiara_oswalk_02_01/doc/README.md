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
  - oswalk.py
- doc
  - README.md
- flussi
  - osstat_x.csv
  - osstat_w.csv
- log
  - log.log

---

### Execution examples

- osstat.py:
  - open the source code and set the "directory" variable to the name of the directory you want to work with, and the "directory_path" to the path of that directory
  - double click

---

## Changelog

- [OSSTAT](#osstat)
  - [Tags](#tags)
  - [Description](#description)
  - [Required](#required)
    - [Directories structure](#directories-structure)
    - [Execution examples](#execution-examples)
  - [Changelog](#changelog)
    - [02.01_2020-05-20](#02012020-05-20)
      - [Added](#added)
      - [Additional info](#additional-info)
    - [01.03_2020-05-07](#01032020-05-07)
      - [Added](#added-1)
    - [01.02_2020-05-07](#01022020-05-07)
      - [Added](#added-2)
    - [01.01_2020-05-04](#01012020-05-04)

---

### 02.01_2020-05-20

#### Added

- Checks for operating system type
- Handling of platform-agnostic file paths using os.path.join function
- Implemented system file permission (read, write, execute) octaves, with support for Windows and Unix-like operating systems

#### Additional info

- Tested both on Windows 10 and Debian Buster on WSL2

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
